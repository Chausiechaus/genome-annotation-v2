import pysam
import pandas as pd
import numpy as np

#first download the bed.gz and bed.gz.tbi files and put in the same directory
input_file = 'hg38.all_motifs.v1.0.bed.gz'
tabix = pysam.TabixFile(input_file)

#Create dictionary using the input selection
records = []
for row in tabix.fetch('chr1',207320867,207320897):
    print(row)
    assets = row.split()
    records.append({
        "seqid": assets.pop(0),
        "source": 'K562',
        "start": assets.pop(0),
        "end": assets.pop(0),
        "featuretype": 'promoter',
        "strand": assets.pop(2),
        "attributes": ({"ID": [assets.pop(0)], "matchscore": [assets.pop(0)], "seq":[assets.pop(0)]})  # Attributes as a dictionary (will be expanded later)
    })
print(records)

df = pd.DataFrame(records)
attributes_df = df["attributes"].apply(pd.Series)
df = pd.concat([df.drop(columns=["attributes"]), attributes_df], axis=1)

df