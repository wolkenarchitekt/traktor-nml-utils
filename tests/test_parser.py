from traktor_nml_utils import TraktorCollection
import os
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_collection():
    collection = TraktorCollection(os.path.join(dir_path, 'fixtures/collection.nml'))
    assert collection.entries()
    for entry in collection.entries():
        print(entry.artist)
        print(entry.title)


def test_playlists():
    for filename in Path(os.path.expanduser('~/Documents/Native Instruments/Traktor 3.2.0/History')).rglob('*.nml'):
        collection = TraktorCollection(str(filename))
        # assert collection.playlists()
        print(filename, len(collection.playlists()))
