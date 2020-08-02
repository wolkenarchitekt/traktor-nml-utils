import os
from pathlib import Path

import pytest

from traktor_nml_utils import TraktorCollection
from traktor_nml_utils.models.collection import Nml as CollectionNml
from traktor_nml_utils.models.history import Nml as HistoryNml
from xsdata.formats.dataclass.parsers import XmlParser

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = XmlParser()


@pytest.mark.parametrize(
    "nml_file,model",
    [("collection_full.nml", CollectionNml), ("history.nml", HistoryNml)],
)
def test_parsing_without_error(nml_file, model):
    path = Path(os.path.join(dir_path, "fixtures", nml_file))
    parser = XmlParser()
    parser.from_path(path, model)


def test_nml_wrapper():
    path = Path(os.path.join(dir_path, "fixtures", "collection.nml"))
    collection = TraktorCollection(path=path)
    assert len(collection.model.entry) == 1
    entry = collection.model.entry[0]
    assert entry.location.dir == (
        "/:Library/:Application Support/:Native Instruments/:Traktor 2/:Factory Sounds/:"
    )
