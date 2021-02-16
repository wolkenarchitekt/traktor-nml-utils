from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Albumtype:
    """
    :ivar value:
    :ivar track:
    :ivar title:
    :ivar of_tracks:
    """
    class Meta:
        name = "ALBUMType"

    value: Optional[str] = field(
        default=None,
    )
    track: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TRACK",
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
    of_tracks: Optional[int] = field(
        default=None,
        metadata=dict(
            name="OF_TRACKS",
            type="Attribute"
        )
    )


@dataclass
class Celltype:
    """
    :ivar value:
    :ivar index:
    :ivar cellname:
    :ivar color:
    :ivar sync:
    :ivar reverse:
    :ivar mode:
    :ivar type:
    :ivar speed:
    :ivar transpose:
    :ivar offset:
    :ivar nudge:
    :ivar gain:
    :ivar start_marker:
    :ivar end_marker:
    :ivar bpm:
    :ivar dir:
    :ivar file:
    :ivar volume:
    """
    class Meta:
        name = "CELLType"

    value: Optional[str] = field(
        default=None,
    )
    index: Optional[int] = field(
        default=None,
        metadata=dict(
            name="INDEX",
            type="Attribute"
        )
    )
    cellname: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CELLNAME",
            type="Attribute"
        )
    )
    color: Optional[int] = field(
        default=None,
        metadata=dict(
            name="COLOR",
            type="Attribute"
        )
    )
    sync: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SYNC",
            type="Attribute"
        )
    )
    reverse: Optional[int] = field(
        default=None,
        metadata=dict(
            name="REVERSE",
            type="Attribute"
        )
    )
    mode: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MODE",
            type="Attribute"
        )
    )
    type: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute"
        )
    )
    speed: Optional[float] = field(
        default=None,
        metadata=dict(
            name="SPEED",
            type="Attribute"
        )
    )
    transpose: Optional[float] = field(
        default=None,
        metadata=dict(
            name="TRANSPOSE",
            type="Attribute"
        )
    )
    offset: Optional[float] = field(
        default=None,
        metadata=dict(
            name="OFFSET",
            type="Attribute"
        )
    )
    nudge: Optional[float] = field(
        default=None,
        metadata=dict(
            name="NUDGE",
            type="Attribute"
        )
    )
    gain: Optional[float] = field(
        default=None,
        metadata=dict(
            name="GAIN",
            type="Attribute"
        )
    )
    start_marker: Optional[float] = field(
        default=None,
        metadata=dict(
            name="START_MARKER",
            type="Attribute"
        )
    )
    end_marker: Optional[float] = field(
        default=None,
        metadata=dict(
            name="END_MARKER",
            type="Attribute"
        )
    )
    bpm: Optional[float] = field(
        default=None,
        metadata=dict(
            name="BPM",
            type="Attribute"
        )
    )
    dir: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DIR",
            type="Attribute"
        )
    )
    file: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FILE",
            type="Attribute"
        )
    )
    volume: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VOLUME",
            type="Attribute"
        )
    )


@dataclass
class CueV2Type:
    """
    :ivar value:
    :ivar name:
    :ivar displ_order:
    :ivar type:
    :ivar start:
    :ivar len:
    :ivar repeats:
    :ivar hotcue:
    """
    class Meta:
        name = "CUE_V2Type"

    value: Optional[str] = field(
        default=None,
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NAME",
            type="Attribute"
        )
    )
    displ_order: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DISPL_ORDER",
            type="Attribute"
        )
    )
    type: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute"
        )
    )
    start: Optional[float] = field(
        default=None,
        metadata=dict(
            name="START",
            type="Attribute"
        )
    )
    len: Optional[float] = field(
        default=None,
        metadata=dict(
            name="LEN",
            type="Attribute"
        )
    )
    repeats: Optional[int] = field(
        default=None,
        metadata=dict(
            name="REPEATS",
            type="Attribute"
        )
    )
    hotcue: Optional[int] = field(
        default=None,
        metadata=dict(
            name="HOTCUE",
            type="Attribute"
        )
    )


@dataclass
class Headtype:
    """
    :ivar value:
    :ivar company:
    :ivar program:
    """
    class Meta:
        name = "HEADType"

    value: Optional[str] = field(
        default=None,
    )
    company: Optional[str] = field(
        default=None,
        metadata=dict(
            name="COMPANY",
            type="Attribute"
        )
    )
    program: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PROGRAM",
            type="Attribute"
        )
    )


@dataclass
class Infotype:
    """
    :ivar value:
    :ivar bitrate:
    :ivar genre:
    :ivar comment:
    :ivar coverartid:
    :ivar key:
    :ivar playtime:
    :ivar playtime_float:
    :ivar import_date:
    :ivar release_date:
    :ivar flags:
    :ivar filesize:
    :ivar label:
    :ivar key_lyrics:
    :ivar catalog_no:
    :ivar playcount:
    :ivar ranking:
    :ivar last_played:
    :ivar remixer:
    :ivar rating:
    :ivar producer:
    :ivar mix:
    """
    class Meta:
        name = "INFOType"

    value: Optional[str] = field(
        default=None,
    )
    bitrate: Optional[int] = field(
        default=None,
        metadata=dict(
            name="BITRATE",
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
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            name="KEY",
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
    playtime_float: Optional[float] = field(
        default=None,
        metadata=dict(
            name="PLAYTIME_FLOAT",
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
    release_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RELEASE_DATE",
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
    filesize: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FILESIZE",
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
    key_lyrics: Optional[str] = field(
        default=None,
        metadata=dict(
            name="KEY_LYRICS",
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
    playcount: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PLAYCOUNT",
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
    last_played: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST_PLAYED",
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
    rating: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RATING",
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
    mix: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MIX",
            type="Attribute"
        )
    )


@dataclass
class Locationtype:
    """
    :ivar value:
    :ivar dir:
    :ivar file:
    :ivar volume:
    :ivar volumeid:
    """
    class Meta:
        name = "LOCATIONType"

    value: Optional[str] = field(
        default=None,
    )
    dir: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DIR",
            type="Attribute"
        )
    )
    file: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FILE",
            type="Attribute"
        )
    )
    volume: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VOLUME",
            type="Attribute"
        )
    )
    volumeid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="VOLUMEID",
            type="Attribute"
        )
    )


@dataclass
class Loopinfotype:
    """
    :ivar value:
    :ivar sample_type_info:
    """
    class Meta:
        name = "LOOPINFOType"

    value: Optional[str] = field(
        default=None,
    )
    sample_type_info: Optional[float] = field(
        default=None,
        metadata=dict(
            name="SAMPLE_TYPE_INFO",
            type="Attribute"
        )
    )


@dataclass
class Loudnesstype:
    """
    :ivar value:
    :ivar peak_db:
    :ivar perceived_db:
    :ivar analyzed_db:
    """
    class Meta:
        name = "LOUDNESSType"

    value: Optional[str] = field(
        default=None,
    )
    peak_db: Optional[float] = field(
        default=None,
        metadata=dict(
            name="PEAK_DB",
            type="Attribute"
        )
    )
    perceived_db: Optional[float] = field(
        default=None,
        metadata=dict(
            name="PERCEIVED_DB",
            type="Attribute"
        )
    )
    analyzed_db: Optional[float] = field(
        default=None,
        metadata=dict(
            name="ANALYZED_DB",
            type="Attribute"
        )
    )


@dataclass
class ModificationInfotype:
    """
    :ivar value:
    :ivar author_type:
    """
    class Meta:
        name = "MODIFICATION_INFOType"

    value: Optional[str] = field(
        default=None,
    )
    author_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AUTHOR_TYPE",
            type="Attribute"
        )
    )


@dataclass
class MusicalKeytype:
    """
    :ivar value:
    :ivar value_attribute:
    """
    class Meta:
        name = "MUSICAL_KEYType"

    value: Optional[str] = field(
        default=None,
    )
    value_attribute: Optional[int] = field(
        default=None,
        metadata=dict(
            name="VALUE",
            type="Attribute"
        )
    )


@dataclass
class Primarykeytype:
    """
    :ivar value:
    :ivar type:
    :ivar key:
    """
    class Meta:
        name = "PRIMARYKEYType"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TYPE",
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


@dataclass
class SortingDatatype:
    """
    :ivar value:
    :ivar idx:
    :ivar ord:
    """
    class Meta:
        name = "SORTING_DATAType"

    value: Optional[str] = field(
        default=None,
    )
    idx: Optional[int] = field(
        default=None,
        metadata=dict(
            name="IDX",
            type="Attribute"
        )
    )
    ord: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ORD",
            type="Attribute"
        )
    )


@dataclass
class Stemstype:
    """
    :ivar value:
    :ivar stems:
    """
    class Meta:
        name = "STEMSType"

    value: Optional[str] = field(
        default=None,
    )
    stems: Optional[str] = field(
        default=None,
        metadata=dict(
            name="STEMS",
            type="Attribute"
        )
    )


@dataclass
class Subnodestype:
    """
    :ivar node:
    :ivar count:
    """
    class Meta:
        name = "SUBNODESType"

    node: List["Nodetype"] = field(
        default_factory=list,
        metadata=dict(
            name="NODE",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="COUNT",
            type="Attribute"
        )
    )


@dataclass
class Tempotype:
    """
    :ivar value:
    :ivar bpm:
    :ivar bpm_quality:
    :ivar bpm_transientcoherence:
    """
    class Meta:
        name = "TEMPOType"

    value: Optional[str] = field(
        default=None,
    )
    bpm: Optional[float] = field(
        default=None,
        metadata=dict(
            name="BPM",
            type="Attribute"
        )
    )
    bpm_quality: Optional[float] = field(
        default=None,
        metadata=dict(
            name="BPM_QUALITY",
            type="Attribute"
        )
    )
    bpm_transientcoherence: Optional[float] = field(
        default=None,
        metadata=dict(
            name="BPM_TRANSIENTCOHERENCE",
            type="Attribute"
        )
    )


@dataclass
class Entrytype:
    """
    :ivar location:
    :ivar album:
    :ivar modification_info:
    :ivar info:
    :ivar tempo:
    :ivar loudness:
    :ivar musical_key:
    :ivar loopinfo:
    :ivar cue_v2:
    :ivar stems:
    :ivar primarykey:
    :ivar modified_date:
    :ivar modified_time:
    :ivar lock:
    :ivar lock_modification_time:
    :ivar audio_id:
    :ivar title:
    :ivar artist:
    """
    class Meta:
        name = "ENTRYType"

    location: Optional[Locationtype] = field(
        default=None,
        metadata=dict(
            name="LOCATION",
            type="Element"
        )
    )
    album: Optional[Albumtype] = field(
        default=None,
        metadata=dict(
            name="ALBUM",
            type="Element"
        )
    )
    modification_info: Optional[ModificationInfotype] = field(
        default=None,
        metadata=dict(
            name="MODIFICATION_INFO",
            type="Element"
        )
    )
    info: Optional[Infotype] = field(
        default=None,
        metadata=dict(
            name="INFO",
            type="Element"
        )
    )
    tempo: Optional[Tempotype] = field(
        default=None,
        metadata=dict(
            name="TEMPO",
            type="Element"
        )
    )
    loudness: Optional[Loudnesstype] = field(
        default=None,
        metadata=dict(
            name="LOUDNESS",
            type="Element"
        )
    )
    musical_key: Optional[MusicalKeytype] = field(
        default=None,
        metadata=dict(
            name="MUSICAL_KEY",
            type="Element"
        )
    )
    loopinfo: Optional[Loopinfotype] = field(
        default=None,
        metadata=dict(
            name="LOOPINFO",
            type="Element"
        )
    )
    cue_v2: List[CueV2Type] = field(
        default_factory=list,
        metadata=dict(
            name="CUE_V2",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    stems: Optional[Stemstype] = field(
        default=None,
        metadata=dict(
            name="STEMS",
            type="Element"
        )
    )
    primarykey: Optional[Primarykeytype] = field(
        default=None,
        metadata=dict(
            name="PRIMARYKEY",
            type="Element"
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
    audio_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AUDIO_ID",
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
    artist: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ARTIST",
            type="Attribute"
        )
    )


@dataclass
class Slottype:
    """
    :ivar cell:
    :ivar keylock:
    :ivar fxenable:
    :ivar punchmode:
    :ivar active_cell_index:
    """
    class Meta:
        name = "SLOTType"

    cell: List[Celltype] = field(
        default_factory=list,
        metadata=dict(
            name="CELL",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    keylock: Optional[int] = field(
        default=None,
        metadata=dict(
            name="KEYLOCK",
            type="Attribute"
        )
    )
    fxenable: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FXENABLE",
            type="Attribute"
        )
    )
    punchmode: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PUNCHMODE",
            type="Attribute"
        )
    )
    active_cell_index: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ACTIVE_CELL_INDEX",
            type="Attribute"
        )
    )


@dataclass
class SortingOrdertype:
    """
    :ivar sorting_data:
    :ivar path:
    """
    class Meta:
        name = "SORTING_ORDERType"

    sorting_data: List[SortingDatatype] = field(
        default_factory=list,
        metadata=dict(
            name="SORTING_DATA",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    path: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PATH",
            type="Attribute"
        )
    )


@dataclass
class Collectiontype:
    """
    :ivar entry:
    :ivar entries:
    """
    class Meta:
        name = "COLLECTIONType"

    entry: List[Entrytype] = field(
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
            type="Attribute"
        )
    )


@dataclass
class Playlisttype:
    """
    :ivar content:
    :ivar entry:
    :ivar entries:
    :ivar type:
    :ivar uuid:
    """
    class Meta:
        name = "PLAYLISTType"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    entry: List[Entrytype] = field(
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
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute"
        )
    )
    uuid: Optional[str] = field(
        default=None,
        metadata=dict(
            name="UUID",
            type="Attribute"
        )
    )


@dataclass
class Settype:
    """
    :ivar location:
    :ivar album:
    :ivar modification_info:
    :ivar info:
    :ivar tempo:
    :ivar slot:
    :ivar title:
    :ivar artist:
    :ivar quant_val_ue:
    :ivar quant_state:
    """
    class Meta:
        name = "SETType"

    location: Optional[Locationtype] = field(
        default=None,
        metadata=dict(
            name="LOCATION",
            type="Element",
            required=True
        )
    )
    album: Optional[Albumtype] = field(
        default=None,
        metadata=dict(
            name="ALBUM",
            type="Element"
        )
    )
    modification_info: Optional[ModificationInfotype] = field(
        default=None,
        metadata=dict(
            name="MODIFICATION_INFO",
            type="Element",
            required=True
        )
    )
    info: Optional[Infotype] = field(
        default=None,
        metadata=dict(
            name="INFO",
            type="Element",
            required=True
        )
    )
    tempo: Optional[Tempotype] = field(
        default=None,
        metadata=dict(
            name="TEMPO",
            type="Element",
            required=True
        )
    )
    slot: List[Slottype] = field(
        default_factory=list,
        metadata=dict(
            name="SLOT",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TITLE",
            type="Attribute"
        )
    )
    artist: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ARTIST",
            type="Attribute"
        )
    )
    quant_val_ue: Optional[int] = field(
        default=None,
        metadata=dict(
            name="QUANT_VAlUE",
            type="Attribute"
        )
    )
    quant_state: Optional[int] = field(
        default=None,
        metadata=dict(
            name="QUANT_STATE",
            type="Attribute"
        )
    )


@dataclass
class Nodetype:
    """
    :ivar playlist:
    :ivar subnodes:
    :ivar type:
    :ivar name:
    """
    class Meta:
        name = "NODEType"

    playlist: Optional[Playlisttype] = field(
        default=None,
        metadata=dict(
            name="PLAYLIST",
            type="Element"
        )
    )
    subnodes: Optional[Subnodestype] = field(
        default=None,
        metadata=dict(
            name="SUBNODES",
            type="Element"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Attribute"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NAME",
            type="Attribute"
        )
    )


@dataclass
class Setstype:
    """
    :ivar set:
    :ivar entries:
    """
    class Meta:
        name = "SETSType"

    set: List[Settype] = field(
        default_factory=list,
        metadata=dict(
            name="SET",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    entries: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ENTRIES",
            type="Attribute"
        )
    )


@dataclass
class Playliststype:
    """
    :ivar node:
    """
    class Meta:
        name = "PLAYLISTSType"

    node: Optional[Nodetype] = field(
        default=None,
        metadata=dict(
            name="NODE",
            type="Element",
            required=True
        )
    )


@dataclass
class Nmltype:
    """
    :ivar head:
    :ivar musicfolders:
    :ivar collection:
    :ivar sets:
    :ivar playlists:
    :ivar indexing:
    :ivar sorting_order:
    :ivar version:
    """
    class Meta:
        name = "NMLType"

    head: Optional[Headtype] = field(
        default=None,
        metadata=dict(
            name="HEAD",
            type="Element",
            required=True
        )
    )
    musicfolders: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MUSICFOLDERS",
            type="Element",
            required=True
        )
    )
    collection: Optional[Collectiontype] = field(
        default=None,
        metadata=dict(
            name="COLLECTION",
            type="Element",
            required=True
        )
    )
    sets: Optional[Setstype] = field(
        default=None,
        metadata=dict(
            name="SETS",
            type="Element",
            required=True
        )
    )
    playlists: Optional[Playliststype] = field(
        default=None,
        metadata=dict(
            name="PLAYLISTS",
            type="Element",
            required=True
        )
    )
    indexing: Optional[str] = field(
        default=None,
        metadata=dict(
            name="INDEXING",
            type="Element",
            required=True
        )
    )
    sorting_order: List[SortingOrdertype] = field(
        default_factory=list,
        metadata=dict(
            name="SORTING_ORDER",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    version: Optional[int] = field(
        default=None,
        metadata=dict(
            name="VERSION",
            type="Attribute"
        )
    )


@dataclass
class Nml(Nmltype):
    class Meta:
        name = "NML"
