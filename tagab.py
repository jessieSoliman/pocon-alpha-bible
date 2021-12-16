import csv

# TAGALOG VERSION
with open('./csv/tagab.csv','r') as csv_tagab_file:
    csv_tagab_reader = csv.DictReader(csv_tagab_file)