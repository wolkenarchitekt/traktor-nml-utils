import os
from pathlib import Path

import pytest
from traktor_nml_utils import TraktorHistory, TraktorCollection

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.mark.parametrize(
    "nml_file", [os.path.join(dir_path, "fixtures", "history.nml")]
)
def test_history(nml_file):
    path = Path(nml_file)
    history = TraktorHistory(path)
    assert (
        history.nml.playlists.node.subnodes.node.playlist.entry[0].extendeddata.deck
        == 1
    )


def test_collection_with_indexing():
    path = Path(os.path.join(dir_path, "fixtures", "collection_indexing.nml"))
    collection = TraktorCollection(path)
    assert len(collection.nml.collection.entry) == 1
