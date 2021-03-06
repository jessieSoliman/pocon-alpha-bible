#ALPHA BIBLE v1.0
#THIS WAS MADE BY PRINCESS EVANGELINE POCON BSIS-2
#PROJECT IN DATA STRUCTURES AND ALGORITHMS
#Note: the code was still messy because i am still learning python and this is my first time working with modules :'))
#I know that my algorithm is not too efficient :')). 
#I have also tried making a GUI but it was really hard but I would love to do it in the future.


import csv
from os import pardir
import random
from datetime import date
from typing import Optional
from br import BibleReading as b_read
from allwords import AllWords as aw
from anywords import AnyWords as anw
from phrase import Phrase as p
today = date.today()

print("ALPHA BIBLE v1.0")
print("Created by: Princess Evangeline Pocon")
print("")
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
                
                print(f"My Apologies, {self.first_con} is invalid")
                self.home()
        
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
        print("")
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
            #all words entire bible
            if self.first_con == 1 and self.second_con == 1:
                self.third_condition()
                if self.optional_condition == 4:
                    aw.all_words_entire_bible(self)
                    self.home()
                elif self.optional_condition == 1:
                    aw.all_words_entire_bible_case_sensitive(self)
                    self.home()
                elif self.optional_condition == 2:
                    aw.all_words_entire_bible_partial_match(self)
                    self.home()
                elif self.optional_condition == 3:
                    aw.all_words_entire_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            #any words entire bible
            elif self.first_con == 2 and self.second_con == 1:
                self.third_condition()
                if self.optional_condition == 4:
                    anw.any_words_entire_bible(self)
                    self.home()
                elif self.optional_condition == 1:
                    anw.any_words_entire_bible_case_sensitive(self)
                    self.home()
                elif self.optional_condition == 2:
                    anw.any_words_entire_bible_partial_match(self)
                    self.home()
                elif self.optional_condition == 3:
                    anw.any_words_entire_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            #phrase entire bible
            elif self.first_con == 3 and self.second_con == 1:
                self.third_condition()
                if self.optional_condition == 4:
                    # p.phrase_entire_bible(self)
                    print("Something went wrong.. Unfortunately, this feature is under maintainance")
                    self.home()
                elif self.optional_condition == 1:
                    # p.phrase_entire_bible_case_sensitive(self)
                    print("Something went wrong.. Unfortunately, this feature is under maintainance")
                    self.home()
                elif self.optional_condition == 2:
                    p.phrase_entire_bible_partial_match(self)
                    self.home()
                elif self.optional_condition == 3:
                    p.phrase_entire_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            #all words old testament
            elif self.second_con== 2 and self.first_con == 1:
                self.third_condition()
                if self.optional_condition == 4:
                    aw.all_words_old_testament(self)
                    self.home()
                elif self.optional_condition == 1:
                    aw.all_words_old_testament_case_sensitive(self)
                    self.home()
                elif self.optional_condition == 2:
                    aw.all_words_old_testament_partial_match(self)
                    self.home()
                elif self.optional_condition == 3:
                    aw.all_words_old_testament_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            #phrase old testament
            elif self.second_con== 2 and self.first_con == 3:
                self.third_condition()
                if self.optional_condition == 4:
                    # p.phrase_old_testament(self)
                    print("Something went wrong.. Unfortunately, this feature is under maintainance")
                    self.home()
                elif self.optional_condition == 1:
                    # p.phrase_old_testament_case_sensitive(self)
                    print("Something went wrong.. Unfortunately, this feature is under maintainance")
                    self.home()
                elif self.optional_condition == 2:
                    p.phrase_old_testament_partial_match(self)
                   
                    self.home()
                elif self.optional_condition == 3:
                    p.phrase_old_testament_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            #any words old testament
            elif self.second_con== 2 and self.first_con == 2:
                self.third_condition()
                if self.optional_condition == 4:
                    anw.any_words_old_testament(self)
                    self.home()
                elif self.optional_condition == 1:
                    anw.any_words_old_testament_case_sensitive(self)
                    self.home()
                elif self.optional_condition == 2:
                    anw.any_words_old_testament_partial_match(self)
                    self.home()
                elif self.optional_condition == 3:
                    anw.any_words_old_testament_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            #all words new testament
            elif self.second_con == 3 and self.first_con == 1:
                self.third_condition()
                if self.optional_condition == 4:
                    aw.all_words_new_testament(self)
                    self.home()
                elif self.optional_condition == 1:
                    aw.all_words_new_testament_case_sensitive(self)
                    self.home()
                elif self.optional_condition == 2:
                    aw.all_words_new_testament_partial_match(self)
                    self.home()
                elif self.optional_condition == 3:
                    aw.all_words_new_testament_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            #any words new testament
            elif self.second_con == 3 and self.first_con == 2:
                self.third_condition()
                if self.optional_condition == 4:
                    anw.any_words_new_testament(self)
                    self.home()
                elif self.optional_condition == 1:
                    anw.any_words_new_testament_case_sensitive(self)
                    self.home()
                elif self.optional_condition == 2:
                    anw.any_words_new_testament_partial_match(self)
                    self.home()
                elif self.optional_condition == 3:
                    anw.any_words_new_testament_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            #phrase new testament
            elif self.second_con == 3 and self.first_con == 3:
                self.third_condition()
                if self.optional_condition == 4:
                    # p.phrase_new_testament(self)
                    print("Something went wrong.. Unfortunately, this feature is under maintainance")
                    self.home()
                elif self.optional_condition == 1:
                    # p.phrase_new_testament_case_sensitive(self)
                    print("Something went wrong.. Unfortunately, this feature is under maintainance")
                    self.home()
                elif self.optional_condition == 2:
                    p.phrase_new_testament_partial_match(self)
                    self.home()
                elif self.optional_condition == 3:
                    p.phrase_new_testament_bible_cs_pm(self)
                    self.home()
                else:
                    print(f"Im Sorry, {self.optional_condition} is not on the choices")
                    self.home()
            elif self.second_con == 4:
                print("")
                print("OLD TESTAMENT")
                print("")
                print("[1]Genesis   [2]Exodus  [3]Leviticus  [4]Numbers  [5]Deuteronomy  [6]Joshua  [7]Judges [8]Ruth  [9]1 Samuel  [10]2 Samuel")
                print("[11]1 Kings  [12]2 Kings   [13]1 Chronicles   [14]2 Chronicles [15]Ezra  [16]Nehemiah  [17]Esther  [18]Job  [19]Psalms  [20]Proverbs  ")
                print("[21]Ecclesiastes  [22]Song of Solomon  [23]Isaiah  [24]Jeremiah  ")
                print("")
                print("NEW TESTAMENT")
                print("")
                print("[40]Matthew  [41]Mark  [42]Luke  [43]John ")
                
                print("")
                print("NOTE: Currently, These are the  books that are available for searching but we are working to complete the 66 books!")
                print("")
                try:
                    self.specific_bible = int(input("Enter the number: "))
                    #Genesis
                    if self.specific_bible == 1 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_genesis(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_genesis_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_genesis_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_genesis_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Exodus
                    elif self.specific_bible == 2 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_exodus(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_exodus_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_exodus_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_exodus_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Leviticus
                    elif self.specific_bible == 3 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_leviticus(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_leviticus_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_leviticus_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_leviticus_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Numbers
                    elif self.specific_bible == 4 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_numbers(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_numbers_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_numbers_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_numbers_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Deuteronomy
                    elif self.specific_bible == 5 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_deuteronomy(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_deuteronomy_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_deuteronomy_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_deuteronomy_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Joshua
                    elif self.specific_bible == 6 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_joshua(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_joshua_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_joshua_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_joshua_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Judges
                    elif self.specific_bible == 7 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_judges(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_judges_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_judges_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_judges_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ruth
                    elif self.specific_bible == 8 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_ruth(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_ruth_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_ruth_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_ruth_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Samuel
                    elif self.specific_bible == 9 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_1samuel(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_1samuel_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_1samuel_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_1samuel_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Samuel
                    elif self.specific_bible == 10 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_2samuel(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_2samuel_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_2samuel_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_2samuel_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Kings
                    elif self.specific_bible == 11 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_1kings(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_1kings_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_1kings_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_1kings_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Kings
                    elif self.specific_bible == 12 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_2kings(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_2kings_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_2kings_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_2kings_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Chronicles
                    elif self.specific_bible == 13 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_1chronicles(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_1chronicles_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_1chronicles_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_1chronicles_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Chronicles
                    elif self.specific_bible == 14 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_2chronicles(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_2chronicles_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_2chronicles_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_2chronicles_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ezra
                    elif self.specific_bible == 15 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_ezra(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_ezra_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_ezra_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_ezra_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Nehemiah
                    elif self.specific_bible == 16 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_nehemiah(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_nehemiah_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_nehemiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_nehemiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Esther
                    elif self.specific_bible == 17 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_esther(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_esther_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_esther_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_esther_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Job
                    elif self.specific_bible == 18 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_job(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_job_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_job_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_job_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Psalms
                    elif self.specific_bible == 19 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_psalms(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_psalms_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_psalms_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_psalms_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Proverbs
                    elif self.specific_bible == 20 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_proverbs(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_proverbs_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_proverbs_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_proverbs_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ecclesiastes
                    elif self.specific_bible == 21 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_ecclesiastes(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_ecclesiastes_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_ecclesiastes_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_ecclesiastes_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Song of Solomon
                    elif self.specific_bible == 22 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_song_of_solomon(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_song_of_solomon_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_song_of_solomon_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_song_of_solomon_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Isaiah
                    elif self.specific_bible == 23 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_isaiah(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_isaiah_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_isaiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_isaiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Jeremiah
                    elif self.specific_bible == 24 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_jeremiah(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_jeremiah_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_jeremiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_jeremiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #NEW TESTAMENT

                    #Matthew
                    elif self.specific_bible == 40 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_matthew(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_matthew_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_matthew_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_matthew_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Mark
                    elif self.specific_bible == 41 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_mark(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_mark_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_mark_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_mark_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #Luke
                    elif self.specific_bible == 42 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_luke(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_luke_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_luke_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_luke_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #John
                    elif self.specific_bible == 43 and self.first_con == 1:
                        self.third_condition()
                        if self.optional_condition == 4:
                            aw.all_words_john(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            aw.all_words_john_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            aw.all_words_john_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_john_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #ANY WORDS

                    #Genesis
                    elif self.specific_bible == 1 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_genesis(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_genesis_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_genesis_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_genesis_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Exodus
                    elif self.specific_bible == 2 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_exodus(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_exodus_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_exodus_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_exodus_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Leviticus
                    elif self.specific_bible == 3 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_leviticus(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_leviticus_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_leviticus_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_leviticus_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Numbers
                    elif self.specific_bible == 4 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_numbers(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_numbers_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_numbers_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_numbers_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Deuteronomy
                    elif self.specific_bible == 5 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_deuteronomy(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_deuteronomy_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_deuteronomy_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_deuteronomy_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Joshua
                    elif self.specific_bible == 6 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_joshua(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_joshua_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_joshua_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_joshua_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Judges
                    elif self.specific_bible == 7 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_judges(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_judges_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_judges_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_judges_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ruth
                    elif self.specific_bible == 8 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_ruth(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_ruth_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_ruth_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_ruth_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Samuel
                    elif self.specific_bible == 9 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_1samuel(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_1samuel_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_1samuel_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_1samuel_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Samuel
                    elif self.specific_bible == 10 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_2samuel(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_2samuel_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_2samuel_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_2samuel_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Kings
                    elif self.specific_bible == 11 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_1kings(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_1kings_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_1kings_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_1kings_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Kings
                    elif self.specific_bible == 12 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_2kings(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_2kings_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_2kings_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_2kings_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Chronicles
                    elif self.specific_bible == 13 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_1chronicles(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_1chronicles_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_1chronicles_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_1chronicles_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Chronicles
                    elif self.specific_bible == 14 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_2chronicles(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_2chronicles_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_2chronicles_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_2chronicles_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ezra
                    elif self.specific_bible == 15 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_ezra(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_ezra_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_ezra_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_ezra_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Nehemiah
                    elif self.specific_bible == 16 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_nehemiah(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_nehemiah_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_nehemiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_nehemiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Esther
                    elif self.specific_bible == 17 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_esther(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_esther_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_esther_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_esther_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Job
                    elif self.specific_bible == 18 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_job(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_job_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_job_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_job_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Psalms
                    elif self.specific_bible == 19 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_psalms(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_psalms_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_psalms_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_psalms_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Proverbs
                    elif self.specific_bible == 20 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_proverbs(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_proverbs_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_proverbs_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_proverbs_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ecclesiastes
                    elif self.specific_bible == 21 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_ecclesiastes(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_ecclesiastes_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_ecclesiastes_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_ecclesiastes_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Song of Solomon
                    elif self.specific_bible == 22 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_song_of_solomon(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_song_of_solomon_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_song_of_solomon_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_song_of_solomon_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Isaiah
                    elif self.specific_bible == 23 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_isaiah(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_isaiah_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_isaiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_isaiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Jeremiah
                    elif self.specific_bible == 24 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_jeremiah(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_jeremiah_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_jeremiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_jeremiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #NEW TESTAMENT

                    #Matthew
                    elif self.specific_bible == 40 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_matthew(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_matthew_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_matthew_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_matthew_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Mark
                    elif self.specific_bible == 41 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_mark(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_mark_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_mark_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_mark_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #Luke
                    elif self.specific_bible == 42 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_luke(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_luke_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_luke_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_luke_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #John
                    elif self.specific_bible == 43 and self.first_con == 2:
                        self.third_condition()
                        if self.optional_condition == 4:
                            anw.any_words_john(self)
                            self.home()
                        elif self.optional_condition ==  1:
                            anw.any_words_john_case_sensitive(self)
                            self.home()
                        elif self.optional_condition ==  2:
                            anw.any_words_john_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            anw.any_words_john_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    
                    #PHRASE

                    #Genesis
                    elif self.specific_bible == 1 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            # p.phrase_genesis(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            # p.phrase_genesis_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_genesis_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_genesis_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Exodus
                    elif self.specific_bible == 2 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            # p.phrase_exodus(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            # p.phrase_exodus_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_exodus_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_exodus_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Leviticus
                    elif self.specific_bible == 3 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            # p.phrase_leviticus(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            # p.phrase_leviticus_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_leviticus_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_leviticus_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Numbers
                    elif self.specific_bible == 4 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            # p.phrase_numbers(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            # p.phrase_numbers_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_numbers_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_numbers_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Deuteronomy
                    elif self.specific_bible == 5 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            # p.phrase_deuteronomy(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            # p.phrase_deuteronomy_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_deuteronomy_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_deuteronomy_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Joshua
                    elif self.specific_bible == 6 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            # p.phrase_joshua(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            # p.phrase_joshua_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_joshua_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_joshua_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Judges
                    elif self.specific_bible == 7 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            # p.phrase_judges(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            # p.phrase_judges_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_judges_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_judges_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ruth
                    elif self.specific_bible == 8 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            # p.phrase_ruth(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_ruth_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_ruth_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_ruth_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Samuel
                    elif self.specific_bible == 9 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_1samuel(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_1samuel_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_1samuel_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_1samuel_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Samuel
                    elif self.specific_bible == 10 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_2samuel(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_2samuel_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_2samuel_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_2samuel_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Kings
                    elif self.specific_bible == 11 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_1kings(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_1kings_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_1kings_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_1kings_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Kings
                    elif self.specific_bible == 12 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_2kings(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_2kings_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_2kings_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_2kings_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #1 Chronicles
                    elif self.specific_bible == 13 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_1chronicles(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_1chronicles_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_1chronicles_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_1chronicles_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #2 Chronicles
                    elif self.specific_bible == 14 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_2chronicles(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_2chronicles_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_2chronicles_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_2chronicles_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ezra
                    elif self.specific_bible == 15 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_ezra(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_ezra_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_ezra_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_ezra_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Nehemiah
                    elif self.specific_bible == 16 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_nehemiah(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_nehemiah_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_nehemiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_nehemiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Esther
                    elif self.specific_bible == 17 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_esther(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_esther_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_esther_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_esther_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Job
                    elif self.specific_bible == 18 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_job(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_job_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_job_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_job_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Psalms
                    elif self.specific_bible == 19 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_psalms(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_psalms_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_psalms_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_psalms_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Proverbs
                    elif self.specific_bible == 20 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_proverbs(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_proverbs_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_proverbs_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_proverbs_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Ecclesiastes
                    elif self.specific_bible == 21 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_ecclesiastes(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_ecclesiastes_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_ecclesiastes_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_ecclesiastes_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Song of Solomon
                    elif self.specific_bible == 22 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_song_of_solomon(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            # p.phrase_song_of_solomon_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_song_of_solomon_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_song_of_solomon_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Isaiah
                    elif self.specific_bible == 23 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_isaiah(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_isaiah_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_isaiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_isaiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Jeremiah
                    elif self.specific_bible == 24 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_jeremiah(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_jeremiah_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_jeremiah_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_jeremiah_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #NEW TESTAMENT

                    #Matthew
                    elif self.specific_bible == 40 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_matthew(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_matthew_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_matthew_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_matthew_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()
                    #Mark
                    elif self.specific_bible == 41 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_mark(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_mark_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_mark_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            aw.all_words_mark_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #Luke
                    elif self.specific_bible == 42 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_luke(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_luke_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_luke_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_luke_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()

                    #John
                    elif self.specific_bible == 43 and self.first_con == 3:
                        self.third_condition()
                        if self.optional_condition == 4:
                            #p.phrase_john(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  1:
                            #p.phrase_john_case_sensitive(self)
                            print("Something went wrong.. Unfortunately, this feature is under maintainance")
                            self.home()
                        elif self.optional_condition ==  2:
                            p.phrase_john_partial_match(self)
                            self.home()
                        elif self.optional_condition ==  3:
                            p.phrase_john_bible_cs_pm(self)
                            self.home()
                        else:
                            print(f"{self.optional_condition} is not on the list")
                            self.home()








                             
                    else:
                        print(f"My Apologies, {self.specific_bible} is invalid")
                        self.home()
                except ValueError:
                    print("")
                    print("Ohh no! please be careful")
            else:
                print(f"We're sorry to inform you that {self.second_con} is invalid")
                self.home()
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
                        self.home()
                except ValueError:
                    print("")
                    print("Whoops! be careful in typing")

            else:
                print("")
                print(f"Unfortunately, {user_choice} is invalid")
                self.home()
                
        except ValueError:
            print("")
            print("Oops! be careful in typing")
        

home_main = MainHome()
home_main.home()
