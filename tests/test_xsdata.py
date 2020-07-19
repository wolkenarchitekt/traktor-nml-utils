from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from traktor_nml_utils.models.collection import *
parser = XmlParser()
XML = """<NML VERSION="19">
  <HEAD COMPANY="www.native-instruments.com" PROGRAM="Traktor"/>
  <MUSICFOLDERS/>
  <PLAYLISTS>
    <NODE TYPE="FOLDER" NAME="$ROOT">
      <SUBNODES COUNT="1">
        <NODE TYPE="PLAYLIST" NAME="Preparation">
          <PLAYLIST ENTRIES="212" TYPE="LIST" UUID="f80b2bdebbb843eb897c1ae90af896f5">
            <ENTRY>
              <PRIMARYKEY TYPE="TRACK" KEY="osx/:Users/:johndoe/:Music/:pechundschwefel/:549043_The_Sky_Was_Pink_Icelandic_Version.mp3"/>
            </ENTRY>
          </PLAYLIST>
        </NODE>
      </SUBNODES>
    </NODE>
  </PLAYLISTS>
</NML>
"""


def test_xsdata():
    obj = parser.from_string(XML, Nml)
    assert obj.playlists.node.subnodes.node[0].playlist.entry[0].primarykey.key == "osx/:Users/:johndoe/:Music/:pechundschwefel/:549043_The_Sky_Was_Pink_Icelandic_Version.mp3"
    obj.playlists.node.subnodes.node[0].playlist.entry[0].primarykey.key = "foobar"
    print(XmlSerializer(pretty_print=True).render(obj))
