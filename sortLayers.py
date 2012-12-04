#! /usr/local/bin/python

"""
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
    help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
    action="store_false", dest="verbose", default=True,
    help="don't print status messages to stdout")

(options, args) = parser.parse_args()

test
"""

import re

class LayerManager(object):
    def __init__(self):
        self.lines = []

    def addLayerLine(self,  line):
        self.lines.append(line)

    def getType(self):
        # loop through layers and grab type
        pass



def main():
    skinFile = open("./skins/cinematic/cinematic.json")
    fiveSpacePattern = re.compile("^\s{9}")
    layerStartPattern = re.compile("\"layers\"")
    layerEndPattern = re.compile("]")
    ignoreLayerLinePattern = re.compile("\{|\}")
    layers = []
    layerStart = False
    for line in skinFile:
        if fiveSpacePattern.search(line):
            if layerStart is True and not ignoreLayerLinePattern.search(line):
                if layerEndPattern.search(line):
                    print "end layer"
                else:
                    print line

            if layerStartPattern.search(line):
                print "start layer"
                layerStart = True

            if layerEndPattern.search(line):
                layerStart = False

if __name__ == "__main__":
    main()