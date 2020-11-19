import pandas as pd
import numpy as np



def getDescriptors(path):
    """
    Read in CSV to pandas Data Frame Object.
    """
    descriptors = pd.read_csv(path, header = 0, index_col = 0)
    # descriptors.fillna(0,inplace=True) substituting NA values for 0
    # descriptors = descriptors.apply(lambda x: x.fillna(x.mean()),axis=0) # substituting NA values for columnwise means
    return descriptors



def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)



def check_dataset(df):
    return



if __name__ == '__main__':
    bag3drugsdescriptors = getDescriptors("C:\\Users\\Tamara\\Desktop\\bag3myopathy\\descriptors\\bag3drugsdescriptors.csv")
    print(bag3drugsdescriptors.shape)
    print(clean_dataset(bag3drugsdescriptors).head(10))