import csv


class Phrase:
    def __init__(self):
        pass
    
    #PHRASE ENTIRE BIBLE NONE NONE
    def phrase_entire_bible(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ENTIRE BIBLE ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_entire_bible_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ENTIRE BIBLE -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_entire_bible_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ENTIRE BIBLE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
            
                        if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                            occurences_in_verse += 1
                            if every_line['Verse ID'] not in validate_item:
                                number_of_verse += 1
                                validate_item.append(every_line['Verse ID'])
                                print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                print(every_line['Text'])
                                    
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
            
                        if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                            occurences_in_verse += 1
                            if every_line['Verse ID'] not in validate_item:
                                number_of_verse += 1
                                validate_item.append(every_line['Verse ID'])
                                print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                print(every_line['Text'])
                                    
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
            
                        if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                            occurences_in_verse += 1
                            if every_line['Verse ID'] not in validate_item:
                                number_of_verse += 1
                                validate_item.append(every_line['Verse ID'])
                                print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                print(every_line['Text'])
                                    
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

    def phrase_entire_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ENTIRE BIBLE -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        
                        if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                            occurences_in_verse += 1
                            if every_line['Verse ID'] not in validate_item:
                                number_of_verse += 1
                                validate_item.append(every_line['Verse ID'])
                                print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                print(every_line['Text'])
                                    
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
                        
                        if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                            occurences_in_verse += 1
                            if every_line['Verse ID'] not in validate_item:
                                number_of_verse += 1
                                validate_item.append(every_line['Verse ID'])
                                print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                print(every_line['Text'])
                                    
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
                        
                        if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                            occurences_in_verse += 1
                            if every_line['Verse ID'] not in validate_item:
                                number_of_verse += 1
                                validate_item.append(every_line['Verse ID'])
                                print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                print(every_line['Text'])
                                    
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

    #PHRASE OLD TESTAMENT NONE NONE
    def phrase_old_testament(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> OLD TESTAMENT ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_old_testament_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> OLD TESTAMENT -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_old_testament_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> OLD TESTAMENT -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_old_testament_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> OLD TESTAMENT -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE NEW TESTAMENT NONE NONE
    def phrase_new_testament(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NEW TESTAMENT ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_new_testament_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NEW TESTAMENT -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_new_testament_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NEW TESTAMENT -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_new_testament_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NEW TESTAMENT -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    
    #PHRASE GENESIS NONE NONE
    def phrase_genesis(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> GENESIS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_genesis_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> GENESIS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_genesis_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> GENESIS-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_genesis_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> GENESIS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE EXODUS NONE NONE
    def phrase_exodus(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> EXODUS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_exodus_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> EXODUS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_exodus_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> EXODUS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_exodus_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> EXODUS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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


    #PHRASE LEVITICUS  NONE NONE
    def phrase_leviticus(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> LEVITICUS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_leviticus_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> LEVITICUS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_leviticus_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> LEVITICUS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_leviticus_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> LEVITICUS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE NUMBERS  NONE NONE
    def phrase_numbers(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NUMBERS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_numbers_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NUMBERS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_numbers_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NUMBERS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_numbers_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NUMBERS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE DEUTERONOMY  NONE NONE
    def phrase_deuteronomy(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> DEUTERONOMY ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_deuteronomy_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> DEUTERONOMY -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_deuteronomy_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> DEUTERONOMY -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_deuteronomy_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> DEUTERONOMY -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE JOSHUA  NONE NONE
    def phrase_joshua(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOSHUA ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_joshua_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOSHUA -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 6:
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
                        if int(every_line['Book Number']) == 6:
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

    def phrase_joshua_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOSHUA-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_joshua_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOSHUA -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE JUDGES  NONE NONE
    def phrase_judges(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JUDGES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_judges_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JUDGES -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 7:
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
                        if int(every_line['Book Number']) == 7:
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

    def phrase_judges_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JUDGES-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_judges_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JUDGES -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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


    #PHRASE RUTH  NONE NONE
    def phrase_ruth(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> RUTH ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_ruth_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> RUTH -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 8:
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
                        if int(every_line['Book Number']) == 8:
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

    def phrase_ruth_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> RUTH -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_ruth_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> RUTH -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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


    #PHRASE 1 SAMUEL  NONE NONE
    def phrase_1samuel(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 SAMUEL ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_1samuel_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 SAMUEL -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 9:
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
                        if int(every_line['Book Number']) == 9:
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

    def phrase_1samuel_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 SAMUEL -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_1samuel_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 SAMUEL -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE 2 SAMUEL  NONE NONE
    def phrase_2samuel(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 SAMUEL ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_2samuel_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 SAMUEL -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 10:
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
                        if int(every_line['Book Number']) == 10:
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

    def phrase_2samuel_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 SAMUEL -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_2samuel_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 SAMUEL -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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


    #PHRASE 1 KINGS  NONE NONE
    def phrase_1kings(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 KINGS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_1kings_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 KINGS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 11:
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
                        if int(every_line['Book Number']) == 11:
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

    def phrase_1kings_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 KINGS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_1kings_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 KINGS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE 2 KINGS  NONE NONE
    def phrase_2kings(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 KINGS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_2kings_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 KINGS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 12:
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
                        if int(every_line['Book Number']) == 12:
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

    def phrase_2kings_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 KINGS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_2kings_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 KINGS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE 1 CHRONICLES  NONE NONE
    def phrase_1chronicles(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 CHRONICLES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_1chronicles_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 CHRONICLES -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 13:
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
                        if int(every_line['Book Number']) == 13:
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

    def phrase_1chronicles_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 CHRONICLES-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_1chronicles_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 1 CHRONICLES -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE 2 CHRONICLES  NONE NONE
    def phrase_2chronicles(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 CHRONICLES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_2chronicles_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 CHRONICLES -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 14:
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
                        if int(every_line['Book Number']) == 14:
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

    def phrase_2chronicles_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 CHRONICLES-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_2chronicles_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 CHRONICLES -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE EZRA NONE NONE
    def phrase_ezra(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> 2 CHRONICLES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_ezra_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> EZRA -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 15:
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
                        if int(every_line['Book Number']) == 15:
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

    def phrase_ezra_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> EZRA -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_ezra_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> EZRA -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
    
    #PHRASE NEHEMIAH NONE NONE
    def phrase_nehemiah(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NEHEMIAH ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_nehemiah_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NEHEMIAH -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 16:
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
                        if int(every_line['Book Number']) == 16:
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

    def phrase_nehemiah_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NEHEMIAH -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_nehemiah_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> NEHEMIAH -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE ESTHER NONE NONE
    def phrase_esther(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ESTHER ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_esther_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ESTHER -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 17:
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
                        if int(every_line['Book Number']) == 17:
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

    def phrase_esther_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ESTHER -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_esther_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ESTHER -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE JOB NONE NONE
    def phrase_job(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOB ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_job_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOB -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 18:
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
                        if int(every_line['Book Number']) == 18:
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

    def phrase_job_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOB -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_job_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOB -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
    
    #PHRASE PSALMS NONE NONE
    def phrase_psalms(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> PSALMS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_psalms_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> PSALMS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 19:
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
                        if int(every_line['Book Number']) == 19:
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

    def phrase_psalms_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> PSALMS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_psalms_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> PSALMS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE PROVERBS NONE NONE
    def phrase_proverbs(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> PROVERBS ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_proverbs_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> PROVERBS -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 20:
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
                        if int(every_line['Book Number']) == 20:
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

    def phrase_proverbs_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> PROVERBS -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_proverbs_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> PROVERBS -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE ECCLESIASTES NONE NONE
    def phrase_ecclesiastes(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ECCLESIASTES ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_ecclesiastes_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ECCLESIASTES -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 21:
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
                        if int(every_line['Book Number']) == 21:
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

    def phrase_ecclesiastes_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ECCLESIASTES-> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_ecclesiastes_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ECCLESIASTES -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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


    #PHRASE SONG OF SOLOMON NONE NONE
    def phrase_song_of_solomon(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> SONG OF SOLOMON ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_song_of_solomon_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> SONG OF SOLOMON -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 22:
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
                        if int(every_line['Book Number']) == 22:
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

    def phrase_song_of_solomon_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> SONG OF SOLOMON -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_song_of_solomon_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> SONG OF SOLOMON -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    
    #PHRASE ISAIAH NONE NONE
    def phrase_isaiah(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ISAIAH ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_isaiah_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ISAIAH -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 23:
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
                        if int(every_line['Book Number']) == 23:
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

    def phrase_isaiah_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ISAIAH -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_isaiah_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> ISAIAH -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE JEREMIAH NONE NONE
    def phrase_jeremiah(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JEREMIAH ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_jeremiah_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JEREMIAH -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 24:
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
                        if int(every_line['Book Number']) == 24:
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

    def phrase_jeremiah_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JEREMIAH -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_jeremiah_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JEREMIAH -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE MATTHEW NONE NONE
    def phrase_matthew(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> MATTHEW ")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_matthew_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> MATTHEW -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 40:
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
                        if int(every_line['Book Number']) == 40:
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

    def phrase_matthew_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> MATTHEW -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_matthew_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> MATTHEW -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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


    #PHRASE MARK NONE NONE
    def phrase_mark(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> MARK")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_mark_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> MARK -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 41:
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
                        if int(every_line['Book Number']) == 41:
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

    def phrase_mark_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> MARK -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_mark_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> MARK -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    
    #PHRASE LUKE NONE NONE
    def phrase_luke(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> LUKE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_luke_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> LUKE -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 42:
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
                        if int(every_line['Book Number']) == 42:
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

    def phrase_luke_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> LUKE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_luke_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> LUKE -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    #PHRASE JOHN NONE NONE
    def phrase_john(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOHN")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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

    def phrase_john_case_sensitive(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOHN -> CASE SENSITIVE")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                        if int(every_line['Book Number']) == 43:
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
                        if int(every_line['Book Number']) == 43:
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

    def phrase_john_partial_match(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOHN -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.upper().strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶').upper():
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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

    def phrase_john_bible_cs_pm(self):
        print("")
        print("SEARCH CONDITIONS: ")
        print("PHRASE -> JOHN -> CASE SENSITIVE -> PARTIAL MATCH")
        print("")
        occurences_in_verse = 0
        number_of_verse = 0
        validate_item = []
        search_user_input = input("Enter the phrase that you want to find: ")
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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
                            
                            if search_user_input.strip() in every_line['Text'].strip(' ?;[]"<>.:,!‹›¶'):
                                occurences_in_verse += 1
                                if every_line['Verse ID'] not in validate_item:
                                    number_of_verse += 1
                                    validate_item.append(every_line['Verse ID'])
                                    print(every_line['Book Name'], every_line['Chapter'],":",every_line['Verse'])
                                    print(every_line['Text'])
                                        
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




phrase_words = Phrase()
