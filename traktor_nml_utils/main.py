import datetime
import os
from dataclasses import dataclass, field

from lxml import etree
from lxml.etree import tostring

dir_path = os.path.dirname(os.path.realpath(__file__))

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


class XMLdataclass:
    def __init__(self, xmltree, xmlfile):
        self.xmltree = xmltree
        self.xmlfile = xmlfile

    def __getattribute__(self, attribute):
        if attribute.startswith('__') or attribute not in self.__dataclass_fields__.keys():
            return super().__getattribute__(attribute)

        dc_field = self.__dataclass_fields__[attribute]
        field_type = dc_field.type
        xpath = dc_field.metadata['xpath']
        result = self.xmltree.xpath(xpath)
        if result:
            return field_type(result[0])

    def __setattr__(self, attribute, value):
        if attribute.startswith('__') or attribute not in self.__dataclass_fields__.keys():
            return super().__setattr__(attribute, value)

        dc_field = self.__dataclass_fields__[attribute]
        xpath = dc_field.metadata['xpath']
        xpath_attrib = xpath.split('/')[-1]
        root = self.xmltree

        # Need to handle 'PATH/PATH/@ATTRIB' or '@ATTRIB'
        if not xpath.startswith('@'):
            xpath_path = '/'.join(xpath.split('/')[:-1])
            root = self.xmltree.find(xpath_path)

        xpath_attrib = xpath_attrib.lstrip('@')
        root.set(xpath_attrib, str(value))

    def save(self):
        with open(self.xmlfile, 'wb') as f:
            f.write(tostring(self.xmltree.getroottree(), encoding='utf8'))


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
class CollectionEntry(XMLdataclass):
    artist: str = field(metadata={'xpath': '@ARTIST'})
    audio_id: str = field(metadata={'xpath': '@AUDIO_ID'}, repr=False)
    bitrate: int = field(metadata={'xpath': 'INFO/@BITRATE'})
    bpm: float = field(metadata={'xpath': 'TEMPO/@BPM'})
    comment: str = field(metadata={'xpath': 'INFO/@COMMENT'})
    comment2: str = field(metadata={'xpath': 'INFO/@RATING'})
    dir: str = field(metadata={'xpath': 'LOCATION/@DIR'})
    file: str = field(metadata={'xpath': 'LOCATION/@FILE'})
    genre: str = field(metadata={'xpath': 'INFO/@GENRE'})
    playcount: int = field(metadata={'xpath': 'INFO/@PLAYCOUNT'})
    playtime: int = field(metadata={'xpath': 'INFO/@PLAYTIME'})
    ranking: int = field(metadata={'xpath': 'INFO/@RANKING'})
    title: str = field(metadata={'xpath': '@TITLE'})
    import_date: str = field(metadata={'xpath': 'INFO/@IMPORT_DATE'})
    last_played: str = field(metadata={'xpath': 'INFO/@LAST_PLAYED'})
    volume: str = field(metadata={'xpath': 'LOCATION/@VOLUME'})

    @property
    def cuepoints(self):
        return [CuePoint(cuepoint, self.xmlfile) for cuepoint in self.xmltree.findall('CUE_V2')]


@dataclass(init=False)
class CuePoint(XMLdataclass):
    name: str = field(metadata={'xpath': '@NAME'})
    cuepoint_type: int = field(metadata={'xpath': '@TYPE'})
    start: float = field(metadata={'xpath': '@START'})
    length: float = field(metadata={'xpath': '@LEN'})
    repeats: int = field(metadata={'xpath': '@REPEATS'})
    hotcue: int = field(metadata={'xpath': '@HOTCUE'})


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
