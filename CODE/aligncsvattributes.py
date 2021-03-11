trainPath = "250sirt2trainingligandspadelwithclass - sirt2trainingligandspadel.csv.arff.csv"

otherPadelPath = "fullzincinmanligandspadelunknownclasspart1.csv"

testPath = "250zincinmanligandsmeshedtestpadelpart1.csv"



trainFile = open(trainPath,"r")

trainAttributes = trainFile.readlines()[0].split(",")
trainFile.close()



otherPadelFile = open(otherPadelPath,"r")


otherPadelLines = otherPadelFile.readlines()
otherPadelFile.close()
otherPadelColumns = []

testLines = []

for attribute in trainAttributes:
    if attribute in otherPadelLines[0].split(","):
        otherPadelColumns += [otherPadelLines[0].split(",").index(attribute)]

count = 0
for line in otherPadelLines:
    rearrangedLine = []
    for inDex in otherPadelColumns:
        rearrangedLine += [line.split(",")[inDex]]
    testLines += [",".join(rearrangedLine)]




testFile = open(testPath,"w")
testFile.writelines(testLines)
testFile.close()
