import csv
import random
from datetime import date
from br import BibleReading as b_read
from allwords import AllWords as aw
today = date.today()

with open('./csv-files/tagab.csv','r') as csv_tagalog_file:
            csv_tagalog_reader = csv.DictReader(csv_tagalog_file)
            selected_verses = ['23316','28752','28145','26712','29449','30170','29532','17022','11339','29747']
            random_verse = random.choice(selected_verses)
            for line in csv_tagalog_reader:
                if random_verse == line['Verse ID']:
                    print("")
                    print("VERSE OF THE DAY")
                    print(today.strftime("%B %d, %Y"))
                    print("")
                    print(line['Book Name'], line['Chapter'],":",line['Verse'])
                    print(line['Text'])

class MainHome():
    def __init__(self) -> None:
        pass
    

    def home(self):
        
        print("")
        print("--------------------------")
        print("WHAT WOULD YOU LIKE TO DO? ")
        print(f"[1] BIBLE READING")
        print(f"[2] SEARCH")
        print("[3] EXIT")
        print("")
        try:
            user_choice = int(input("Enter the number: "))
            print("--------------------------")
            if user_choice == 1:
                b_read.bible_reading(self)
                self.home()
            elif user_choice == 2:
                print("SELECT")
                # aw.all_words_entire_bible(self)
                # aw.all_words_entire_bible_case_sensitive(self)
                # aw.all_words_entire_bible_partial_match(self)
                # aw.all_words_entire_bible_cs_pm(self)
                # aw.all_words_numbers_case_sensitive(self)
                aw.all_words_numbers_partial_match(self)
                # aw.all_words_numbers_bible_cs_pm(self)
                # print("First Condition: [1]ALL WORDS [2]ANY WORDS [3]PHRASE")
                # first_con = int(input("Enter the number: "))
                # print("Second Condition: [1]ENTIRE BIBLE [2]OLD TESTAMENT [3]NEW TESTAMENT [4]SPECIFIC BOOK")
                # second_con = int(input("Enter the number: "))
                # print("***OPTIONAL CONDITIONS****")
                # print("[1] CASE SENSITIVE ONLY")
                # print("[2] PARTIAL MATCH ONLY")
                # print("[3] CASE SENSITIVE & PARTIAL MATCH")
                # print("[4] IT DOESN'T MATTER. SEARCH IT NOW!")
            elif user_choice == 3:
                print("")
                print("ARE YOU SURE YOU WANT TO EXIT?")
                print("[1] YES")
                print("[2] NO")
                try:
                    user_exit = int(input("Enter the number: "))
                    if user_exit == 1:
                        print("")
                        print("Exited")
                    elif user_exit == 2:
                        self.home()
                    else:
                        print(f"My Apologies, {user_exit} is invalid")
                except ValueError:
                    print("")
                    print("Whoops! be careful in typing")

            else:
                print("")
                print(f"Unfortunately, {user_choice} is invalid")
                
        except ValueError:
            print("")
            print("Oops! be careful in typing")
        

home_main = MainHome()
home_main.home()
