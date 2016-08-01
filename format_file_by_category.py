# coding=utf8

import sys

file_name = sys.argv[1]
with open(file_name) as inputData:
    firstLine=None
    baseName="good_picture.csv"
    outputData=None
    for line in inputData:
        lineArr = line.split("\t")
        if lineArr[1] != firstLine:
            if outputData is not None:
                outputData.close()
            outfileName = lineArr[1] + "_" +  baseName
            outputData = open(outfileName,'w')
            firstLine = lineArr[1]
        outputData.write(",".join(lineArr))
    if outputData is not None:
        outputData.close()

