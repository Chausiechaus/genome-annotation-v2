import gffutils
fn = gffutils.example_filename('intro_docs_example.gff')
print(open(fn).read())

db = gffutils.create_db(fn, dbfn='test.db', force=True, keep_order=True, 
merge_strategy='merge', sort_attribute_values=True)

gene = db['FBgn0031208']

def get_annotations(db, begin, stop):
    ##Returns a list of all annotations within a given range
    ##Chromosome listing not accounted for yet
    annotation_lst = []
    for gene in db.all_features():
        if ((gene.start >= begin) and (gene.end <= stop)):
            annotation_lst.append(gene.id)
    return annotation_lst

print('\n====================BUFFER========================\n')
print(gene.start)
print(gene.end)
print(gene.id)

print('\nAttempt to obtain the ids of all annotations between start 8000 and stop 9000:\n')
print(get_annotations(db, 8000, 9000))

print('\n\nTesting built in system:')
rg = list(db.region(region=('2L', 9277, 10000), completely_within=True))
print(rg[0])
