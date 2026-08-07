__version__ = "4.1.0"

import dataclasses
import re
import sys
from abc import ABC
from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from traktor_nml_utils.models.collection import Nml as CollectionNml
from traktor_nml_utils.models.history import Nml as HistoryNml

# Traktor writes floating-point attributes with a fixed 6 decimal places
# (e.g. BPM="122.000671", START="29.684317", LEN="0.000000"). xsdata
# re-serialises Python floats using the shortest repr, so "0.000000" becomes
# "0.0" and "136.204590" becomes "136.20459". The values stay numerically
# identical but the file changes textually; we restore Traktor's formatting.
FLOAT_DECIMALS = 6

# SAMPLE_TYPE_INFO is a float in Traktor 2.x/3.x collections ("0.000000") but
# Traktor 4.x (NML VERSION >= 20) writes it as a bare integer ("0"). It is the
# one float-typed attribute whose textual format depends on the file version.
VERSION_INT_FLOAT_ATTRS = {"SAMPLE_TYPE_INFO"}
TRAKTOR4_NML_VERSION = 20


class ParseError(Exception):
    pass


def is_history_file(path: Path):
    content = path.read_text(encoding="utf8")
    return "HistoryData" in content


def _float_attribute_names(nml) -> set:
    """Names of every XML attribute backed by a float dataclass field."""
    names = set()
    module = sys.modules[type(nml).__module__]
    for obj in vars(module).values():
        if dataclasses.is_dataclass(obj):
            for field_ in dataclasses.fields(obj):
                if "float" in str(field_.type):
                    name = field_.metadata.get("name")
                    if name:
                        names.add(name)
    return names


def restore_traktor_float_format(serialized: str, nml) -> str:
    """Re-apply Traktor's fixed-point float formatting to a serialized NML."""
    float_attrs = _float_attribute_names(nml)
    if not float_attrs:
        return serialized

    version = getattr(nml, "version", None) or 0
    pattern = re.compile(
        r"\b("
        + "|".join(sorted(float_attrs))
        + r')="(-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)"'
    )

    def _repl(match: "re.Match") -> str:
        attr, value = match.group(1), match.group(2)
        if attr in VERSION_INT_FLOAT_ATTRS and version >= TRAKTOR4_NML_VERSION:
            return f'{attr}="{int(float(value))}"'
        return f'{attr}="{float(value):.{FLOAT_DECIMALS}f}"'

    return pattern.sub(_repl, serialized)


# Traktor's exact XML prolog (note the space before "?>" and standalone="no").
TRAKTOR_XML_DECLARATION = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'


def format_traktor_layout(serialized: str) -> str:
    """Reformat a serialized NML document to match Traktor's on-disk layout.

    Traktor writes empty elements with explicit closing tags (``<X></X>``,
    never ``<X/>``) and puts exactly one newline after every closing tag.
    xsdata self-closes empty elements and emits the document on a single line,
    so we restore both. Angle brackets inside attribute values are always
    escaped (``&lt;`` / ``&gt;``), so these tag-based substitutions never touch
    attribute data.
    """
    # Drop xsdata's declaration and collapse any whitespace between tags.
    serialized = re.sub(r"^\s*<\?xml[^>]*\?>", "", serialized)
    serialized = re.sub(r">\s+<", "><", serialized).strip()

    # Traktor always double-quotes attributes, writing quotes inside values as
    # "&quot;" (e.g. the STEMS JSON). xsdata's sax-based writer switches to
    # single quotes for such values, so convert them back.
    def _double_quote_attr(match: "re.Match") -> str:
        value = match.group(2).replace('"', "&quot;")
        return f'{match.group(1)}"{value}"'

    serialized = re.sub(r"(\s[A-Za-z0-9_]+=)'([^']*)'", _double_quote_attr, serialized)
    # Traktor leaves ">" unescaped inside values (only "<", "&" and '"' are
    # escaped); xsdata escapes ">" as "&gt;", so undo that. Raw ">" is valid
    # XML in both attribute values and text, so this stays well-formed.
    serialized = serialized.replace("&gt;", ">")
    # Expand self-closing empty elements: <X .../> -> <X ...></X>
    serialized = re.sub(
        r"<([A-Za-z0-9_]+)((?:\s[^<>]*)?)/>", r"<\1\2></\1>", serialized
    )
    # One newline after every closing tag (leaves parent/first-child inline).
    serialized = re.sub(r"(</[A-Za-z0-9_]+>)", r"\1\n", serialized)
    return f"{TRAKTOR_XML_DECLARATION}\n{serialized}"


class TraktorNmlMixin(ABC):
    parser = XmlParser()

    def __init__(self, path, nml):
        self.path = path
        self.nml = nml

    def save(self):
        with self.path.open(mode="w", encoding="utf8") as file_obj:
            serialized = XmlSerializer().render(self.nml)
            serialized = restore_traktor_float_format(serialized, self.nml)
            serialized = format_traktor_layout(serialized)
            file_obj.write(serialized)


class TraktorCollection(TraktorNmlMixin):
    def __init__(self, path: Path):
        if is_history_file(path):
            raise ParseError(f"'{path}' is not a valid collection file")
        self.path = path
        self.nml: CollectionNml = self.parser.from_path(path, CollectionNml)
        super().__init__(path=path, nml=self.nml)


class TraktorHistory(TraktorNmlMixin):
    def __init__(self, path: Path):
        if not is_history_file(path):
            raise ParseError(f"'{path}' is not a valid history file")
        self.path = path
        self.nml: HistoryNml = self.parser.from_path(path, HistoryNml)
        super().__init__(path=path, nml=self.nml)
