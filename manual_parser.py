import csv
import json
import os

pwd =  os.getcwd()
peps = [line.rstrip() for line in open('peptides_1588.pf')]

heads = "field_names.txt"
#raw
ic = pwd+"/ahdb_data/ic_function/"
admet = pwd+"/ahdb_data/admet/"
#pdb
mw = pwd+"/ahdb_data/peptide_mw/"
#duallink
ACE_html = "/ahdb_data/ACE_complex_html/"
#link
ACE_comp = "/ahdb_data/ACE_peptide_complex/"
ACE_pics = "/ahdb_data/ACE_peptide_complex-pics/"
da = "/ahdb_data/peptide_da/"
htmls = "/ahdb_data/Peptide_html/"
mini_strc = "/ahdb_data/peptide_minimized_structures/"
pics = "/ahdb_data/Peptide_pics/"


def folder_to_dict_raw(path,pep):

    with open(path+heads) as field_names_file:
            fields = csv.reader(field_names_file)
            for row in fields:
                field_names = row
    try:
        with open(path+pep, 'r',encoding='utf-8') as csvfile:
            reader = csv.DictReader( csvfile, field_names,delimiter=';')
            for row in reader:
                row_dict = row
    except FileNotFoundError:
        row_dict = {fd : "#" for fd in field_names}

    return row_dict

def folder_to_dict_pdb(path,pep):

    with open(path+heads) as field_names_file:
            fields = csv.reader(field_names_file)
            for row in fields:
                field_names = row
    try:
        with open(path+pep+'.pdb', 'r',encoding='utf-8') as csvfile:
            reader = csv.DictReader( csvfile, field_names,delimiter=';')
            for row in reader:
                row_dict = row
    except FileNotFoundError:
        row_dict = {fd : "#" for fd in field_names}

    return row_dict

def folder_to_dict_link(path,pep,link,isACE):

    with open(pwd+path+heads) as field_names_file:
            fields = csv.reader(field_names_file)
            for row in fields:
                field_names = row
    try:
        with open(pwd+path+isACE+pep+link, 'r',encoding='utf-8'):
            row_dict = {field_names[0]:pwd+path+isACE+pep+link}
    except FileNotFoundError:
        row_dict = {fd : "#" for fd in field_names}

    return row_dict

def folder_to_dict_duallink(path,pep,link1,link2,isACE):

    with open(pwd+path+heads) as field_names_file:
            fields = csv.reader(field_names_file)
            for row in fields:
                field_names = row
    try:
        with open(pwd+path+isACE+pep+link1, 'r',encoding='utf-8'):
            row_dict = {field_names[0]:pwd+path+isACE+pep+link1,field_names[1]:pwd+path+isACE+pep+link2}
    except FileNotFoundError:
        row_dict = {fd : "#" for fd in field_names}

    return row_dict

# using isfile checks
# peppy_list = os.scandir(ic)
# peps = [ n.name for n in peppy_list ]
# peps.remove(heads)

idx=1

with open('alles_pep.json', 'w') as jsonfile:
    for pep in peps:
        print(pep)
        row_ic = folder_to_dict_raw(ic,pep)
        row_admet = folder_to_dict_raw(admet,pep)

        row_mw = folder_to_dict_pdb(mw,pep)

        row_ACE_html = folder_to_dict_duallink(ACE_html,pep,".pdb.html",".pdbatoms.txt","ACE_")

        row_ACE_comp = folder_to_dict_link(ACE_comp,pep,".pdb","ACE_")
        row_ACE_pics = folder_to_dict_link(ACE_pics,pep,".png","ACE_")

        row_da = folder_to_dict_link(da,pep,".pdb","")
        row_htmls = folder_to_dict_link(htmls,pep,".pdb.html","")
        row_mini_strc = folder_to_dict_link(mini_strc,pep,".pdb","")
        row_pics = folder_to_dict_link(pics,pep,".png","")

        row_idx = {"_id":idx}
        row_par = {"index":row_idx}
        idx = idx +1
        json.dump(row_par, jsonfile)
        jsonfile.write('\n')
        
        row_all = {**row_ic,**row_admet, **row_mw,**row_ACE_html,**row_ACE_comp,**row_ACE_pics,**row_da,**row_htmls,**row_mini_strc,**row_pics}
        json.dump(row_all, jsonfile)
        jsonfile.write('\n')