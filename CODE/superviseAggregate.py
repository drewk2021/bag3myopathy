import pandas as pd
from retrieveDescriptors import getDescriptors, clean_dataset

def superviseLabel(df, label, title = "class"):
    # FOR ASCRIBING label CLASS TO EVERY INSTANCE IN df UNDER title ATTRIBUTE

    df[title] = [label for i in range(df.shape[0])]
    return df


if __name__ == '__main__':
    drugs = getDescriptors("C:\\Users\\Tamara\\Desktop\\bag3myopathy\\descriptors\\bag3drugsdescriptors.csv")
    drugs = superviseLabel(drugs, 1)

    controls = getDescriptors("C:\\Users\\Tamara\\Desktop\\bag3myopathy\\descriptors\\180randomcontrolsdescriptors.csv")
    controls = superviseLabel(controls, 0)

    comb = pd.concat([drugs,controls])
    comb.to_csv("C:\\Users\\Tamara\\Desktop\\bag3myopathy\\descriptors\\pdbag3withclass.csv", index = True)
