import os
import shutil
import tempfile
from pathlib import Path

from traktor_nml_utils import TraktorCollection, TraktorHistory
from traktor_nml_utils.models.collection import (
    CueV2Type,
    Entrytype,
    Infotype,
    Locationtype,
    Loudnesstype,
    ModificationInfotype,
    MusicalKeytype,
    Tempotype,
)

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_history():
    path = Path(os.path.join(dir_path, "fixtures", "history.nml"))
    history = TraktorHistory(path)
    assert (
        history.nml.playlists.node.subnodes.node.playlist.entry[0].extendeddata.deck
        == 1
    )


def test_collection_with_indexing():
    path = Path(os.path.join(dir_path, "fixtures", "collection_indexing.nml"))
    collection = TraktorCollection(path)
    assert len(collection.nml.collection.entry) == 1


def test_add_entry_to_collection(tmpdir):
    with tempfile.TemporaryFile() as fp:
        collection_file = Path(os.path.join(dir_path, "fixtures", "collection.nml"))
        temp_collection = tmpdir.join("collection.nml")
    shutil.copy(src=collection_file, dst=temp_collection)
    print(temp_collection)

    path = Path(os.path.join(dir_path, "fixtures", "collection.nml"))
    collection = TraktorCollection(path)
    entry = Entrytype(
        location=Locationtype(
            value=None,
            dir="/:Library/:Application Support/:Native Instruments/:Traktor 2/:Factory Sounds/:",
            file="Loopmasters_Dubstep1.mp3",
            volume="osx",
            volumeid="osx",
        ),
        album=None,
        modification_info=ModificationInfotype(value=None, author_type="user"),
        info=Infotype(
            value=None,
            bitrate=189720,
            genre="Dubstep",
            comment="Tracks by www.loopmasters.com",
            coverartid="113/R1PI3ZDLWQMLAAASJ4B2AQZXI1ZD",
            key="10m",
            playtime=193,
            playtime_float=192.078369,
            import_date="2010/8/16",
            release_date="2010/1/1",
            flags=28,
            filesize=5040,
            label=None,
            key_lyrics=None,
            catalog_no=None,
            playcount=None,
            ranking=None,
            last_played=None,
            remixer=None,
            rating=None,
            producer=None,
            mix=None,
        ),
        tempo=Tempotype(
            value=None, bpm=139.999924, bpm_quality=100.0, bpm_transientcoherence=None
        ),
        loudness=Loudnesstype(
            value=None, peak_db=-2.78208, perceived_db=0.0, analyzed_db=-2.0
        ),
        musical_key=MusicalKeytype(value=None, value_attribute=12),
        loopinfo=None,
        cue_v2=[
            CueV2Type(
                value=None,
                name="AutoGrid",
                displ_order=0,
                type=4,
                start=52.315876,
                len=0.0,
                repeats=-1,
                hotcue=0,
            ),
            CueV2Type(
                value=None,
                name="n.n.",
                displ_order=0,
                type=0,
                start=52.315876,
                len=0.0,
                repeats=-1,
                hotcue=7,
            ),
            CueV2Type(
                value=None,
                name="n.n.",
                displ_order=0,
                type=0,
                start=52.315876,
                len=0.0,
                repeats=-1,
                hotcue=6,
            ),
        ],
        stems=None,
        primarykey=None,
        modified_date="2019/10/19",
        modified_time=13047,
        lock=1,
        lock_modification_time="2019-08-23T21:27:21",
        title="Dubstep 1",
        artist="Loopmasters",
    )
    collection.nml.collection.entry.append(entry)
    collection.save()
    assert len(TraktorCollection(path).nml.collection.entry) == 2
