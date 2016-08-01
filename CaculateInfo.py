# coding=utf8

import re
import sys


def caculateRatio(fileClick, fileView, outFile):
    with open(fileClick) as clickInput:
        with open(fileView) as viewInput:
           outputFile = open(outFile, "w")
           allLinesClick = clickInput.readlines()
           allLinesView = viewInput.readlines()
           for i in range(len(allLinesClick)):
               clickLine = allLinesClick[i]
               viewLine = allLinesView[i]
               clickLineArr = re.split(re.compile("\s+"), clickLine)
               viewLineArr  = re.split(re.compile("\s+"), viewLine)
               print("viewText is: %s "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 %viewLineArr[0])
               ratio = int(clickLineArr[0])/float(viewLineArr[0])
               lineToBeWrite = clickLineArr[0] + "\t" + viewLineArr[0] + "\t" + str(ratio) + "\t" + "\t".join(clickLineArr[1:])
               outputFile.write(lineToBeWrite + "\n")

           outputFile.close()


if __name__ == '__main__':
    fileName1 = sys.argv[1]
    fileName2 = sys.argv[2]
    outputFile = sys.argv[3]

    caculateRatio(fileName1, fileName2, outputFile)
