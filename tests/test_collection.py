import os
from decimal import Decimal
from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser

from traktor_nml_utils import TraktorCollection

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = XmlParser()


def test_read_collection():
    path = Path(os.path.join(dir_path, "fixtures", "collection.nml"))
    collection = TraktorCollection(path=path)
    assert (
        collection.model.entry[0].location.dir
        == "/:Library/:Application Support/:Native Instruments/:Traktor 2/:Factory Sounds/:"
    )


def test_read_collection_full():
    path = Path(os.path.join(dir_path, "fixtures", "collection_full.nml"))
    collection = TraktorCollection(path=path)

    # assert obj.collection.entry[0].tempo.bpm == Decimal("139.999924")
    # assert obj.collection.entry[0].musical_key.value == 12
#
#
# def test_write_collection():
#     obj = parser.from_path(
#         Path(os.path.join(dir_path, "fixtures", "collection.nml")), Nml
#     )
#     assert obj.collection.entry[0].tempo.bpm == Decimal("123")
#
#
