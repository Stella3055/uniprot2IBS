import jinja2
import pandas as pd
import xml.etree.ElementTree as et
from collections import OrderedDict
import sys


class uniprot2Info(object):
    def __init__(self, pathToUniprotXml):
        self.inPath = pathToUniprotXml
        self.xmlParse()
        return

    def xmlParse(self):
        parser = et.parse(self.inPath)
        root = parser.getroot()
        featureList = []
        for features in root.iter(tag="{http://uniprot.org/uniprot}feature"):
            posStart = "NA"
            posEnd = "NA"
            posLoci = "NA"
            for childElem in features.getchildren():
                if childElem.tag == "{http://uniprot.org/uniprot}location":
                    for subChildElem in childElem.getchildren():
                        # print(subChildElem.tag)
                        if subChildElem.tag == "{http://uniprot.org/uniprot}begin":
                            posStart = subChildElem.get("position")
                        if subChildElem.tag == "{http://uniprot.org/uniprot}end":
                            posEnd = subChildElem.get("position")
                        if subChildElem.tag == "{http://uniprot.org/uniprot}position":
                            posLoci = subChildElem.get("position")
            featureList.append([
                features.get("type"),
                features.get("description", default="NA"),
                posStart,
                posEnd,
                posLoci
            ])
        header = "\t".join([
            "feature_name",
            "description",
            "Start_Position",
            "End_Position",
            "Loci_Position"
        ])
        # print(header)
        # for feature in featureList:
        #     print("\t".join(feature))

        with open(self.inPath+".info.tsv", "w") as output:
            output.write(header+"\n")
            for feature in featureList:
                output.write("\t".join(feature)+"\n")
        return


class info2IbsProj(object):
    def __init__(self, pathToInfo):
        self.pathToInfo = pathToInfo
        self.importInfo()
        self.importTemplates()
        self.writeIbsXml()
        return

    def importInfo(self):
        self.df = pd.read_table(self.pathToInfo)
        return

    def importTemplates(self):
        with open("./templates/chain.xml", "r") as chainTemplate:
            self.chainTemplate = chainTemplate.read()
        with open("./templates/domain.xml", "r") as domainTemplate:
            self.domainTemplate = domainTemplate.read()
        with open("./templates/site.xml", "r") as siteTemplate:
            self.siteTemplate = siteTemplate.read()
        return

    def renderDomain(self, domainRow):
        domain = {}
        domain["id"] = "Domain"+str(domainRow.name)
        domain["name"] = domainRow.description
        domain["start"] = int(domainRow.Start_Position)
        domain["end"] = int(domainRow.End_Position)
        return jinja2.Template(self.domainTemplate).render(domain=domain)

    def renderSite(self, siteRow):
        site = {}
        site["id"] = "Site"+str(siteRow.name)
        site["name"] = str(int(siteRow.Loci_Position))
        site["pos"] = int(siteRow.Loci_Position)
        return jinja2.Template(self.siteTemplate).render(site=site)

    def renderXml(self):
        chain = {}
        chainSeries = self.df[self.df.feature_name == "chain"]
        # print(chainSeries.description[0])

        chain["name"] = chainSeries.description[0]
        chain["start"] = int(chainSeries.Start_Position[0])
        chain["end"] = int(chainSeries.End_Position[0])
        chain["components"] = []

        compDf = self.df[self.df.feature_name != "chain"]
        for _, row in compDf.iterrows():
            if pd.isnull(row.Loci_Position):
                chain["components"].append(self.renderDomain(row))
            else:
                chain["components"].append(self.renderSite(row))

        # print(chain)
        print(jinja2.Template(self.chainTemplate).render(chain=chain))
        return jinja2.Template(self.chainTemplate).render(chain=chain)

    def writeIbsXml(self):
        with open(self.pathToInfo+".ibs.xml", "w") as output:
            output.write(self.renderXml())
        return


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(
            "Useage:\t\tuniprot2IBS [command] [filename]\nCommands:\n- parse:\textract protein metadata into .tsv file\n- construct:\tconstruct IBS project file from .tsv metadata file")
    elif sys.argv[1] == "parse":
        pathToUniprotXml = sys.argv[2]
        uniprot2IBS_instance = uniprot2Info(pathToUniprotXml)
    elif sys.argv[1] == "construct":
        pathToInfo = sys.argv[2]
        info2IbsProj_instance = info2IbsProj(pathToInfo)
    else:
        print("Invalid Command")

