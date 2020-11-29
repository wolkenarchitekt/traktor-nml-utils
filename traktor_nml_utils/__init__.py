__version__ = "2.0.6"

from abc import ABC
from pathlib import Path

from traktor_nml_utils.models.collection import Nml as CollectionNml
from traktor_nml_utils.models.history import Nml as HistoryNml
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer


class ParseError(Exception):
    pass


def is_history_file(path: Path):
    content = open(path).read()
    return "HistoryData" in content


class TraktorNmlMixin(ABC):
    parser = XmlParser()

    def __init__(self, path: Path, model):
        self.path = path
        self.nml = model

    def save(self):
        with self.path.open(mode="w") as file_obj:
            serialized = XmlSerializer(pretty_print=True).render(self.nml)
            serialized = serialized.split("\n")
            serialized = "\n".join(line.lstrip() for line in serialized)
            file_obj.write(serialized)


class TraktorCollection(TraktorNmlMixin):
    def __init__(self, path: Path):
        if is_history_file(path):
            nml = self.parser.from_path(path, HistoryNml)
        else:
            nml = self.parser.from_path(path, CollectionNml)
        super().__init__(path=path, model=nml)
