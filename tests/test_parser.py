import logging
import os
import shutil
from pathlib import Path

from traktor_nml_utils import TraktorCollection, TraktorHistory

logger = logging.getLogger(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))


def test_parse_nml_files(nml_dir: Path):
    for path in nml_dir.glob("**/*.nml"):
        print(path)
        if path.name.startswith("collection"):
            logger.info(f"Parsing collection: {path}")
            TraktorCollection(path=path)
        if path.name.startswith("history"):
            logger.info(f"Parsing history: {path}")
            TraktorHistory(path=path)


def test_parse_collection():
    path = Path(os.path.join(dir_path, "fixtures", "collection.nml"))
    traktor_collection = TraktorCollection(path=path)
    assert len(traktor_collection.nml.collection.entry) == 1
    entry = traktor_collection.nml.collection.entry[0]
    assert entry.location.dir == (
        "/:Library/:Application Support/:Native Instruments/:Traktor 2/:Factory Sounds/:"
    )


def test_save_artist(tmp_path: Path):
    tmp_collection_path = tmp_path / "collection.nml"
    shutil.copy(
        Path(os.path.join(dir_path, "fixtures", "collection.nml")), tmp_collection_path
    )

    traktor_collection = TraktorCollection(path=tmp_collection_path)
    entry = traktor_collection.nml.collection.entry[0]
    entry.artist = "Foobar"
    traktor_collection.save()

    assert "Foobar" in open(tmp_collection_path).read()
