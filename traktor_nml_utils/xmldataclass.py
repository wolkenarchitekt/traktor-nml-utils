from lxml.etree import tostring


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
