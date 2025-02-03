import csv
import pandas as pd
import re

BASE_DIR='/Users/jengs/OneDrive - Oregon Health & Science University/From_Box/Targetome/'
compound=pd.read_csv(BASE_DIR + 'Sorger/sms_tables_chembl_v25/lsp_compound_dictionary.csv',low_memory=False)
target=pd.read_csv(BASE_DIR + 'Sorger/sms_tables_chembl_v25/lsp_target_mapping.csv')
mapping=pd.read_csv(BASE_DIR + 'Sorger/sms_tables_chembl_v25/lsp_compound_library.csv')
binding=pd.read_csv(BASE_DIR + 'Sorger/sms_tables_chembl_v25/lsp_biochem.csv')


drug_target_df=pd.DataFrame()
for index,map in mapping.iterrows():
	lspci=map["lspci_id"]
	gene=map['gene_id']
	reason=map['reason_included']
	binding_evidence=binding.loc[(binding['lspci_id']==lspci) &  (binding['gene_id']==gene)]
	uniprot=target.loc[target['gene_id']==gene,'uniprot_id'].drop_duplicates()
	name=target.loc[target['gene_id']==gene,'pref_name'].drop_duplicates()
	if len(name) > 1:
		name=' | '.join(name)
	else:
		name=name.to_string(index=False)
	name=[name]*len(uniprot)
	drug=compound.loc[compound['lspci_id']==lspci,'pref_name'].to_string(index=False)
	drug=[drug]*len(uniprot)
	reason=[reason]*len(uniprot)
	lspci=[lspci]*len(uniprot)
	gene=[gene]*len(uniprot)
	df=pd.DataFrame({'lspci_id':lspci,'Drug':drug,'Target Name':name,'Uniprot':uniprot,'Reason':reason, 'gene_id':gene})
	df_binding=df.merge(binding_evidence,left_on=['lspci_id','gene_id'],right_on=['lspci_id','gene_id'],how='outer')
	frames=[drug_target_df,df_binding]
	drug_target_df=pd.concat(frames)

drug_target_df.to_csv('sorger_targets.txt',sep='\t',index=False)


