import datetime
import os
from dataclasses import dataclass, field
from typing import List
from lxml import etree
from traktor_nml_utils.xmldataclass import XMLdataclass
dir_path = os.path.dirname(os.path.realpath(__file__))
from lxml.etree import ElementTree


PLAYLIST_XPATH = "/PLAYLISTS/NODE[@TYPE='FOLDER']/SUBNODES/NODE[@TYPE='PLAYLIST']"
ENTRY_XPATH = "/COLLECTION/ENTRY"

PLAYLIST_ENTRY_XPATH = (
    "/PLAYLISTS/NODE[@TYPE='FOLDER']"
    "/SUBNODES/NODE[@TYPE='PLAYLIST'][not(@NAME='HISTORY')]"
    "/PLAYLIST/ENTRY"
)

HISTORY_XPATH = (
    "/PLAYLISTS/NODE[@TYPE='FOLDER']"
    "/SUBNODES/NODE[@TYPE='PLAYLIST'][@NAME='HISTORY']"
    "/PLAYLIST/ENTRY"
)


@dataclass(init=False)
class Playlist(XMLdataclass):
    name: str = field(metadata={'xpath': '@NAME'})

    @property
    def entries(self):
        return [PlaylistEntry(entry, self.xmlfile)
                for entry in self.xmltree.findall('PLAYLIST/ENTRY')]


@dataclass(init=False)
class PlaylistEntry(XMLdataclass):
    filename: str = field(metadata={'xpath': 'PRIMARYKEY/@KEY'})


@dataclass(init=False)
class HistoryEntry(XMLdataclass):
    deck: int = field(metadata={'xpath': 'EXTENDEDDATA/@DECK'})
    duration: float = field(metadata={'xpath': 'EXTENDEDDATA/@DURATION'})
    filename: str = field(metadata={'xpath': 'PRIMARYKEY/@KEY'})
    played_public: bool = field(metadata={'xpath': 'EXTENDEDDATA/@PLAYEDPUBLIC'})
    startdate: int = field(metadata={'xpath': 'EXTENDEDDATA/@STARTDATE'})
    starttime: int = field(metadata={'xpath': 'EXTENDEDDATA/@STARTTIME'})

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
class CuePoint(XMLdataclass):
    name: str = field(metadata={'xpath': '@NAME'})
    cuepoint_type: int = field(metadata={'xpath': '@TYPE'})
    start: float = field(metadata={'xpath': '@START'})
    length: float = field(metadata={'xpath': '@LEN'})
    repeats: int = field(metadata={'xpath': '@REPEATS'})
    hotcue: int = field(metadata={'xpath': '@HOTCUE'})


@dataclass(init=False)
class CollectionEntry(XMLdataclass):
    artist: str = field(metadata={'xpath': '@ARTIST'})
    album: str = field(metadata={'xpath': 'ALBUM/@TITLE'})
    label: str = field(metadata={'xpath': 'INFO/@LABEL'})
    audio_id: str = field(metadata={'xpath': '@AUDIO_ID'}, repr=False)
    bitrate: int = field(metadata={'xpath': 'INFO/@BITRATE'})
    bpm: float = field(metadata={'xpath': 'TEMPO/@BPM'})
    key: str = field(metadata={'xpath': 'INFO/@KEY'})
    comment: str = field(metadata={'xpath': 'INFO/@COMMENT'})
    comment2: str = field(metadata={'xpath': 'INFO/@RATING'})
    dir: str = field(metadata={'xpath': 'LOCATION/@DIR'})
    file: str = field(metadata={'xpath': 'LOCATION/@FILE'})
    filesize: str = field(metadata={'xpath': 'INFO/@FILESIZE'})
    genre: str = field(metadata={'xpath': 'INFO/@GENRE'})
    playcount: int = field(metadata={'xpath': 'INFO/@PLAYCOUNT'})
    playtime: int = field(metadata={'xpath': 'INFO/@PLAYTIME'})
    ranking: int = field(metadata={'xpath': 'INFO/@RANKING'})
    title: str = field(metadata={'xpath': '@TITLE'})
    import_date: str = field(metadata={'xpath': 'INFO/@IMPORT_DATE'})
    release_date: str = field(metadata={'xpath': 'INFO/@RELEASE_DATE'})
    last_played: str = field(metadata={'xpath': 'INFO/@LAST_PLAYED'})
    volume: str = field(metadata={'xpath': 'LOCATION/@VOLUME'})
    cuepoints: List[CuePoint] = field(metadata={'xpath': "CUE_V2"}, default_factory=list)


class TraktorCollection:
    def __init__(self, path: str):
        self.path = path
        self.xml_tree = etree.parse(self.path)

        self.entries = [
            CollectionEntry(entry, path) for entry in self.xml_tree.findall(ENTRY_XPATH)]
        self.playlists = [
            Playlist(entry, path) for entry in self.xml_tree.findall(PLAYLIST_XPATH)]
        self.history = [
            HistoryEntry(entry, path) for entry in self.xml_tree.findall(HISTORY_XPATH)]
