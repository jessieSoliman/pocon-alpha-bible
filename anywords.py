import csv


class AnyWords:
    def __init__(self):
        pass
    
    #ANY WORDS ENTIRE BIBLE NONE NONE
    def any_words_entire_bible(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ENTIRE BIBLE ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                            for item in search_user_input.split():
                                if item.upper() == word.strip(' ?;[]"<>.:,!‹›¶').upper():
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
                            for item in search_user_input.split():
                                if item.upper() == word.strip(' ?;[]"<>.:,!‹›¶').upper():
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
                            for item in search_user_input.split():
                                if item.upper() == word.strip(' ?;[]"<>.:,!‹›¶').upper():
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

    def any_words_entire_bible_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ENTIRE BIBLE -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                            for item in search_user_input.split():
                                if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                            for item in search_user_input.split():
                                if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                            for item in search_user_input.split():
                                if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_entire_bible_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ENTIRE BIBLE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    def any_words_entire_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ENTIRE BIBLE -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    #ANY WORDS OLD TESTAMENT NONE NONE
    def any_words_old_testament(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> OLD TESTAMENT ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_old_testament_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> OLD TESTAMENT -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_old_testament_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> OLD TESTAMENT -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    def any_words_old_testament_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> OLD TESTAMENT -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    #ANY WORDS NEW TESTAMENT NONE NONE
    def any_words_new_testament(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NEW TESTAMENT ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_new_testament_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NEW TESTAMENT -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_new_testament_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NEW TESTAMENT -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    def any_words_new_testament_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NEW TESTAMENT -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    
    #ANY WORDS GENESIS NONE NONE
    def any_words_genesis(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> GENESIS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_genesis_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> GENESIS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_genesis_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> GENESIS-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    def any_words_genesis_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> GENESIS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    #ANY WORDS EXODUS NONE NONE
    def any_words_exodus(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> EXODUS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_exodus_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> EXODUS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_exodus_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> EXODUS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    def any_words_exodus_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> EXODUS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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


    #ANY WORDS LEVITICUS  NONE NONE
    def any_words_leviticus(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> LEVITICUS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_leviticus_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> LEVITICUS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_leviticus_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> LEVITICUS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    def any_words_leviticus_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> LEVITICUS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    #ANY WORDS NUMBERS  NONE NONE
    def any_words_numbers(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NUMBERS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_numbers_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NUMBERS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_numbers_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NUMBERS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    def any_words_numbers_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NUMBERS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    #ANY WORDS DEUTERONOMY  NONE NONE
    def any_words_deuteronomy(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> DEUTERONOMY ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_deuteronomy_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> DEUTERONOMY -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_deuteronomy_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> DEUTERONOMY -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    def any_words_deuteronomy_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> DEUTERONOMY -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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

    #ANY WORDS JOSHUA  NONE NONE
    def any_words_joshua(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOSHUA ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 6:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 6:
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
                        if int(every_line['Book Number']) == 6:
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

    def any_words_joshua_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOSHUA -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 6:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 6:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 6:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_joshua_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOSHUA-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 6:
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
                        if int(every_line['Book Number']) == 6:
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
                        if int(every_line['Book Number']) == 6:
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

    def any_words_joshua_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOSHUA -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 6:
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
                        if int(every_line['Book Number']) == 6:
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
                        if int(every_line['Book Number']) == 6:
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

    #ANY WORDS JUDGES  NONE NONE
    def any_words_judges(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JUDGES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 7:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 7:
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
                        if int(every_line['Book Number']) == 7:
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

    def any_words_judges_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JUDGES -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 7:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 7:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 7:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_judges_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JUDGES-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 7:
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
                        if int(every_line['Book Number']) == 7:
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
                        if int(every_line['Book Number']) == 7:
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

    def any_words_judges_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JUDGES -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 7:
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
                        if int(every_line['Book Number']) == 7:
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
                        if int(every_line['Book Number']) == 7:
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


    #ANY WORDS RUTH  NONE NONE
    def any_words_ruth(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> RUTH ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 8:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 8:
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
                        if int(every_line['Book Number']) == 8:
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

    def any_words_ruth_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> RUTH -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 8:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 8:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 8:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_ruth_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> RUTH -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 8:
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
                        if int(every_line['Book Number']) == 8:
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
                        if int(every_line['Book Number']) == 8:
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

    def any_words_ruth_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> RUTH -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 8:
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
                        if int(every_line['Book Number']) == 8:
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
                        if int(every_line['Book Number']) == 8:
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


    #ANY WORDS 1 SAMUEL  NONE NONE
    def any_words_1samuel(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 SAMUEL ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 9:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 9:
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
                        if int(every_line['Book Number']) == 9:
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

    def any_words_1samuel_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 SAMUEL -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 9:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 9:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 9:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_1samuel_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 SAMUEL -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 9:
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
                        if int(every_line['Book Number']) == 9:
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
                        if int(every_line['Book Number']) == 9:
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

    def any_words_1samuel_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 SAMUEL -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 9:
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
                        if int(every_line['Book Number']) == 9:
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
                        if int(every_line['Book Number']) == 9:
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

    #ANY WORDS 2 SAMUEL  NONE NONE
    def any_words_2samuel(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 SAMUEL ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 10:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 10:
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
                        if int(every_line['Book Number']) == 10:
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

    def any_words_2samuel_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 SAMUEL -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 10:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 10:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 10:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_2samuel_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 SAMUEL -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 10:
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
                        if int(every_line['Book Number']) == 10:
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
                        if int(every_line['Book Number']) == 10:
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

    def any_words_2samuel_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 SAMUEL -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 10:
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
                        if int(every_line['Book Number']) == 10:
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
                        if int(every_line['Book Number']) == 10:
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


    #ANY WORDS 1 KINGS  NONE NONE
    def any_words_1kings(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 KINGS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 11:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 11:
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
                        if int(every_line['Book Number']) == 11:
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

    def any_words_1kings_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 KINGS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 11:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 11:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 11:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_1kings_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 KINGS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 11:
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
                        if int(every_line['Book Number']) == 11:
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
                        if int(every_line['Book Number']) == 11:
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

    def any_words_1kings_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 KINGS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 11:
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
                        if int(every_line['Book Number']) == 11:
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
                        if int(every_line['Book Number']) == 11:
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

    #ANY WORDS 2 KINGS  NONE NONE
    def any_words_2kings(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 KINGS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 12:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 12:
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
                        if int(every_line['Book Number']) == 12:
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

    def any_words_2kings_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 KINGS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 12:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 12:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 12:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_2kings_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 KINGS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 12:
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
                        if int(every_line['Book Number']) == 12:
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
                        if int(every_line['Book Number']) == 12:
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

    def any_words_2kings_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 KINGS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 12:
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
                        if int(every_line['Book Number']) == 12:
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
                        if int(every_line['Book Number']) == 12:
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

    #ANY WORDS 1 CHRONICLES  NONE NONE
    def any_words_1chronicles(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 CHRONICLES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 13:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 13:
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
                        if int(every_line['Book Number']) == 13:
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

    def any_words_1chronicles_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 CHRONICLES -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 13:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 13:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 13:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_1chronicles_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 CHRONICLES-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 13:
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
                        if int(every_line['Book Number']) == 13:
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
                        if int(every_line['Book Number']) == 13:
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

    def any_words_1chronicles_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 1 CHRONICLES -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 13:
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
                        if int(every_line['Book Number']) == 13:
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
                        if int(every_line['Book Number']) == 13:
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

    #ANY WORDS 2 CHRONICLES  NONE NONE
    def any_words_2chronicles(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 CHRONICLES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 14:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 14:
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
                        if int(every_line['Book Number']) == 14:
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

    def any_words_2chronicles_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 CHRONICLES -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 14:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 14:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 14:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_2chronicles_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 CHRONICLES-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 14:
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
                        if int(every_line['Book Number']) == 14:
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
                        if int(every_line['Book Number']) == 14:
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

    def any_words_2chronicles_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 CHRONICLES -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 14:
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
                        if int(every_line['Book Number']) == 14:
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
                        if int(every_line['Book Number']) == 14:
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

    #ANY WORDS EZRA NONE NONE
    def any_words_ezra(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> 2 CHRONICLES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 15:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 15:
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
                        if int(every_line['Book Number']) == 15:
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

    def any_words_ezra_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> EZRA -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 15:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 15:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 15:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_ezra_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> EZRA -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 15:
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
                        if int(every_line['Book Number']) == 15:
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
                        if int(every_line['Book Number']) == 15:
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

    def any_words_ezra_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> EZRA -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 15:
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
                        if int(every_line['Book Number']) == 15:
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
                        if int(every_line['Book Number']) == 15:
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
    
    #ANY WORDS NEHEMIAH NONE NONE
    def any_words_nehemiah(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NEHEMIAH ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 16:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 16:
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
                        if int(every_line['Book Number']) == 16:
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

    def any_words_nehemiah_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NEHEMIAH -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 16:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 16:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 16:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_nehemiah_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NEHEMIAH -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 16:
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
                        if int(every_line['Book Number']) == 16:
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
                        if int(every_line['Book Number']) == 16:
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

    def any_words_nehemiah_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> NEHEMIAH -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 16:
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
                        if int(every_line['Book Number']) == 16:
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
                        if int(every_line['Book Number']) == 16:
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

    #ANY WORDS ESTHER NONE NONE
    def any_words_esther(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ESTHER ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 17:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 17:
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
                        if int(every_line['Book Number']) == 17:
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

    def any_words_esther_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ESTHER -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 17:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 17:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 17:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_esther_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ESTHER -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 17:
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
                        if int(every_line['Book Number']) == 17:
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
                        if int(every_line['Book Number']) == 17:
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

    def any_words_esther_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ESTHER -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 17:
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
                        if int(every_line['Book Number']) == 17:
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
                        if int(every_line['Book Number']) == 17:
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

    #ANY WORDS JOB NONE NONE
    def any_words_job(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOB ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 18:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 18:
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
                        if int(every_line['Book Number']) == 18:
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

    def any_words_job_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOB -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 18:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 18:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 18:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_job_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOB -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 18:
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
                        if int(every_line['Book Number']) == 18:
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
                        if int(every_line['Book Number']) == 18:
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

    def any_words_job_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOB -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 18:
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
                        if int(every_line['Book Number']) == 18:
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
                        if int(every_line['Book Number']) == 18:
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
    
    #ANY WORDS PSALMS NONE NONE
    def any_words_psalms(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> PSALMS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 19:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 19:
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
                        if int(every_line['Book Number']) == 19:
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

    def any_words_psalms_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> PSALMS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 19:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 19:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 19:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_psalms_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> PSALMS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 19:
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
                        if int(every_line['Book Number']) == 19:
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
                        if int(every_line['Book Number']) == 19:
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

    def any_words_psalms_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> PSALMS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 19:
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
                        if int(every_line['Book Number']) == 19:
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
                        if int(every_line['Book Number']) == 19:
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

    #ANY WORDS PROVERBS NONE NONE
    def any_words_proverbs(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> PROVERBS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 20:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 20:
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
                        if int(every_line['Book Number']) == 20:
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

    def any_words_proverbs_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> PROVERBS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 20:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 20:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 20:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_proverbs_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> PROVERBS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 20:
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
                        if int(every_line['Book Number']) == 20:
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
                        if int(every_line['Book Number']) == 20:
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

    def any_words_proverbs_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> PROVERBS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 20:
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
                        if int(every_line['Book Number']) == 20:
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
                        if int(every_line['Book Number']) == 20:
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

    #ANY WORDS ECCLESIASTES NONE NONE
    def any_words_ecclesiastes(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ECCLESIASTES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 21:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 21:
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
                        if int(every_line['Book Number']) == 21:
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

    def any_words_ecclesiastes_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ECCLESIASTES -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 21:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 21:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 21:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_ecclesiastes_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ECCLESIASTES-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 21:
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
                        if int(every_line['Book Number']) == 21:
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
                        if int(every_line['Book Number']) == 21:
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

    def any_words_ecclesiastes_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ECCLESIASTES -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 21:
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
                        if int(every_line['Book Number']) == 21:
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
                        if int(every_line['Book Number']) == 21:
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


    #ANY WORDS SONG OF SOLOMON NONE NONE
    def any_words_song_of_solomon(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> SONG OF SOLOMON ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 22:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 22:
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
                        if int(every_line['Book Number']) == 22:
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

    def any_words_song_of_solomon_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> SONG OF SOLOMON -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 22:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 22:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 22:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_song_of_solomon_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> SONG OF SOLOMON -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 22:
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
                        if int(every_line['Book Number']) == 22:
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
                        if int(every_line['Book Number']) == 22:
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

    def any_words_song_of_solomon_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> SONG OF SOLOMON -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 22:
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
                        if int(every_line['Book Number']) == 22:
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
                        if int(every_line['Book Number']) == 22:
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

    
    #ANY WORDS ISAIAH NONE NONE
    def any_words_isaiah(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ISAIAH ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 23:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 23:
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
                        if int(every_line['Book Number']) == 23:
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

    def any_words_isaiah_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ISAIAH -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 23:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 23:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 23:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_isaiah_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ISAIAH -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 23:
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
                        if int(every_line['Book Number']) == 23:
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
                        if int(every_line['Book Number']) == 23:
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

    def any_words_isaiah_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> ISAIAH -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 23:
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
                        if int(every_line['Book Number']) == 23:
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
                        if int(every_line['Book Number']) == 23:
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

    #ANY WORDS JEREMIAH NONE NONE
    def any_words_jeremiah(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JEREMIAH ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 24:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 24:
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
                        if int(every_line['Book Number']) == 24:
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

    def any_words_jeremiah_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JEREMIAH -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 24:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 24:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 24:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_jeremiah_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JEREMIAH -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 24:
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
                        if int(every_line['Book Number']) == 24:
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
                        if int(every_line['Book Number']) == 24:
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

    def any_words_jeremiah_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JEREMIAH -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 24:
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
                        if int(every_line['Book Number']) == 24:
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
                        if int(every_line['Book Number']) == 24:
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



    # NEW TESTAMENT

    #ANY WORDS MATTHEW NONE NONE
    def any_words_matthew(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> MATTHEW ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 40:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 40:
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
                        if int(every_line['Book Number']) == 40:
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

    def any_words_matthew_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> MATTHEW -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 40:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 40:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 40:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_matthew_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> MATTHEW -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 40:
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
                        if int(every_line['Book Number']) == 40:
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
                        if int(every_line['Book Number']) == 40:
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

    def any_words_matthew_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> MATTHEW -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 40:
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
                        if int(every_line['Book Number']) == 40:
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
                        if int(every_line['Book Number']) == 40:
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


    #ANY WORDS MARK NONE NONE
    def any_words_mark(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> MARK")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 41:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 41:
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
                        if int(every_line['Book Number']) == 41:
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

    def any_words_mark_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> MARK -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 41:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 41:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 41:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_mark_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> MARK -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 41:
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
                        if int(every_line['Book Number']) == 41:
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
                        if int(every_line['Book Number']) == 41:
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

    def any_words_mark_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> MARK -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 41:
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
                        if int(every_line['Book Number']) == 41:
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
                        if int(every_line['Book Number']) == 41:
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

    
    #ANY WORDS LUKE NONE NONE
    def any_words_luke(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> LUKE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 42:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 42:
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
                        if int(every_line['Book Number']) == 42:
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

    def any_words_luke_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> LUKE -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 42:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 42:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 42:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_luke_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> LUKE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 42:
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
                        if int(every_line['Book Number']) == 42:
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
                        if int(every_line['Book Number']) == 42:
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

    def any_words_luke_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> LUKE -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 42:
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
                        if int(every_line['Book Number']) == 42:
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
                        if int(every_line['Book Number']) == 42:
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

    #ANY WORDS JOHN NONE NONE
    def any_words_john(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOHN")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 43:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item.upper() == word.upper().strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 43:
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
                        if int(every_line['Book Number']) == 43:
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

    def any_words_john_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOHN -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 43:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 43:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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
                        if int(every_line['Book Number']) == 43:
                        # -----------------------------------
                            for word in every_line['Text'].split():
                                for item in search_user_input.split():
                                    if item == word.strip(' ?;[]"<>.:,!‹›¶'):
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

    def any_words_john_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOHN -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 43:
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
                        if int(every_line['Book Number']) == 43:
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
                        if int(every_line['Book Number']) == 43:
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

    def any_words_john_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("ANY WORDS -> JOHN -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the words you want to find: ")
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
                        if int(every_line['Book Number']) == 43:
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
                        if int(every_line['Book Number']) == 43:
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
                        if int(every_line['Book Number']) == 43:
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




any_words = AnyWords()
