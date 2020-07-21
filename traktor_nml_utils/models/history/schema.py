from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Album:
    """
    :ivar title:
    :ivar track:
    """
    class Meta:
        name = "ALBUM"

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
class Extendeddata:
    """
    :ivar deck:
    :ivar duration:
    :ivar extendedtype:
    :ivar playedpublic:
    :ivar startdate:
    :ivar starttime:
    """
    class Meta:
        name = "EXTENDEDDATA"

    deck: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DECK",
            type="Attribute",
            required=True
        )
    )
    duration: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="DURATION",
            type="Attribute",
            required=True
        )
    )
    extendedtype: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EXTENDEDTYPE",
            type="Attribute",
            required=True
        )
    )
    playedpublic: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PLAYEDPUBLIC",
            type="Attribute",
            required=True
        )
    )
    startdate: Optional[int] = field(
        default=None,
        metadata=dict(
            name="STARTDATE",
            type="Attribute",
            required=True
        )
    )
    starttime: Optional[int] = field(
        default=None,
        metadata=dict(
            name="STARTTIME",
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
    :ivar playcount:
    :ivar playtime:
    :ivar playtime_float:
    :ivar ranking:
    :ivar release_date:
    :ivar remixer:
    """
    class Meta:
        name = "INFO"

    bitrate: Optional[int] = field(
        default=None,
        metadata=dict(
            name="BITRATE",
            type="Attribute",
            required=True
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
            type="Attribute",
            required=True
        )
    )
    flags: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FLAGS",
            type="Attribute",
            required=True
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
            type="Attribute",
            required=True
        )
    )
    playcount: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PLAYCOUNT",
            type="Attribute",
            required=True
        )
    )
    playtime: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PLAYTIME",
            type="Attribute",
            required=True
        )
    )
    playtime_float: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="PLAYTIME_FLOAT",
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
            type="Attribute",
            required=True
        )
    )
    peak_db: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="PEAK_DB",
            type="Attribute",
            required=True
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
class Playlists:
    class Meta:
        name = "PLAYLISTS"


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
class Sets:
    """
    :ivar entries:
    """
    class Meta:
        name = "SETS"

    entries: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ENTRIES",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Subnodes:
    """
    :ivar count:
    """
    class Meta:
        name = "SUBNODES"

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
            type="Attribute",
            required=True
        )
    )


@dataclass
class Entry:
    """
    :ivar location:
    :ivar album:
    :ivar modification_info:
    :ivar info:
    :ivar primarykey:
    :ivar extendeddata:
    :ivar tempo:
    :ivar loudness:
    :ivar musical_key:
    :ivar cue_v2:
    :ivar artist:
    :ivar audio_id:
    :ivar modified_date:
    :ivar modified_time:
    :ivar title:
    """
    class Meta:
        name = "ENTRY"

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
    primarykey: Optional[Primarykey] = field(
        default=None,
        metadata=dict(
            name="PRIMARYKEY",
            type="Element",
            required=True
        )
    )
    extendeddata: Optional[Extendeddata] = field(
        default=None,
        metadata=dict(
            name="EXTENDEDDATA",
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
    loudness: Optional[Loudness] = field(
        default=None,
        metadata=dict(
            name="LOUDNESS",
            type="Element",
            required=True
        )
    )
    musical_key: Optional[MusicalKey] = field(
        default=None,
        metadata=dict(
            name="MUSICAL_KEY",
            type="Element",
            required=True
        )
    )
    cue_v2: List[CueV2] = field(
        default_factory=list,
        metadata=dict(
            name="CUE_V2",
            type="Element",
            min_occurs=1,
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
class Nml:
    """
    :ivar head:
    :ivar musicfolders:
    :ivar collection:
    :ivar sets:
    :ivar playlists:
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
    version: Optional[int] = field(
        default=None,
        metadata=dict(
            name="VERSION",
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
