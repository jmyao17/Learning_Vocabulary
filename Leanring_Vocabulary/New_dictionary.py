# Hi, this is a program for creating a new vocabulary

from sys import argv
from pathlib import Path
import csv
import pandas as pd
import random

Words_List={}

def Starline():
    print("*******************************************************************")
def Starline_NL():
    print("*******************************************************************\n")

def Goodbye():
    print("I respect your choice. Hope to see you next time ^_^")

# load dictionary from the datebase
def Load_Dict(Filename):
    Dict={}
    df=pd.DataFrame()
    my_file=Path(Filename)
    if my_file.is_file():
        df=pd.read_csv(Filename,header=None)
        df.columns=['word','meaning']
        Starline()
        print("This is your dictionary (Only several headlines are shown)!  ")
        Starline()
        print(df.head())
        Starline_NL()
        for index,row in df.iterrows():
            key=row['word']
            val=row['meaning']
            Dict[key]=val
    else:
        print(f"The file {Filename} does not exist.")
    return Dict,df

# write new words into the dictionary and save them into the datebase
def Write_Dict(Filename,Dict):
    w=csv.writer(open(Filename,'w'))
    for key,val in Dict.items():
        w.writerow([key,val])

def Review_Dict(start,end,df):
    if(start > end):
        print("Error: start > end")
        exit(0)
    for item in range(start,end):
        Starline()
        print(f"{df.word[item]} -->" f"{df.meaning[item]}")
        Starline()
        if item == end-1:
            print("You reach the last word in the dictionary!")
            break
        More=input("Do you want to see more word? (Y/N)>")
        if More == 'N':
            break
        elif More == 'Y':
            print("Ok!")
        else:
            print("You should enter either Y or N.")


# load new dictionary
script,Filename = argv
print(f"Load dictionary from {Filename}")
Words_List,df=Load_Dict(Filename)

# enrich the dictionary by adding new words 
Enter_New_Word = input("Do you want to enter a new word into the dictionary?(Y/N)>") 
while Enter_New_Word =='Y':
    New_Word=input("Please enter the new word >")
    Meaning=input("Please enter the meaning of the word >")
    Words_List[New_Word]=Meaning
    print(f"A new word {New_Word} with the meaning: {Meaning} is added into the dictionary.")
    Enter_New_Word=input("Do you want to enter another new word?(Y/N)>")

# write words into dictionary file 
print("The newly added words are written back to the dictionary.")
Write_Dict(Filename,Words_List)
Num_Words=len(Words_List)
print(f"Congratulation! You have a new dictionary with {Num_Words} words totally.")

Starline_NL()

Review=input("Do you want to review all the words in your dictionary ? (Y/N)>")
if Review == 'Y' and Num_Words >=1:
    Review_Dict(0,Num_Words-1,df)
else:
    print("Good! I believe you made a smart choice!")

Goodbye()

#for key,value in my_dict.items():
