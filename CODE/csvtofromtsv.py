def csv2tsv(basepath, endpath = None):

    if not endpath:
        endpath = basepath.replace(".csv",".tsv")

    
    csv = open(basepath, "r")
    csvLines = csv.readlines()
    csv.close()


    tsv = open(endpath, "w")
    tsv.writelines([line.replace(",","\t") for line in csvLines])
    tsv.close()
    

    return endpath



def tsv2csv(basepath, endpath = None):

    if not endpath:
        endpath = basepath.replace(".tsv",".csv")

    
    tsv = open(basepath, "r")
    tsvLines = tsv.readlines()
    tsv.close()


    csv = open(endpath, "w")
    csv.writelines([line.replace("\t",",") for line in tsvLines])
    csv.close()
    

    return endpath