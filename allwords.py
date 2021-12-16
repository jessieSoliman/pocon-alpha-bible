import csv


class AllWords:
    def __init__(self):
        pass
    
    #ALL WORDS ENTIRE BIBLE NONE NONE
    def all_words_entire_bible(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> ENTIRE BIBLE ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        for word in every_line['Text'].split():
                            if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        for word in every_line['Text'].split():
                            if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        for word in every_line['Text'].split():
                            if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def all_words_entire_bible_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> ENTIRE BIBLE -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        for word in every_line['Text'].split():
                            if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        for word in every_line['Text'].split():
                            if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        for word in every_line['Text'].split():
                            if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")              

    def all_words_entire_bible_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> ENTIRE BIBLE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        for word in every_line['Text'].split():
                            if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        for word in every_line['Text'].split():
                            if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        for word in every_line['Text'].split():
                            if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    def all_words_entire_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> ENTIRE BIBLE -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        for word in every_line['Text'].split():
                            if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        for word in every_line['Text'].split():
                            if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        for word in every_line['Text'].split():
                            if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                    
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    #ALL WORDS OLD TESTAMENT NONE NONE
    def all_words_old_testament(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> OLD TESTAMENT ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        if int(every_line['Verse ID']) >= 1 and int(every_line['Verse ID']) <= 23145:
                            for word in every_line['Text'].split():
                    
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                    
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def all_words_old_testament_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> OLD TESTAMENT -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")              

    def all_words_old_testament_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> OLD TESTAMENT -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    def all_words_old_testament_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> OLD TESTAMENT -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        if int(every_line['Book Number']) >= 1 and int(every_line['Book Number']) <= 39:
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    #ALL WORDS NEW TESTAMENT NONE NONE
    def all_words_new_testament(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> NEW TESTAMENT ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                    
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                    
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def all_words_new_testament_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> NEW TESTAMENT -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")              

    def all_words_new_testament_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> NEW TESTAMENT -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    def all_words_new_testament_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> NEW TESTAMENT -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        if int(every_line['Book Number']) >= 40 and int(every_line['Book Number']) <= 66:
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    
    #ALL WORDS GENESIS NONE NONE
    def all_words_genesis(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> GENESIS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                    
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                    
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def all_words_genesis_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> GENESIS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")              

    def all_words_genesis_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> GENESIS-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    def all_words_genesis_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> GENESIS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 1:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    #ALL WORDS EXODUS NONE NONE
    def all_words_exodus(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> EXODUS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                    
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                    
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def all_words_exodus_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> EXODUS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")              

    def all_words_exodus_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> EXODUS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    def all_words_exodus_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> EXODUS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 2:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    


    #ALL WORDS LEVITICUS  NONE NONE
    def all_words_leviticus(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> LEVITICUS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                    
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                    
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def all_words_leviticus_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> LEVITICUS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")              

    def all_words_leviticus_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> LEVITICUS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    def all_words_leviticus_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> LEVITICUS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 3:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    #ALL WORDS NUMBERS  NONE NONE
    def all_words_numbers(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> NUMBERS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                    
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                    
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def all_words_numbers_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> NUMBERS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")              

    def all_words_numbers_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> NUMBERS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    def all_words_numbers_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> NUMBERS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 4:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    #ALL WORDS DEUTERONOMY  NONE NONE
    def all_words_numbers(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> DEUTERONOMY ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                    
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                    
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                            else:
                                continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.upper().strip(' ?;[]"<>.:,!‹›¶') == search_user_input.upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def all_words_deuteronomy_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> DEUTERONOMY -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if word.strip(' ?;[]"<>.:,!‹›¶') == search_user_input:
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")              

    def all_words_deuteronomy_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> DEUTERONOMY -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input.upper() in word.strip(' ?;[]"<>.:,!‹›¶').upper():
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    

    def all_words_deuteronomy_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ALL WORDS -> DEUTERONOMY -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("What word do you want to find: ")
        print("")
        print("****CHOOSE THE BIBLE VERSION****")
        print("[1] ANG DATING BIBLIA")
        print("[2] AUTHORIZED KING JAMES VERSION")
        print("[3] AMERICAN STANDARD VERSION") 
        print("")
        try:
            search_user_version = int(input("Enter the number: "))
            if search_user_version == 1:
                with open('./csv-files/tagab.csv','r') as csv_tagalog_file: 
                    csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
                    print("")
                    for every_line in csv_tagalog_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 2:
                with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                    csv_king_james_reader = csv.DictReader(csv_king_james_file)
                    print("")
                    for every_line in csv_king_james_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            elif search_user_version == 3:    
                with open('./csv-files/asv.csv','r') as csv_asv_file:
                    csv_asv_reader = csv.DictReader(csv_asv_file)

                    print("")
                    for every_line in csv_asv_reader:
                        # -----------------------------------
                        if int(every_line['Book Number']) == 5:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                if search_user_input in word.strip(' ?;[]"<>.:,!‹›¶'):
                                    occurences_in_verse += 1
                                    if every_line['Verse ID'] not in validate_item:
                                        number_of_verse += 1
                                        validate_item.append(every_line['Verse ID'])
                                        print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                        print(every_line['Text'])
                                        
                                else:
                                    continue
                print("")
                if number_of_verse <= 1 and occurences_in_verse <= 1:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} match")
                elif number_of_verse <= 1 and occurences_in_verse >= 2:
                    print(f"{number_of_verse} verse were found with {occurences_in_verse} matches")
                else:
                    print(f"{number_of_verse} verses were found with {occurences_in_verse} matches")
            else:
                print(f"My Apologies, {search_user_version} is invalid")


        except ValueError:
            print("")
            print("Oops! be careful in typing")    







ol_words = AllWords()