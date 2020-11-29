import os
from pathlib import Path

import pytest

from traktor_nml_utils import TraktorHistory

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.mark.parametrize(
    "nml_file", [os.path.join(dir_path, "fixtures", "history.nml")]
)
def test_history(nml_file):
    collection = TraktorHistory(Path(nml_file))
    assert collection.nml.collection.entry[0]
