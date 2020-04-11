import csv
import json
import os

pwd =  os.getcwd()
heads = "field_names.txt"
#raw
ic = pwd+"/ahdb_data/ic_function/"
admet = pwd+"/ahdb_data/admet/"
#pdb
mw = pwd+"/ahdb_data/peptide_mw/"
#link
pics = "/ahdb_data/Peptide_pics/"


def folder_to_dict_raw(path,pep):

    with open(path+heads) as field_names_file:
            fields = csv.reader(field_names_file)
            for row in fields:
                field_names = row
    
    with open(path+pep, 'r',encoding='utf-8') as csvfile:
        reader = csv.DictReader( csvfile, field_names,delimiter=';')
        for row in reader:
            row_dict = row

    return row_dict

def folder_to_dict_pdb(path,pep):

    with open(path+heads) as field_names_file:
            fields = csv.reader(field_names_file)
            for row in fields:
                field_names = row
    
    with open(path+pep+'.pdb', 'r',encoding='utf-8') as csvfile:
        reader = csv.DictReader( csvfile, field_names,delimiter=';')
        for row in reader:
            row_dict = row

    return row_dict

def folder_to_dict_link(path,pep):

    with open(pwd+path+heads) as field_names_file:
            fields = csv.reader(field_names_file)
            for row in fields:
                field_names = row
 
    row_dict = {field_names[0]:path+pep+".png"}

    return row_dict

# not using isfile checks
peppy_list = os.scandir(ic)
peps = [ n.name for n in peppy_list ]
peps.remove(heads)



with open('alles_pep.json', 'w') as jsonfile:
    for pep in peps:
        row_ic = folder_to_dict_raw(ic,pep)
        row_admet = folder_to_dict_raw(admet,pep)
        row_mw = folder_to_dict_pdb(mw,pep)
        row_pics = folder_to_dict_link(pics,pep)
        row_all = {**row_ic,**row_admet,**row_mw,**row_pics}
        json.dump(row_all, jsonfile)
        jsonfile.write('\n')

    



# csvfile = open('AA', 'r',encoding='utf-8')
# jsonfile = open('AA_ic.json', 'w')

# fieldnames = ("Peptide_Sequence", "Origin", "Peptide_Preparation",
#               "Isolation_Method", "ACE_inhibition_assay", "In-vivo_or_in-vitro",
#               "IC50_micromol_per_L", "Reference", "Binding_Energy_kcal_per_mol")
# reader = csv.DictReader( csvfile, fieldnames,delimiter=';')
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write('\n')