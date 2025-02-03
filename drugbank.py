import xml.etree.ElementTree as ET
import csv 
import xmlschema
from pprint import pprint
#xs = xmlschema.XMLSchema('drugbank.xsd')
#drug_dict=xs.to_dict('full database.xml')


tree = ET.parse("/Users/jengs/Box/Targetome/drug_bank/full database.xml")
root = tree.getroot()

drug_head = []
count = 0 
{http://www.drugbank.ca}drug v

drugs2=root.findall("{http://www.drugbank.ca}drug")
targets=drugs[0].find("{http://www.drugbank.ca}targets")
drugs[0].find('{http://www.drugbank.ca}targets').find('{http://www.drugbank.ca}target').find('{http://www.drugbank.ca}name').text
drugs[0].find('{http://www.drugbank.ca}targets').find('{http://www.drugbank.ca}target').find('{http://www.drugbank.ca}references').findall('{http://www.drugbank.ca}articles')
drugs[0].find('{http://www.drugbank.ca}targets').find('{http://www.drugbank.ca}target').find('{http://www.drugbank.ca}references').findall('{http://www.drugbank.ca}articles')[0].findall('{http://www.drugbank.ca}article')[0].find('{http://www.drugbank.ca}pubmed-id').text

#get list of all subelements
list(drugs[0].find('{http://www.drugbank.ca}targets').find('{http://www.drugbank.ca}target').iter())
[elem.tag for elem in drugs[0].find('{http://www.drugbank.ca}targets').find('{http://www.drugbank.ca}target').iter()]
references=drugs[0].find('{http://www.drugbank.ca}targets').find('{http://www.drugbank.ca}target').find('{http://www.drugbank.ca}references').find('{http://www.drugbank.ca}articles')
drugs2[0].find('{http://www.drugbank.ca}targets').find('{http://www.drugbank.ca}target').find('{http://www.drugbank.ca}organsim')

tmp_root=drugs2[0].find('{http://www.drugbank.ca}targets').find('{http://www.drugbank.ca}target')
for child in tmp_root.iter():
	print(child.tag, child.attrib)
tmp_root.find('{http://www.drugbank.ca}organism')

{http://www.drugbank.ca}gene-name
{http://www.drugbank.ca}organism {'ncbi-taxonomy-id': 
with open('/Users/jengs/Box/Targetome/output_files/drugbank_test_20210608.csv', 'w', newline='') as csvfile:
	drugwriter = csv.writer(csvfile)
	for drugs in root.findall("{http://www.drugbank.ca}drug"):
		#pids=""
		tname=""
		peptide_id=""
		source=""
		organism=""
		name = drugs.find('{http://www.drugbank.ca}name').text
		refs = drugs.find('{http://www.drugbank.ca}general-references')
		articles = refs.find('{http://www.drugbank.ca}articles')
		num_article = len(articles)
		tar = drugs.find("{http://www.drugbank.ca}targets")
		if (len(tar) > 0):
			pids=""
			for target in tar.findall('{http://www.drugbank.ca}target'):
				polypeptide=target.find('{http://www.drugbank.ca}polypeptide')
				if (polypeptide is not None):
					peptide_id=polypeptide.attrib.get('id')
					source=polypeptide.attrib.get('source')
				organism=target.find('{http://www.drugbank.ca}organism').text
				t_name = target.find('{http://www.drugbank.ca}name')
				if (t_name is not None):	
        				refs = target.find('{http://www.drugbank.ca}references')
					if (refs is not None):
        					for articles in refs.findall('{http://www.drugbank.ca}articles'):
                					for article in articles.findall('{http://www.drugbank.ca}article'):
                        					pid=article.find('{http://www.drugbank.ca}pubmed-id').text
								if (pid is not None):
									pids=pid+'|'+pids
				drugwriter.writerow([name,t_name.text,peptide_id,source,organism,pids])
	



if drugs == "small molecule":
		print(drugs.attrib)

	#name = member.find('Name').text
	#resident.append(name)
	#PhoneNumber = member.find('PhoneNumber').text
	#resident.append(PhoneNumber)
	#EmailAddress = member.find('EmailAddress').text
	#resident.append(EmailAddress)
	#Address = member[3][0].text
	#address_list.append(Address)
	#City = member[3][1].text
	#address_list.append(City)
	#StateCode = member[3][2].text
	#address_list.append(StateCode)
	#PostalCode = member[3][3].text
	#address_list.append(PostalCode)
	#resident.append(address_list)
