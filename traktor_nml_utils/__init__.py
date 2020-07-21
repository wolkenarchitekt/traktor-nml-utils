__version__ = "2.0.0"
from pathlib import Path

from traktor_nml_utils.models import Nml
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer


class TraktorCollection:
    parser = XmlParser()

    def __init__(self, path: Path):
        self.path = path
        self.model = self.parser.from_path(self.path, Nml)

    def save(self):
        with self.path.open(mode="w") as file_obj:
            serialized = XmlSerializer(pretty_print=True).render(self.model)
            file_obj.write(serialized)
