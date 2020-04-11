import csv
import json

csvfile = open('AA', 'r')
jsonfile = open('AA_ic.json', 'w')

fieldnames = ("Peptide_Sequence", "Origin", "Peptide_Preparation",
              "Isolation_Method", "ACE_inhibition_assay", "In-vivo_or_in-vitro",
              "IC50_micromol_per_L", "Reference", "Binding_Energy_kcal_per_mol")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n') 
