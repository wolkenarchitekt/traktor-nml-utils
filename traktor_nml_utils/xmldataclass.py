from dataclasses import dataclass
from typing import List

from lxml.etree import tostring, Element


# TODO: check alternative implementation: https://github.com/theatlantic/django-xml/blob/master/djxml/xmlmodels/base.py

@dataclass
class XMLdataclass:
    xmlfile: str = ""
    xmltree: str = ""

    def from_xml(self, xmlfile, xmltree):
        pass

    def to_xml(self, xmlfile, xmltree):
        for field in self.__dataclass_fields__.keys():
            print(field)

    """Use dataclass fields to wrap XML elements with getters and setters"""
    def __getattribute__(self, attribute):
        """Retrieve XML via dataclass field metadata attribute"""
        if attribute.startswith('__') \
                or attribute not in self.__dataclass_fields__.keys():
            return super().__getattribute__(attribute)

        dc_field = self.__dataclass_fields__[attribute]
        field_type = dc_field.type

        if 'xpath' not in dc_field.metadata:
            return super().__getattribute__(attribute)

        xpath = dc_field.metadata['xpath']

        # Bare instance
        if not self.xmltree:
            return None

        # Extract typing information for list types
        if getattr(field_type, "__origin__", None) == list:
            result = self.xmltree.findall(xpath)
            class_type = field_type.__args__[0]
            return [class_type(element, self.xmlfile) for element in result]

        result = self.xmltree.xpath(xpath)
        if result:
            return field_type(result[0])

    def __setattr__(self, attribute, value):
        """Set XML via dataclass field metadata attribute"""
        if attribute.startswith('__') \
                or attribute not in self.__dataclass_fields__.keys()\
                or not getattr(self, 'xmltree', None):
            return super().__setattr__(attribute, value)

        dc_field = self.__dataclass_fields__[attribute]
        field_type = dc_field.type

        if 'xpath' not in dc_field.metadata:
            return super().__setattr__(attribute, value)
        xpath = dc_field.metadata['xpath']
        xpath_attrib = xpath.split('/')[-1]
        root = self.xmltree

        # Need to handle 'PATH/PATH/@ATTRIB' or '@ATTRIB'
        if not xpath.startswith('@'):
            xpath_path = '/'.join(xpath.split('/')[:-1])
            root = self.xmltree.find(xpath_path)

        xpath_attrib = xpath_attrib.lstrip('@')

        if field_type == list:
            return self.xmltree.findall(xpath)

        root.set(xpath_attrib, str(value))

    def save(self):
        with open(self.xmlfile, 'wb') as f:
            f.write(tostring(self.xmltree.getroottree(), encoding='utf8'))
