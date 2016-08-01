# coding=utf8

import sys

file_name = sys.argv[1]
with open(file_name) as inputData:
    firstLine=None
    baseName="result.csv"
    outputData=None
    for line in inputData:
        lineArr = line.split("\t")
        if(lineArr[0] != firstLine):
            if outputData is not None:
                outputData.close()
            outfileName = lineArr[0] + "_" +  baseName
            outputData = open(outfileName,'w')
            firstLine = lineArr[0]
        outputData.write(",".join([lineArr[0], lineArr[-1]]))
    if outputData is not None:
        outputData.close()

