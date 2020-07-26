import datetime
import os
from dataclasses import dataclass, field
from lxml import etree
from traktor_nml_utils.xmldataclass import XMLdataclass

dir_path = os.path.dirname(os.path.realpath(__file__))

PLAYLIST_ROOT_XPATH = "/PLAYLISTS/NODE[@TYPE='FOLDER'][@NAME='$ROOT']"
FOLDER_XPATH = "./SUBNODES/NODE[@TYPE='FOLDER']"
PLAYLIST_XPATH = "./SUBNODES/NODE[@TYPE='PLAYLIST']"
ENTRY_XPATH = "/COLLECTION/ENTRY"

PLAYLIST_ENTRY_XPATH = "./ENTRY"

HISTORY_XPATH = (
    "/PLAYLISTS/NODE[@TYPE='FOLDER']"
    "/SUBNODES/NODE[@TYPE='PLAYLIST'][@NAME='HISTORY']"
    "/PLAYLIST/ENTRY"
)


@dataclass(init=False)
class Playlist(XMLdataclass):
    def __init__(self, xmltree: etree.Element, xmlfile: str, name: str):
        super().__init__(xmltree, xmlfile)
        self.name = name

    def __repr__(self):
        return f"Playlist({self.name})"

    @property
    def entries(self):
        return [
            PlaylistEntry(entry, self.xmlfile)
            for entry in self.xmltree.findall("PLAYLIST/ENTRY")
        ]


@dataclass(init=False)
class PlaylistEntry(XMLdataclass):
    filename: str = field(metadata={"xpath": "PRIMARYKEY/@KEY"})


@dataclass(init=False)
class HistoryEntry(XMLdataclass):
    deck: int = field(metadata={"xpath": "EXTENDEDDATA/@DECK"})
    duration: float = field(metadata={"xpath": "EXTENDEDDATA/@DURATION"})
    filename: str = field(metadata={"xpath": "PRIMARYKEY/@KEY"})
    played_public: bool = field(metadata={"xpath": "EXTENDEDDATA/@PLAYEDPUBLIC"})
    startdate: int = field(metadata={"xpath": "EXTENDEDDATA/@STARTDATE"})
    starttime: int = field(metadata={"xpath": "EXTENDEDDATA/@STARTTIME"})

    @property
    def startdatetime(self) -> datetime.datetime:
        year = self.startdate >> 16
        month = self.startdate >> 8 & 0xFF
        day = self.startdate & 0xFF
        hour = int(self.starttime / 3600)
        minute = int(self.starttime / 60) % 60
        second = self.starttime % 60
        return datetime.datetime(
            year=year, month=month, day=day, hour=hour, minute=minute, second=second
        )


@dataclass(init=False)
class CollectionEntry(XMLdataclass):
    artist: str = field(metadata={"xpath": "@ARTIST"})
    album: str = field(metadata={"xpath": "ALBUM/@TITLE"})
    label: str = field(metadata={"xpath": "INFO/@LABEL"})
    audio_id: str = field(metadata={"xpath": "@AUDIO_ID"}, repr=False)
    bitrate: int = field(metadata={"xpath": "INFO/@BITRATE"})
    bpm: float = field(metadata={"xpath": "TEMPO/@BPM"})
    key: str = field(metadata={"xpath": "INFO/@KEY"})
    comment: str = field(metadata={"xpath": "INFO/@COMMENT"})
    comment2: str = field(metadata={"xpath": "INFO/@RATING"})
    dir: str = field(metadata={"xpath": "LOCATION/@DIR"})
    file: str = field(metadata={"xpath": "LOCATION/@FILE"})
    filesize: str = field(metadata={"xpath": "INFO/@FILESIZE"})
    genre: str = field(metadata={"xpath": "INFO/@GENRE"})
    playcount: int = field(metadata={"xpath": "INFO/@PLAYCOUNT"})
    playtime: int = field(metadata={"xpath": "INFO/@PLAYTIME"})
    ranking: int = field(metadata={"xpath": "INFO/@RANKING"})
    title: str = field(metadata={"xpath": "@TITLE"})
    import_date: str = field(metadata={"xpath": "INFO/@IMPORT_DATE"})
    release_date: str = field(metadata={"xpath": "INFO@RELEASE_DATE"})
    last_played: str = field(metadata={"xpath": "INFO/@LAST_PLAYED"})
    volume: str = field(metadata={"xpath": "LOCATION/@VOLUME"})

    @property
    def cuepoints(self):
        return [
            CuePoint(cuepoint, self.xmlfile)
            for cuepoint in self.xmltree.findall("CUE_V2")
        ]


@dataclass(init=False)
class CuePoint(XMLdataclass):
    name: str = field(metadata={"xpath": "@NAME"})
    cuepoint_type: int = field(metadata={"xpath": "@TYPE"})
    start: float = field(metadata={"xpath": "@START"})
    length: float = field(metadata={"xpath": "@LEN"})
    repeats: int = field(metadata={"xpath": "@REPEATS"})
    hotcue: int = field(metadata={"xpath": "@HOTCUE"})


class TraktorCollection:
    def __init__(self, path: str):
        self.path = path
        self.xml_tree = etree.parse(self.path)

        self.entries = [
            CollectionEntry(entry, path) for entry in self.xml_tree.findall(ENTRY_XPATH)
        ]
        self.playlists = self._get_playlists()
        self.history = [
            HistoryEntry(entry, path) for entry in self.xml_tree.findall(HISTORY_XPATH)
        ]

    def _get_playlists(self, parent=None, prefix=None):
        # import pdb; pdb.set_trace()
        playlists = []
        if parent is None:
            parent = self.xml_tree.find(PLAYLIST_ROOT_XPATH)
            if parent is None:
                return playlists
        if prefix is None:
            prefix = parent.xpath("@NAME")[0]
            if prefix == "$ROOT":
                prefix = None
        else:
            prefix = "/".join((prefix, parent.xpath("@NAME")[0]))
        for playlist in parent.findall(PLAYLIST_XPATH):
            name_parts = []
            if prefix is not None:
                name_parts.append(prefix)
            name_parts.append(playlist.xpath("@NAME")[0])
            playlists.append(Playlist(playlist, self.path, "/".join(name_parts)))
        for folder in parent.findall(FOLDER_XPATH):
            playlists.extend(self._get_playlists(folder, prefix))
        return playlists
