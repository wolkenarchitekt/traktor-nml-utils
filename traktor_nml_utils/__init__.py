from pathlib import Path

from traktor_nml_utils.models.collection import Nml as CollectionNml
from traktor_nml_utils.models.history import Nml as HistoryNml
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer


class TraktorCollection:
    parser = XmlParser()

    def __init__(self, path: Path):
        self.path = path
        self.model = self.parser.from_path(self.path, CollectionNml).collection

    def save(self):
        with self.path.open(mode="w") as file_obj:
            serialized = XmlSerializer(pretty_print=True).render(self.model)
            file_obj.write(serialized)


class TraktorHistory:
    parser = XmlParser()

    def __init__(self, path: Path):
        self.path = path
        self.model = self.parser.from_path(self.path, HistoryNml).collection

    def save(self):
        with self.path.open(mode="w") as file_obj:
            serialized = XmlSerializer(pretty_print=True).render(self.model)
            file_obj.write(serialized)
