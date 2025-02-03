import csv 
import pandas as pd
import os 

BASE_DIR="/Users/jengs/OneDrive - Oregon Health & Science University/From_Box/"
pubchem_files=os.listdir(BASE_DIR + 'Targetome/pubchem')


pubchem_bioassay_data=[]
for pubchem_file in pubchem_files:
	print(pubchem_file)
	if pubchem_file != "Aid2GeneidAccessionUniProt":
		bioassay=pd.read_csv(BASE_DIR + 'Targetome/pubchem/'+pubchem_file)
		pubchem_bioassay_data.append(bioassay[["cmpdname","targetname","taxid","geneid","pmid","protacxn","aid","aidtype","acname","acqualifier","acvalue","activity"]])


pubchem_bioassay_dataframe=pd.concat(pubchem_bioassay_data,ignore_index=True)
pubchem_bioassay_dataframe.to_csv("pubchem_manual.txt",sep="\t",index=False,header=True)








