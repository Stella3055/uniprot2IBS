class uniprot2IBS(object):
    def __init__(self, pathToUniprotXml):
        import configparser
        self.inPath = pathToUniprotXml

        self.xmlParse()
        return

    def xmlParse(self):
        import xml.etree.ElementTree as et
        from collections import OrderedDict
        parser = et.parse(self.inPath)
        root = parser.getroot()

        featureList = []
        for features in root.iter(tag="{http://uniprot.org/uniprot}feature"):
            featureList.append([features.get("type"), features.get("description")])
        print(featureList)
        for i in featureList:
            print(lambda i:"\t".join(i))
        print("\n".join(map(lambda x:"\t".join(x), featureList)))
            # if features.get("type") == "region of interest":
            #     for subfeatures in features.iter(tag="{http://uniprot.org/uniprot}location"):
            #         print(subfeatures.find("begin").get("position"))
                # loc = features.find("location")
                # print(loc.find("begin"))

if __name__ == "__main__":
    pathToUniprotXml = "./ESR1.xml"
    uniprot2IBS_test = uniprot2IBS(pathToUniprotXml)