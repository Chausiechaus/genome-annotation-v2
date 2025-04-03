import gffutils
db = gffutils.FeatureDB('test2.db', keep_order=True)



slct = db.region(region=('chr1', 207317678, 207325678), completely_within=True)
slct_lst =[]
##about 43 seconds to iterate through all of chromosome 1
for item in slct:
    print(item)
    slct_lst.append(item)


redo = 0
while (redo < 0):
    slct = db.region(region=('chr1', redo, redo + 100000), completely_within=True)
    for item in slct:
          print(item) 
    redo += 100000
##49 seconds for 2488 iterations
##look into pandas dataframe/dictionary
##look into str attribute of feature object for listing
##dir command dir(object)

##source activate myenv
##python -m ipykernel install --user --name myenv --display-name "Python (myenv)"

##CD55 30bp region of interest: hg38_cd55 = 'chr1:207320867-207320897'
##hg38 cd55 gene = 'chr1:207,321,678-207,360,966 39,289 bp.' [from UCSC]
##TSS:     chr1:207,321,678 [from IGV as well]
##TSS +/- 4 KB  chr1:207317678-207325678
