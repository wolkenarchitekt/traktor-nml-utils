from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Album:
    """
    :ivar of_tracks:
    :ivar title:
    :ivar track:
    """
    class Meta:
        name = "ALBUM"

    of_tracks: Optional[int] = field(
        default=None,
        metadata=dict(
            name="OF_TRACKS",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TITLE",
            type="Attribute"
        )
    )
    track: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TRACK",
            type="Attribute"
        )
    )


@dataclass
class Cell:
    """
    :ivar bpm:
    :ivar cellname:
    :ivar color:
    :ivar dir:
    :ivar end_marker:
    :ivar file:
    :ivar gain:
    :ivar index:
    :ivar mode:
    :ivar nudge:
    :ivar offset:
    :ivar reverse:
    :ivar speed:
    :ivar start_marker:
    :ivar sync:
    :ivar transpose:
    :ivar type:
    :ivar volume:
    """
    class Meta:
        name = "CELL"

    bpm: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="BPM",
            type="Attribute",
            required=True
        )
    )
    cellname: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CELLNAME",
            type="Attribute",
            required=True
        )
    )
    color: Optional[int] = field(
        default=None,
        metadata=dict(
            name="COLOR",
            type="Attribute",
            required=True
        )
    )
    dir: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DIR",
            type="Attribute",
            required=True
        )
    )
    end_marker: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="END_MARKER",
            type="Attribute",
            required=True
        )
    )
    file: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FILE",
            type="Attribute",
            required=True
        )
    )
    gain: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="GAIN",
            type="Attribute",
            required=True
        )
    )
    index: Optional[int] = field(
        default=None,
        metadata=dict(
            name="INDEX",
            type="Attribute",
            required=True
        )
    )
    mode: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MODE",
            type="Attribute",
            required=True
        )
    )
    nudge: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="NUDGE",
            type="Attribute",
            required=True
        )
    )
    offset: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="OFFSET",
            type="Attribute",
            required=True
        )
    )
    reverse: Optional[int] = field(
        default=None,
        metadata=dict(
            name="REVERSE",
            type="Attribute",
            required=True
        )
    )
    speed: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="SPEED",
            type="Attribute",
            required=True
        )
    )
    start_marker: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="START_MARKER",
            type="Attribute",
            required=True
        )
    )
    sync: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SYNC",
            type="Attribute",
            required=True
        )
    )
    transpose: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="TRANSPOSE",
            type="Attribute",
            required=True
        )
    )
    type: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute",
            required=True
        )
    )
    volume: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VOLUME",
            type="Attribute",
            required=True
        )
    )


@dataclass
class CueV2:
    """
    :ivar displ_order:
    :ivar hotcue:
    :ivar len:
    :ivar name:
    :ivar repeats:
    :ivar start:
    :ivar type:
    """
    class Meta:
        name = "CUE_V2"

    displ_order: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DISPL_ORDER",
            type="Attribute",
            required=True
        )
    )
    hotcue: Optional[int] = field(
        default=None,
        metadata=dict(
            name="HOTCUE",
            type="Attribute",
            required=True
        )
    )
    len: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="LEN",
            type="Attribute",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NAME",
            type="Attribute",
            required=True
        )
    )
    repeats: Optional[int] = field(
        default=None,
        metadata=dict(
            name="REPEATS",
            type="Attribute",
            required=True
        )
    )
    start: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="START",
            type="Attribute",
            required=True
        )
    )
    type: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Head:
    """
    :ivar company:
    :ivar program:
    """
    class Meta:
        name = "HEAD"

    company: Optional[str] = field(
        default=None,
        metadata=dict(
            name="COMPANY",
            type="Attribute",
            required=True
        )
    )
    program: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PROGRAM",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Info:
    """
    :ivar bitrate:
    :ivar catalog_no:
    :ivar comment:
    :ivar coverartid:
    :ivar filesize:
    :ivar flags:
    :ivar genre:
    :ivar import_date:
    :ivar key:
    :ivar key_lyrics:
    :ivar label:
    :ivar last_played:
    :ivar mix:
    :ivar playcount:
    :ivar playtime:
    :ivar playtime_float:
    :ivar producer:
    :ivar ranking:
    :ivar rating:
    :ivar release_date:
    :ivar remixer:
    """
    class Meta:
        name = "INFO"

    bitrate: Optional[int] = field(
        default=None,
        metadata=dict(
            name="BITRATE",
            type="Attribute"
        )
    )
    catalog_no: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CATALOG_NO",
            type="Attribute"
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="COMMENT",
            type="Attribute"
        )
    )
    coverartid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="COVERARTID",
            type="Attribute"
        )
    )
    filesize: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FILESIZE",
            type="Attribute"
        )
    )
    flags: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FLAGS",
            type="Attribute"
        )
    )
    genre: Optional[str] = field(
        default=None,
        metadata=dict(
            name="GENRE",
            type="Attribute"
        )
    )
    import_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IMPORT_DATE",
            type="Attribute"
        )
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="KEY",
            type="Attribute"
        )
    )
    key_lyrics: Optional[str] = field(
        default=None,
        metadata=dict(
            name="KEY_LYRICS",
            type="Attribute"
        )
    )
    label: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LABEL",
            type="Attribute"
        )
    )
    last_played: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST_PLAYED",
            type="Attribute"
        )
    )
    mix: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MIX",
            type="Attribute"
        )
    )
    playcount: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PLAYCOUNT",
            type="Attribute"
        )
    )
    playtime: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PLAYTIME",
            type="Attribute"
        )
    )
    playtime_float: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="PLAYTIME_FLOAT",
            type="Attribute"
        )
    )
    producer: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PRODUCER",
            type="Attribute"
        )
    )
    ranking: Optional[int] = field(
        default=None,
        metadata=dict(
            name="RANKING",
            type="Attribute"
        )
    )
    rating: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RATING",
            type="Attribute"
        )
    )
    release_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RELEASE_DATE",
            type="Attribute"
        )
    )
    remixer: Optional[str] = field(
        default=None,
        metadata=dict(
            name="REMIXER",
            type="Attribute"
        )
    )


@dataclass
class Location:
    """
    :ivar dir:
    :ivar file:
    :ivar volume:
    :ivar volumeid:
    """
    class Meta:
        name = "LOCATION"

    dir: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DIR",
            type="Attribute",
            required=True
        )
    )
    file: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FILE",
            type="Attribute",
            required=True
        )
    )
    volume: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VOLUME",
            type="Attribute",
            required=True
        )
    )
    volumeid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VOLUMEID",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Loudness:
    """
    :ivar analyzed_db:
    :ivar peak_db:
    :ivar perceived_db:
    """
    class Meta:
        name = "LOUDNESS"

    analyzed_db: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="ANALYZED_DB",
            type="Attribute"
        )
    )
    peak_db: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="PEAK_DB",
            type="Attribute"
        )
    )
    perceived_db: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="PERCEIVED_DB",
            type="Attribute",
            required=True
        )
    )


@dataclass
class ModificationInfo:
    """
    :ivar author_type:
    """
    class Meta:
        name = "MODIFICATION_INFO"

    author_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AUTHOR_TYPE",
            type="Attribute",
            required=True
        )
    )


@dataclass
class MusicalKey:
    """
    :ivar value:
    """
    class Meta:
        name = "MUSICAL_KEY"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="VALUE",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Musicfolders:
    class Meta:
        name = "MUSICFOLDERS"


@dataclass
class Primarykey:
    """
    :ivar key:
    :ivar type:
    """
    class Meta:
        name = "PRIMARYKEY"

    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="KEY",
            type="Attribute",
            required=True
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute",
            required=True
        )
    )


@dataclass
class SortingData:
    """
    :ivar idx:
    :ivar ord:
    """
    class Meta:
        name = "SORTING_DATA"

    idx: Optional[int] = field(
        default=None,
        metadata=dict(
            name="IDX",
            type="Attribute",
            required=True
        )
    )
    ord: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ORD",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Subnodes:
    """
    :ivar node:
    :ivar count:
    """
    class Meta:
        name = "SUBNODES"

    node: List["Node"] = field(
        default_factory=list,
        metadata=dict(
            name="NODE",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="COUNT",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Tempo:
    """
    :ivar bpm:
    :ivar bpm_quality:
    :ivar bpm_transientcoherence:
    """
    class Meta:
        name = "TEMPO"

    bpm: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="BPM",
            type="Attribute",
            required=True
        )
    )
    bpm_quality: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="BPM_QUALITY",
            type="Attribute"
        )
    )
    bpm_transientcoherence: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="BPM_TRANSIENTCOHERENCE",
            type="Attribute"
        )
    )


@dataclass
class Entry:
    """
    :ivar primarykey:
    :ivar location:
    :ivar album:
    :ivar modification_info:
    :ivar info:
    :ivar tempo:
    :ivar loudness:
    :ivar musical_key:
    :ivar cue_v2:
    :ivar artist:
    :ivar audio_id:
    :ivar lock:
    :ivar lock_modification_time:
    :ivar modified_date:
    :ivar modified_time:
    :ivar title:
    """
    class Meta:
        name = "ENTRY"

    primarykey: Optional[Primarykey] = field(
        default=None,
        metadata=dict(
            name="PRIMARYKEY",
            type="Element"
        )
    )
    location: Optional[Location] = field(
        default=None,
        metadata=dict(
            name="LOCATION",
            type="Element"
        )
    )
    album: Optional[Album] = field(
        default=None,
        metadata=dict(
            name="ALBUM",
            type="Element"
        )
    )
    modification_info: Optional[ModificationInfo] = field(
        default=None,
        metadata=dict(
            name="MODIFICATION_INFO",
            type="Element"
        )
    )
    info: Optional[Info] = field(
        default=None,
        metadata=dict(
            name="INFO",
            type="Element"
        )
    )
    tempo: Optional[Tempo] = field(
        default=None,
        metadata=dict(
            name="TEMPO",
            type="Element"
        )
    )
    loudness: Optional[Loudness] = field(
        default=None,
        metadata=dict(
            name="LOUDNESS",
            type="Element"
        )
    )
    musical_key: Optional[MusicalKey] = field(
        default=None,
        metadata=dict(
            name="MUSICAL_KEY",
            type="Element"
        )
    )
    cue_v2: List[CueV2] = field(
        default_factory=list,
        metadata=dict(
            name="CUE_V2",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    artist: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ARTIST",
            type="Attribute"
        )
    )
    audio_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AUDIO_ID",
            type="Attribute"
        )
    )
    lock: Optional[int] = field(
        default=None,
        metadata=dict(
            name="LOCK",
            type="Attribute"
        )
    )
    lock_modification_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LOCK_MODIFICATION_TIME",
            type="Attribute"
        )
    )
    modified_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MODIFIED_DATE",
            type="Attribute"
        )
    )
    modified_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MODIFIED_TIME",
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TITLE",
            type="Attribute"
        )
    )


@dataclass
class Slot:
    """
    :ivar cell:
    :ivar active_cell_index:
    :ivar fxenable:
    :ivar keylock:
    :ivar punchmode:
    """
    class Meta:
        name = "SLOT"

    cell: List[Cell] = field(
        default_factory=list,
        metadata=dict(
            name="CELL",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    active_cell_index: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ACTIVE_CELL_INDEX",
            type="Attribute",
            required=True
        )
    )
    fxenable: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FXENABLE",
            type="Attribute",
            required=True
        )
    )
    keylock: Optional[int] = field(
        default=None,
        metadata=dict(
            name="KEYLOCK",
            type="Attribute",
            required=True
        )
    )
    punchmode: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PUNCHMODE",
            type="Attribute",
            required=True
        )
    )


@dataclass
class SortingOrder:
    """
    :ivar sorting_data:
    :ivar path:
    """
    class Meta:
        name = "SORTING_ORDER"

    sorting_data: List[SortingData] = field(
        default_factory=list,
        metadata=dict(
            name="SORTING_DATA",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    path: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PATH",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Collection:
    """
    :ivar entry:
    :ivar entries:
    """
    class Meta:
        name = "COLLECTION"

    entry: List[Entry] = field(
        default_factory=list,
        metadata=dict(
            name="ENTRY",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    entries: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ENTRIES",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Playlist:
    """
    :ivar entry:
    :ivar entries:
    :ivar type:
    :ivar uuid:
    """
    class Meta:
        name = "PLAYLIST"

    entry: List[Entry] = field(
        default_factory=list,
        metadata=dict(
            name="ENTRY",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    entries: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ENTRIES",
            type="Attribute",
            required=True
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute",
            required=True
        )
    )
    uuid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UUID",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Set:
    """
    :ivar location:
    :ivar modification_info:
    :ivar info:
    :ivar tempo:
    :ivar slot:
    :ivar artist:
    :ivar quant_state:
    :ivar quant_val_ue:
    :ivar title:
    """
    class Meta:
        name = "SET"

    location: Optional[Location] = field(
        default=None,
        metadata=dict(
            name="LOCATION",
            type="Element",
            required=True
        )
    )
    modification_info: Optional[ModificationInfo] = field(
        default=None,
        metadata=dict(
            name="MODIFICATION_INFO",
            type="Element",
            required=True
        )
    )
    info: Optional[Info] = field(
        default=None,
        metadata=dict(
            name="INFO",
            type="Element",
            required=True
        )
    )
    tempo: Optional[Tempo] = field(
        default=None,
        metadata=dict(
            name="TEMPO",
            type="Element",
            required=True
        )
    )
    slot: List[Slot] = field(
        default_factory=list,
        metadata=dict(
            name="SLOT",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    artist: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ARTIST",
            type="Attribute",
            required=True
        )
    )
    quant_state: Optional[int] = field(
        default=None,
        metadata=dict(
            name="QUANT_STATE",
            type="Attribute",
            required=True
        )
    )
    quant_val_ue: Optional[int] = field(
        default=None,
        metadata=dict(
            name="QUANT_VAlUE",
            type="Attribute",
            required=True
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TITLE",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Node:
    """
    :ivar subnodes:
    :ivar playlist:
    :ivar name:
    :ivar type:
    """
    class Meta:
        name = "NODE"

    subnodes: Optional[Subnodes] = field(
        default=None,
        metadata=dict(
            name="SUBNODES",
            type="Element"
        )
    )
    playlist: Optional[Playlist] = field(
        default=None,
        metadata=dict(
            name="PLAYLIST",
            type="Element"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NAME",
            type="Attribute",
            required=True
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Sets:
    """
    :ivar set:
    :ivar entries:
    """
    class Meta:
        name = "SETS"

    set: List[Set] = field(
        default_factory=list,
        metadata=dict(
            name="SET",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    entries: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ENTRIES",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Playlists:
    """
    :ivar node:
    """
    class Meta:
        name = "PLAYLISTS"

    node: Optional[Node] = field(
        default=None,
        metadata=dict(
            name="NODE",
            type="Element",
            required=True
        )
    )


@dataclass
class Nml:
    """
    :ivar head:
    :ivar musicfolders:
    :ivar collection:
    :ivar sets:
    :ivar playlists:
    :ivar sorting_order:
    :ivar version:
    """
    class Meta:
        name = "NML"

    head: Optional[Head] = field(
        default=None,
        metadata=dict(
            name="HEAD",
            type="Element",
            required=True
        )
    )
    musicfolders: Optional[Musicfolders] = field(
        default=None,
        metadata=dict(
            name="MUSICFOLDERS",
            type="Element",
            required=True
        )
    )
    collection: Optional[Collection] = field(
        default=None,
        metadata=dict(
            name="COLLECTION",
            type="Element",
            required=True
        )
    )
    sets: Optional[Sets] = field(
        default=None,
        metadata=dict(
            name="SETS",
            type="Element",
            required=True
        )
    )
    playlists: Optional[Playlists] = field(
        default=None,
        metadata=dict(
            name="PLAYLISTS",
            type="Element",
            required=True
        )
    )
    sorting_order: List[SortingOrder] = field(
        default_factory=list,
        metadata=dict(
            name="SORTING_ORDER",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    version: Optional[int] = field(
        default=None,
        metadata=dict(
            name="VERSION",
            type="Attribute",
            required=True
        )
    )
