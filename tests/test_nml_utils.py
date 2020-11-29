import os
from pathlib import Path

import pytest
from traktor_nml_utils.models.history import Nml as HistoryNml

from traktor_nml_utils import TraktorHistory

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.mark.parametrize(
    "nml_file", [os.path.join(dir_path, "fixtures", "history.nml")]
)
def test_history(nml_file):
    path = Path(nml_file)
    history = TraktorHistory(path)
    assert history.nml.playlists.node.subnodes.node.playlist.entry[0].extendeddata.deck == 1
