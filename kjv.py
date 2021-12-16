import csv

# KING JAMES VERSION
with open('./csv/kjv.csv','r') as csv_kjv_file:
    csv_kjv_reader = csv.DictReader(csv_kjv_file)