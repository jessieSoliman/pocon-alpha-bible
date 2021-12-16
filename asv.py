import csv

# AMERICAN STANDARD VERSION
with open('./csv/asv.csv','r') as csv_asv_file:
    csv_asv_reader = csv.DictReader(csv_asv_file)


    def test():
        counter = 0
        verse_counter = 0
        temp_list = []
        for row in csv_asv_reader:
            for word in row['Text'].split():
                multiple_words =['Gnat','eternity','grandmother']
                for item in multiple_words:
                    if item.upper() == word.strip(' .,!;:[]<>?').upper():
                        counter +=1
                        if row['Verse ID'] not in temp_list:
                            verse_counter += 1
                            temp_list.append(row['Verse ID'])
                            print(f"{row['Book Name']} {row['Chapter']}:{row['Verse']}")
                            print(row['Text'])
                        
        print(f"{verse_counter} verses found, {counter} matches")
