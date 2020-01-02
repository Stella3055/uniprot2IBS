class uniprot2IBS(object):
    def __init__(self, pathToUniprotXml):
        import configparser
        self.inPath = pathToUniprotXml

        self.xmlParse()
        return

    def xmlParse(self):
        try:
            import xml.etree.cElementTree as et
        except ImportError:
            import xml.etree.ElementTree as et
        
        parser = et.parse(self.inPath)
        root = parser.getroot()
        print(root.tag)
        entry=root.iter("entry")
        print(entry.find("accession"))
        attr = root.attrib
        print(attr)

        # for features in entry.iter("acession"):
        #     print(features.text)

if __name__ == "__main__":
    pathToUniprotXml = "./ESR1.xml"
    uniprot2IBS_test = uniprot2IBS(pathToUniprotXml)