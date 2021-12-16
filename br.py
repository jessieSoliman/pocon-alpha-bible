import csv 
class BibleReading:
    def __init__(self) -> None:
        pass


    def bible_reading(self):

            print("")
            print("OLD TESTAMENT")
            print("")
            print("Genesis   Exodus  Leviticus  Numbers  Deuteronomy  Joshua  Judges Ruth  1 Samuel  2 Samuel")
            print("1 Kings  2 Kings   1 Chronicles   2 Chronicles Ezra  Nehemiah  Esther  Job  Psalms  Proverbs  ")
            print("Ecclesiastes  Song of Solomon  Isaiah  Jeremiah  Lamentations  Ezekiel Daniel  Hosea  Joel  Amos")
            print("Obadiah  Jonah  Micah  Nahum  Habakkuk  Zephaniah  Haggai  Zechariah  Malachi")
            print("")
            print("NEW TESTAMENT")
            print("")
            print("Matthew  Mark  Luke  John  Acts  Romans  1 Corinthians  2 Corinthians  Galatians  Ephesians  ")
            print("Philippians  Colossians  1 Thessalonians  2 Thessalonians  1 Timothy  2 Timothy  Titus  Philemon  Hebrews  James")
            print("1 Peter  2 Peter  1 John  2 John  3 John  Jude  Revelation")
            print("")

            book_in = input("What book? : ")
            chap_in = input("What chapter: ")
            print("")
            print("----CHOOSE BIBLE VERSION-----")
            print("[1] ANG DATING BIBLIA")
            print("[2] AUTHORIZED KING JAMES VERSION")
            print("[3] AMERICAN STANDARD VERSION") 
            print("")
            try:
                bible_version = int(input("Enter the number:"))
                print("")
                if bible_version == 1:
                    with open('./csv-files/tagab.csv','r') as self.csv_tagalog_file:
                        self.csv_tagalog_reader = csv.DictReader(self.csv_tagalog_file)
                        for row in self.csv_tagalog_reader:
                            
                            if row['Book Name'].upper() == book_in.upper() and row['Chapter'] == chap_in:
                                print(f"{row['Verse']}  {row['Text']}")
                            else:
                                continue
                        
                elif bible_version == 2:
                    with open('./csv-files/kjv.csv','r') as csv_king_james_file:
                        csv_king_james_reader = csv.DictReader(csv_king_james_file)
                        for row in csv_king_james_reader:
                            if row['Book Name'].upper() == book_in.upper() and row['Chapter'] == chap_in:
                                print(f"{row['Verse']}  {row['Text']}")
                            else:
                                continue
                elif bible_version == 3:
                    with open('./csv-files/asv.csv','r') as csv_asv_file:
                        csv_asv_reader = csv.DictReader(csv_asv_file)
                        for row in csv_asv_reader:
                            if row['Book Name'].upper() == book_in.upper() and row['Chapter'] == chap_in:
                                print(f"{row['Verse']}  {row['Text']}")
                            else:
                                continue
                else:
                    print(f"My Apologies, {bible_version} is invalid")
            except ValueError:
                print("")
                print("Oops! be careful in typing")



bible_read = BibleReading()



