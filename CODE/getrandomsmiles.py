from random import shuffle

def getRandom(basepath, endpath, num):
    """
    Parameters: imported tsv path (str), exported tsv path (str), number
    of random molecules (int).
    """

    old = open(basepath, "r")
    oldlines = old.readlines()
    shuffle(oldlines)
    old.close()

    
    new = open(endpath, "w")
    new.writelines(oldlines[:num])
    new.close()
    return


if __name__ == '__main__':
    getRandom("C:\\Users\\Tamara\\Desktop\\bag3myopathy\\zincinman - smilesid.tsv","C:\\Users\\Tamara\\Desktop\\bag3myopathy\\zincinman180random.tsv",180)
