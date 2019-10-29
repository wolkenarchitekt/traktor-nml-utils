from dataclasses import dataclass, field
from datetime import datetime

import xmltodict
from lxml import etree

HISTORY_XPATH = (
    "/PLAYLISTS/NODE[@TYPE='FOLDER']"
    "/SUBNODES/NODE[@TYPE='PLAYLIST'][@NAME='HISTORY']"
    "/PLAYLIST/ENTRY")


def parse_date(startdate: int, starttime: int) -> datetime:
    year = startdate >> 16
    month = startdate >> 8 & 0xff
    day = startdate & 0xff
    hour = int(starttime / 3600)
    minute = int(starttime / 60) % 60
    second = starttime % 60
    return datetime(year=year, month=month, day=day,
                    hour=hour, minute=minute, second=second)


@dataclass
class TraktorCollectionEntry:
    artist: str
    title: str
    xml_dict: 'TraktorCollection' = field(repr=False)


@dataclass
class TraktorPlaylistEntry:
    duration: float
    filename: str
    startdatetime: datetime


class TraktorCollection:
    def __init__(self, path: str):
        self.path = path
        self._entries = []
        self._playlist_entries = []
        self.xml_str = open(self.path).read()
        self.xml_dict = xmltodict.parse(self.xml_str)
        self.xml_tree = etree.parse(self.path)

    def entries(self) -> [TraktorCollectionEntry]:
        if not self._entries:
            xml_data = self.xml_dict['NML']['COLLECTION']['ENTRY']

            for xml_id, xml_data in enumerate(xml_data):
                entry = TraktorCollectionEntry(
                    artist=xml_data.get('@ARTIST', None),
                    title=xml_data.get('@TITLE', None),
                    xml_dict=self.xml_dict,
                )
                self._entries.append(entry)

        return self._entries

    def playlists(self) -> [TraktorPlaylistEntry]:
        playlists = []
        for entry in self.xml_tree.findall(HISTORY_XPATH):
            duration = float(entry.xpath('EXTENDEDDATA/@DURATION')[0])
            filename = entry.xpath('PRIMARYKEY/@KEY')[0]

            startdate = int(entry.xpath('EXTENDEDDATA/@STARTDATE')[0])
            starttime = int(entry.xpath('EXTENDEDDATA/@STARTTIME')[0])
            dt = parse_date(startdate, starttime)

            playlist_entry = TraktorPlaylistEntry(
                duration=duration, filename=filename, startdatetime=dt)
            playlists.append(playlist_entry)
        return playlists
