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
    
    def first_condition(self):
        print("")
        print("------------------SEARCH SELECTION------------------")
        print("")
        print("First Condition: [1]ALL WORDS [2]ANY WORDS [3]PHRASE")
        print("")
        try:
            self.first_con = int(input("Enter the number: "))
            if self.first_con >= 1 and self.first_con <4:
                self.second_condition()
            else:
                pass
                # print(f"My Apologies, {self.first_con} is invalid")
        
        except ValueError:
            print("")
            print("Oops! be careful in typing")

    def third_condition(self):
        print("")
        print("***OPTIONAL CONDITIONS****")
        print("[1] CASE SENSITIVE ONLY")
        print("[2] PARTIAL MATCH ONLY")
        print("[3] CASE SENSITIVE & PARTIAL MATCH")
        print("[4] IT DOESN'T MATTER. SEARCH IT NOW!")
        try:
            self.optional_condition = int(input("Enter the number: "))
        except ValueError:
            print("")
            print("whoops! be careful in typing")

    def second_condition(self):
        print("")
        print("Second Condition: [1]ENTIRE BIBLE [2]OLD TESTAMENT [3]NEW TESTAMENT [4]SPECIFIC BOOK")
        print("")
        try:
            self.second_con = int(input("Enter the number: "))
            if self.first_con == 1 and self.second_con == 1:
                self.third_condition()
                if self.optional_condition == 4:
                    #dito na tatawagin yung function
                    aw.all_words_entire_bible(self)
            if self.second_con== 2:
                pass
            elif self.second_con == 3:
                pass
            elif self.second_con == 4:
                print("")
                print("OLD TESTAMENT")
                print("")
                print("[1]Genesis   [2]Exodus  [3]Leviticus  [4]Numbers  [5]Deuteronomy  [6]Joshua  [7]Judges [8]Ruth  [9]1 Samuel  [10]2 Samuel")
                print("[11]1 Kings  [12]2 Kings   [13]1 Chronicles   [14]2 Chronicles [15]Ezra  [16]Nehemiah  [17]Esther  [18]Job  [19]Psalms  [20]Proverbs  ")
                print("[21]Ecclesiastes  [22]Song of Solomon  [23]Isaiah  [24]Jeremiah  [25]Lamentations  [26]Ezekiel [27]Daniel  [28]Hosea  [29]Joel  [30]Amos")
                print("[31]Obadiah  [32]Jonah  [33]Micah  [34]Nahum  [35]Habakkuk  [36]Zephaniah  [37]Haggai  [38]Zechariah  [39]Malachi")
                print("")
                print("NEW TESTAMENT")
                print("")
                print("[40]Matthew  [41]Mark  [42]Luke  [43]John  [44]Acts  [45]Romans  [46]1 Corinthians  [47]2 Corinthians  [48]Galatians  [49]Ephesians  ")
                print("[50]Philippians  [51]Colossians  [52]1 Thessalonians  [53]2 Thessalonians  [54]1 Timothy  [55]2 Timothy  [56]Titus  [57]Philemon  [58]Hebrews  [59]James")
                print("[60]1 Peter  [61]2 Peter  [62]1 John  [63]2 John  [64]3 John  [65]Jude  [66]Revelation")
                print("")
                specific_bible = int(input("Enter the number: "))
                if specific_bible == 1 and self.first_con == 1:
                    self.third_condition()
                    if self.optional_condition == 4:
                        aw.all_words_genesis(self)
                    elif self.optional_condition ==  1:
                        aw.all_words_genesis_case_sensitive(self)
                    elif self.optional_condition ==  2:
                        aw.all_words_genesis_partial_match(self)
                    elif self.optional_condition ==  3:
                        aw.all_words_genesis_bible_cs_pm(self)
                    else:
                        pass
                elif specific_bible == 2 and self.first_con == 1:
                    pass
                else:
                    pass
            else:
                pass
                # print(f"My Apologie, {self.second_con} is invalid")
        
        except ValueError:
            print("")
            print("Oops! be careful in typing")

        


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
                self.first_condition()
                
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
