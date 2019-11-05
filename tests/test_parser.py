from shutil import copy2 as copy
import pytest
import os

from traktor_nml_utils import TraktorCollection

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.mark.parametrize("nml_file", [
    os.path.join(dir_path, 'fixtures', 'collection.nml'),
])
def test_collection(nml_file):
    nml_file = os.path.join(dir_path, 'fixtures', 'collection.nml')
    collection = TraktorCollection(os.path.join(dir_path, nml_file))
    assert collection.entries
    entry = collection.entries[0]
    assert entry.dir == \
        '/:Library/:Application Support/:Native Instruments/:Traktor 2/:Factory Sounds/:'
    assert entry.bitrate == 189720
    assert entry.bpm == 139.999924
    assert entry.volume == 'osx'


@pytest.mark.parametrize("nml_file", [
    os.path.join(dir_path, 'fixtures', 'playlist.nml')
])
def test_playlists(nml_file):
    collection = TraktorCollection(nml_file)
    assert collection.playlists
    playlist = collection.playlists[0]
    assert playlist.name == 'Preparation'
    assert len(playlist.entries) == 1


@pytest.mark.parametrize("nml_file", [
    os.path.join(dir_path, 'fixtures', 'collection.nml')
])
def test_update(nml_file, tmpdir):
    nml_file = copy(os.path.join(dir_path, 'fixtures', 'collection.nml'), tmpdir)
    collection = TraktorCollection(nml_file)
    entry = collection.entries[0]
    entry.volume = 'blablu'
    entry.save()
    assert 'blablu' in open(nml_file).read()


@pytest.mark.parametrize("nml_file", [
    os.path.join(dir_path, 'fixtures', 'cuepoints.nml')
])
def test_cuepoints(nml_file):
    collection = TraktorCollection(nml_file)
    entry = collection.entries[0]
    assert len(entry.cuepoints) == 3
    cuepoint = entry.cuepoints[0]
    assert cuepoint.name == 'AutoGrid'
    assert cuepoint.cuepoint_type == 4
    assert cuepoint.start == 52.315876
    assert cuepoint.length == 0
    assert cuepoint.repeats == -1
    assert cuepoint.hotcue == 0


@pytest.mark.parametrize("nml_file", [
    os.path.join(dir_path, 'fixtures', 'history.nml')
])
def test_history(nml_file):
    collection = TraktorCollection(nml_file)
    assert collection.history
    history_entry = collection.history[0]
    assert history_entry.deck == 1
    assert history_entry.duration == 241.700394
    assert history_entry.played_public
    assert history_entry.startdate == 132319762
    assert history_entry.starttime == 68839
    assert history_entry.filename == \
        'Transcend/:DJing/:beatport_steve/:09 Change (Like Mix Extended Instrumental).mp3'


def test_travis():
    assert False
