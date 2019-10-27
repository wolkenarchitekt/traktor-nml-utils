from traktor_nml_utils import TraktorCollection
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_collection():
    collection = TraktorCollection(os.path.join(dir_path, 'fixtures/collection.nml'))
    assert collection.entries()
    for entry in collection.entries():
        print(entry.artist)
        print(entry.title)


def test_playlists():
    collection = TraktorCollection(os.path.join(dir_path, 'fixtures/history.nml'))
    #assert collection.playlists()
    print(len(collection.playlists()))
