# coding=utf8

import sys

file_name = sys.argv[1]
base_name = sys.argv[2]
index = int(sys.argv[3])
sep = sys.argv[4]
print sep
with open(file_name) as inputData:
    firstLine = None
    outputData = None
    for line in inputData:
        lineArr = line.split(sep)
        if lineArr[index] != firstLine:
            if outputData is not None:
                outputData.close()
            outfileName = lineArr[index] + "_" + base_name
            outputData = open(outfileName,'w')
            firstLine = lineArr[index]
        outputData.write(",".join(lineArr))
    if outputData is not None:
        outputData.close()

