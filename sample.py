import csv 

with open('./csv-files/tagab.csv','r') as csv_tagab_file: 
    csv_tagab_reader = csv.DictReader(csv_tagab_file)
    user_input = input("What word do you want to find: ")
    counter = 0
    verse_counter = 0
    temp_list = []
    print("")
    for row in csv_tagab_reader:
        for word in row['Text'].split():
            if word.upper().strip(' .:,!;[]<>') == user_input.upper():
                counter += 1
                if row['Verse ID'] not in temp_list:
                    verse_counter += 1
                    temp_list.append(row['Verse ID'])
                    print(f"{row['Book Name']} {row['Chapter']}:{row['Verse']}")
                    print(row['Text'])
                    
            else:
                continue
    if counter == 1:
        print("")
        print(counter, "verse found",verse_counter, "match")
    elif counter > 1:
        print("")
        print(counter, "verses found",verse_counter, "matches")
    else:
        print("")
        print("No words found")
            