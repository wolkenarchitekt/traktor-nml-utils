import pytest
from pathlib import Path
import os

from traktor_nml_utils import TraktorCollection

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.mark.parametrize("nml_file", [
    os.path.join(dir_path, 'fixtures', 'history.nml')
])
def test_history(nml_file):
    collection = TraktorCollection(Path(nml_file))
    assert collection.nml.collection.entry[0]
