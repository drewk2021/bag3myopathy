import pandas as pd
from retrieveDescriptors import getDescriptors
from superviseAggregate import superviseLabel

def meshData(basisAttributes, unfilteredData):
    df = unfilteredData
    df = df.filter(basisAttributes, axis = 1) # column-wise filtering off model attributes
    return df





if __name__ == "__main__":
    modelData = open("C:\\Users\\Tamara\\Desktop\\bag3myopathy\\arffs\\pdbag3drugsstandard250.arff","r")
    modelLines = modelData.readlines()
    modelData.close()
    
    modelAttributes = []
    for line in modelLines:
        if "@attribute" in line:
            modelAttributes.append(line.split(" ")[1])


    dbDrugs = getDescriptors("C:\\Users\\Tamara\\Desktop\\bag3myopathy\\descriptors\\drugbankdescriptors.csv")
    dbDrugs = superviseLabel(dbDrugs, "?")

    filteredTest = meshData(modelAttributes,dbDrugs)
    filteredTest.to_csv("C:\\Users\\Tamara\\Desktop\\bag3myopathy\\descriptors\\drugbankwithclass.csv", index = True)