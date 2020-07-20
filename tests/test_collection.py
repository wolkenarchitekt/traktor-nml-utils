import os
from pathlib import Path

from traktor_nml_utils.models import Nml
from xsdata.formats.dataclass.parsers import XmlParser

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = XmlParser()


def test_collection_read():
    obj = parser.from_path(
        Path(os.path.join(dir_path, "fixtures", "collection.nml")), Nml
    )
    assert (
        obj.collection.entry[0].location.dir
        == "/:Library/:Application Support/:Native Instruments/:Traktor 2/:Factory Sounds/:"
    )
