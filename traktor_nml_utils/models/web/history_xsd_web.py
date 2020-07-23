from dataclasses import dataclass, field
from typing import List, Optional


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

    head: Optional["Nml.Head"] = field(
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
    collection: Optional["Nml.Collection"] = field(
        default=None,
        metadata=dict(
            name="COLLECTION",
            type="Element",
            required=True
        )
    )
    sets: Optional["Nml.Sets"] = field(
        default=None,
        metadata=dict(
            name="SETS",
            type="Element",
            required=True
        )
    )
    playlists: Optional["Nml.Playlists"] = field(
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
            type="Attribute"
        )
    )

    @dataclass
    class Head:
        """
        :ivar value:
        :ivar company:
        :ivar program:
        """
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
    class Collection:
        """
        :ivar entry:
        :ivar entries:
        """
        entry: List["Nml.Collection.Entry"] = field(
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
        class Entry:
            """
            :ivar location:
            :ivar album:
            :ivar modification_info:
            :ivar info:
            :ivar tempo:
            :ivar loudness:
            :ivar musical_key:
            :ivar cue_v2:
            :ivar modified_date:
            :ivar modified_time:
            :ivar audio_id:
            :ivar title:
            :ivar artist:
            """
            location: Optional["Nml.Collection.Entry.Location"] = field(
                default=None,
                metadata=dict(
                    name="LOCATION",
                    type="Element",
                    required=True
                )
            )
            album: Optional["Nml.Collection.Entry.Album"] = field(
                default=None,
                metadata=dict(
                    name="ALBUM",
                    type="Element"
                )
            )
            modification_info: Optional["Nml.Collection.Entry.ModificationInfo"] = field(
                default=None,
                metadata=dict(
                    name="MODIFICATION_INFO",
                    type="Element",
                    required=True
                )
            )
            info: Optional["Nml.Collection.Entry.Info"] = field(
                default=None,
                metadata=dict(
                    name="INFO",
                    type="Element",
                    required=True
                )
            )
            tempo: Optional["Nml.Collection.Entry.Tempo"] = field(
                default=None,
                metadata=dict(
                    name="TEMPO",
                    type="Element"
                )
            )
            loudness: Optional["Nml.Collection.Entry.Loudness"] = field(
                default=None,
                metadata=dict(
                    name="LOUDNESS",
                    type="Element"
                )
            )
            musical_key: Optional["Nml.Collection.Entry.MusicalKey"] = field(
                default=None,
                metadata=dict(
                    name="MUSICAL_KEY",
                    type="Element"
                )
            )
            cue_v2: List["Nml.Collection.Entry.CueV2"] = field(
                default_factory=list,
                metadata=dict(
                    name="CUE_V2",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
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
            class Location:
                """
                :ivar value:
                :ivar dir:
                :ivar file:
                :ivar volume:
                :ivar volumeid:
                """
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
            class Album:
                """
                :ivar value:
                :ivar track:
                :ivar title:
                """
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

            @dataclass
            class ModificationInfo:
                """
                :ivar value:
                :ivar author_type:
                """
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
            class Info:
                """
                :ivar value:
                :ivar bitrate:
                :ivar label:
                :ivar comment:
                :ivar coverartid:
                :ivar key:
                :ivar playcount:
                :ivar playtime:
                :ivar playtime_float:
                :ivar ranking:
                :ivar import_date:
                :ivar last_played:
                :ivar flags:
                :ivar filesize:
                :ivar release_date:
                :ivar genre:
                :ivar key_lyrics:
                :ivar remixer:
                """
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
                label: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="LABEL",
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
                playtime_float: Optional[float] = field(
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
                import_date: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="IMPORT_DATE",
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
                release_date: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="RELEASE_DATE",
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
                key_lyrics: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="KEY_LYRICS",
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
            class Tempo:
                """
                :ivar value:
                :ivar bpm:
                :ivar bpm_quality:
                """
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

            @dataclass
            class Loudness:
                """
                :ivar value:
                :ivar peak_db:
                :ivar perceived_db:
                :ivar analyzed_db:
                """
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
            class MusicalKey:
                """
                :ivar value:
                :ivar value_attribute:
                """
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
            class CueV2:
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
    class Sets:
        """
        :ivar value:
        :ivar entries:
        """
        value: Optional[str] = field(
            default=None,
        )
        entries: Optional[int] = field(
            default=None,
            metadata=dict(
                name="ENTRIES",
                type="Attribute"
            )
        )

    @dataclass
    class Playlists:
        """
        :ivar node:
        """
        node: Optional["Nml.Playlists.Node"] = field(
            default=None,
            metadata=dict(
                name="NODE",
                type="Element",
                required=True
            )
        )

        @dataclass
        class Node:
            """
            :ivar subnodes:
            :ivar type:
            :ivar name:
            """
            subnodes: Optional["Nml.Playlists.Node.Subnodes"] = field(
                default=None,
                metadata=dict(
                    name="SUBNODES",
                    type="Element",
                    required=True
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
            class Subnodes:
                """
                :ivar node:
                :ivar count:
                """
                node: Optional["Nml.Playlists.Node.Subnodes.Node"] = field(
                    default=None,
                    metadata=dict(
                        name="NODE",
                        type="Element",
                        required=True
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
                class Node:
                    """
                    :ivar playlist:
                    :ivar type:
                    :ivar name:
                    """
                    playlist: Optional["Nml.Playlists.Node.Subnodes.Node.Playlist"] = field(
                        default=None,
                        metadata=dict(
                            name="PLAYLIST",
                            type="Element",
                            required=True
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
                    class Playlist:
                        """
                        :ivar entry:
                        :ivar entries:
                        :ivar type:
                        :ivar uuid:
                        """
                        entry: List["Nml.Playlists.Node.Subnodes.Node.Playlist.Entry"] = field(
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
                        class Entry:
                            """
                            :ivar primarykey:
                            :ivar extendeddata:
                            """
                            primarykey: Optional["Nml.Playlists.Node.Subnodes.Node.Playlist.Entry.Primarykey"] = field(
                                default=None,
                                metadata=dict(
                                    name="PRIMARYKEY",
                                    type="Element",
                                    required=True
                                )
                            )
                            extendeddata: Optional["Nml.Playlists.Node.Subnodes.Node.Playlist.Entry.Extendeddata"] = field(
                                default=None,
                                metadata=dict(
                                    name="EXTENDEDDATA",
                                    type="Element",
                                    required=True
                                )
                            )

                            @dataclass
                            class Primarykey:
                                """
                                :ivar value:
                                :ivar type:
                                :ivar key:
                                """
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
                            class Extendeddata:
                                """
                                :ivar value:
                                :ivar deck:
                                :ivar duration:
                                :ivar extendedtype:
                                :ivar playedpublic:
                                :ivar startdate:
                                :ivar starttime:
                                """
                                value: Optional[str] = field(
                                    default=None,
                                )
                                deck: Optional[int] = field(
                                    default=None,
                                    metadata=dict(
                                        name="DECK",
                                        type="Attribute"
                                    )
                                )
                                duration: Optional[float] = field(
                                    default=None,
                                    metadata=dict(
                                        name="DURATION",
                                        type="Attribute"
                                    )
                                )
                                extendedtype: Optional[str] = field(
                                    default=None,
                                    metadata=dict(
                                        name="EXTENDEDTYPE",
                                        type="Attribute"
                                    )
                                )
                                playedpublic: Optional[int] = field(
                                    default=None,
                                    metadata=dict(
                                        name="PLAYEDPUBLIC",
                                        type="Attribute"
                                    )
                                )
                                startdate: Optional[int] = field(
                                    default=None,
                                    metadata=dict(
                                        name="STARTDATE",
                                        type="Attribute"
                                    )
                                )
                                starttime: Optional[int] = field(
                                    default=None,
                                    metadata=dict(
                                        name="STARTTIME",
                                        type="Attribute"
                                    )
                                )
