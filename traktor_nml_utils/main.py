from dataclasses import dataclass, field
import xmltodict
from lxml import etree
from datetime import datetime

@dataclass
class TraktorCollectionEntry:
    """
    <ENTRY MODIFIED_DATE="2019/10/19" MODIFIED_TIME="13047" LOCK="1" LOCK_MODIFICATION_TIME="2019-08-23T21:27:21" AUDIO_ID="AMARERERERERERERERERERERERA92ktc3N20taZ9y0ta3NzEtpcsz97e3e3Vvtqt393d/v3Wnsmd////////////////////////zarYzdzarYp6uqnYqN3arayL3vzp/qzPv7/5zf393qlsVYu1NWZUI2RWZUI1lYh3KGmrm82Sr/////////////////3+///73/////////r////////+/v7+///v/4f//f/5b//////Xx7qbj////////////////////////////+zf////u////////////qiHxoWqiXxoWIyJiJm6eXyKd6VypnNaVyp3QREREREREREREA==" TITLE="Dubstep 1" ARTIST="Loopmasters">
      <LOCATION DIR="/:Library/:Application Support/:Native Instruments/:Traktor 2/:Factory Sounds/:" FILE="Loopmasters_Dubstep1.mp3" VOLUME="osx" VOLUMEID="osx"/>
      <MODIFICATION_INFO AUTHOR_TYPE="user"/>
      <INFO BITRATE="189720" GENRE="Dubstep" COMMENT="Tracks by www.loopmasters.com" COVERARTID="113/R1PI3ZDLWQMLAAASJ4B2AQZXI1ZD" KEY="10m" PLAYTIME="193" PLAYTIME_FLOAT="192.078369" IMPORT_DATE="2010/8/16" RELEASE_DATE="2010/1/1" FLAGS="28" FILESIZE="5040"/>
      <TEMPO BPM="139.999924" BPM_QUALITY="100.000000"/>
      <LOUDNESS PEAK_DB="-2.782080" PERCEIVED_DB="0.000000" ANALYZED_DB="-2.000000"/>
      <MUSICAL_KEY VALUE="12"/>
      <CUE_V2 NAME="AutoGrid" DISPL_ORDER="0" TYPE="4" START="52.315876" LEN="0.000000" REPEATS="-1" HOTCUE="0"/>
      <CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="0" START="52.315876" LEN="0.000000" REPEATS="-1" HOTCUE="7"/>
      <CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="0" START="52.315876" LEN="0.000000" REPEATS="-1" HOTCUE="6"/>
    </ENTRY>
    """
    artist: str
    title: str
    xml_dict: 'TraktorCollection' = field(repr=False)


@dataclass
class TraktorPlaylistEntry:
    """
    <ENTRY>
      <PRIMARYKEY TYPE="TRACK" KEY="Transcend/:DJing/:beatport_steve/:09 Change (Like Mix Extended Instrumental).mp3"/>
      <EXTENDEDDATA DECK="1" DURATION="241.700394" EXTENDEDTYPE="HistoryData" PLAYEDPUBLIC="1" STARTDATE="132319762" STARTTIME="68839"/>
    </ENTRY>
    """

    """
    Date trans:
    2017-12-31: 132189215
    2018-01-01: 132251905 +62690
    2018-12-31: 132254751
    2019-01-01: 132317441 +62690
    2019-01-02: 132317442
    2019-01-03: 132317443
    2019-01-31: 132317471
    2019-02-01: 132317697 +226
    2019-02-28: 132317724 +27
    2019-03-01: 132317953 +229
    2019-03-31: 132317983 +30
    2019-04-01: 132318209 +226
    2019-04-30: 132318238
    2019-05-01: 132318465 +227
    2019-05-31: 132318495
    2019-06-01: 132318721 +226
    
    https://github.com/drumsoft/TraktorLogDecode/blob/master/traktor-log-decode.pl
    sprintf "%04d-%02d-%02d", 
		$trday>>16, ($trday>>8 & 0xff), ($trday & 0xff);
    """
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
        if not self._playlist_entries:
            # /PLAYLISTS/NODE[@TYPE='FOLDER']/SUBNODES/NODE[@TYPE='PLAYLIST'][@NAME='Auto-Cued Tracks']/PLAYLIST/ENTRY
            for entry in self.xml_tree.findall(
                    "/PLAYLISTS/NODE[@TYPE='FOLDER']/SUBNODES/NODE[@TYPE='PLAYLIST'][@NAME='HISTORY']/PLAYLIST/ENTRY"):
                duration = float(entry.xpath('EXTENDEDDATA/@DURATION')[0])
                filename = entry.xpath('PRIMARYKEY/@KEY')[0]

                startdate = entry.xpath('EXTENDEDDATA/@STARTDATE')[0]
                startdate = int(startdate)
                starttime = entry.xpath('EXTENDEDDATA/@STARTTIME')[0]
                starttime = int(starttime)
                # sprintf "%02d:%02d:%02d", int($s / 3600), int($s / 60) % 60, ($s % 60);

                year = startdate >> 16
                month = startdate >> 8 & 0xff
                day = startdate & 0xff
                hour = int(starttime / 3600)
                minute = int(starttime / 60) % 60
                second = starttime % 60
                startdate = datetime(year=year, month=month, day=day,
                                     hour=hour, minute=minute, second=second)

                playlist_entry = TraktorPlaylistEntry(
                    duration=duration, filename=filename, startdatetime=startdate)
                self._playlist_entries.append(playlist_entry)

                print(playlist_entry.filename, playlist_entry.startdatetime.isoformat())

                # from ipdb import set_trace
                # set_trace()
                # pass
            # self._playlist_entries = self.xml_tree.findall(
            #     "/PLAYLISTS/NODE[@TYPE='FOLDER']/SUBNODES/NODE[@TYPE='PLAYLIST'][@NAME='HISTORY']/PLAYLIST/ENTRY")
            # from ipdb import set_trace
            # set_trace()

        return self._playlist_entries

