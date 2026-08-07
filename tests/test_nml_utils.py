import os
import shutil
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


def test_history_with_indexing():
    path = Path(os.path.join(dir_path, "fixtures", "history_indexing.nml"))
    history = TraktorHistory(path)
    sorting_info = history.nml.indexing.sorting_info[0]
    assert sorting_info.path == "$HISTORY"
    assert sorting_info.criteria.attribute == "2"


def test_collection_with_indexing():
    path = Path(os.path.join(dir_path, "fixtures", "collection_indexing.nml"))
    collection = TraktorCollection(path)
    assert len(collection.nml.collection.entry) == 1


def test_collection_with_smartlists():
    path = Path(os.path.join(dir_path, "fixtures", "collection_smartlist.nml"))
    collection = TraktorCollection(path)
    assert len(collection.nml.collection.entry) == 1

    nodes = collection.nml.playlists.node.subnodes.node
    smartlist_node = next(node for node in nodes if node.type == "SMARTLIST")
    assert smartlist_node.name == "Instrumentals"
    assert smartlist_node.smartplaylist.uuid == "5566f26cd8414288a8ea378d0cc5ac55"
    assert (
        smartlist_node.smartplaylist.search_expression.query
        == '$COMMENT % "#Instrumental"'
    )


def test_add_entry_to_collection(tmpdir):
    collection_file = Path(os.path.join(dir_path, "fixtures", "collection.nml"))
    temp_collection = tmpdir.join("collection.nml")
    shutil.copy(src=collection_file, dst=temp_collection)

    # Operate on the temp copy so the committed fixture is never mutated.
    path = Path(str(temp_collection))
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


def _canonical(element):
    """Order-independent representation of an XML element tree."""
    return (
        element.tag,
        tuple(sorted(element.attrib.items())),
        (element.text or "").strip(),
        [_canonical(child) for child in element],
    )


def test_collection_v4_parses():
    """Traktor 4 (NML VERSION=20) collections parse, including new fields."""
    path = Path(os.path.join(dir_path, "fixtures", "collection_v4.nml"))
    collection = TraktorCollection(path)
    assert collection.nml.version == 20
    assert collection.nml.head.program == "Traktor Pro 4"

    loopinfos = [
        entry.loopinfo
        for entry in collection.nml.collection.entry
        if entry.loopinfo is not None
    ]
    assert loopinfos, "fixture should contain at least one LOOPINFO"
    loopinfo = loopinfos[0]
    # Attributes that Traktor 4 writes but the 3.x model silently dropped.
    assert loopinfo.original_title is not None
    assert loopinfo.original_loop_size is not None
    assert loopinfo.original_loop_start is not None


def test_collection_v4_roundtrip_is_lossless(tmp_path):
    """Parsing then saving a Traktor 4 collection must not change any data."""
    import xml.etree.ElementTree as ET

    src = Path(os.path.join(dir_path, "fixtures", "collection_v4.nml"))
    work = tmp_path / "collection_v4.nml"
    shutil.copy(src=src, dst=work)

    TraktorCollection(work).save()

    before = _canonical(ET.parse(str(src)).getroot())
    after = _canonical(ET.parse(str(work)).getroot())
    assert before == after


def test_collection_v4_float_formatting(tmp_path):
    """Floats keep Traktor's 6-decimal format; SAMPLE_TYPE_INFO stays integer."""
    src = Path(os.path.join(dir_path, "fixtures", "collection_v4.nml"))
    work = tmp_path / "collection_v4.nml"
    shutil.copy(src=src, dst=work)

    TraktorCollection(work).save()
    saved = work.read_text(encoding="utf8")

    assert 'BPM_QUALITY="100.000000"' in saved
    assert 'LEN="0.000000"' in saved
    assert 'BPM_QUALITY="100.0"' not in saved
    # NML VERSION >= 20 writes SAMPLE_TYPE_INFO as a bare integer, not a float.
    assert 'SAMPLE_TYPE_INFO="0"' in saved
    assert 'SAMPLE_TYPE_INFO="0.000000"' not in saved


def test_collection_v4_traktor_layout(tmp_path):
    """save() writes Traktor's on-disk layout: explicit close tags, one per line."""
    src = Path(os.path.join(dir_path, "fixtures", "collection_v4.nml"))
    work = tmp_path / "collection_v4.nml"
    shutil.copy(src=src, dst=work)

    TraktorCollection(work).save()
    lines = work.read_text(encoding="utf8").split("\n")

    # Traktor's exact XML declaration on its own first line.
    assert lines[0] == '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'
    # Traktor never self-closes elements (no "<X/>").
    assert "/>" not in work.read_text(encoding="utf8")
    # Empty elements are written explicitly, each closing tag ending a line.
    assert any(line.endswith("</LOCATION>") for line in lines)
    assert any(line.endswith("</ENTRY>") for line in lines)
    # One element per line means many lines, not a single blob.
    assert len(lines) > 50


def test_collection_v4_byte_exact_roundtrip(tmp_path):
    """A file already in Traktor's on-disk format must round-trip byte-for-byte.

    This guards the whole write path at once: attribute order, ">" left
    unescaped, 6-decimal floats, explicit close tags and per-line layout.
    """
    src = Path(os.path.join(dir_path, "fixtures", "collection_v4_traktor_format.nml"))
    work = tmp_path / src.name
    shutil.copy(src=src, dst=work)

    original = src.read_text(encoding="utf8")
    TraktorCollection(work).save()
    assert work.read_text(encoding="utf8") == original
