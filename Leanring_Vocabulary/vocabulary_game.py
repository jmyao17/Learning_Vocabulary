# This is a simple game for learning new vocabulary
# The basic idea of this game is following. 
# One can add a set of new words into the datebase
# and then guess the correct word based on the meaning
# provided on the screen.


import csv
import pandas as pd
import random

Num_Words=1
Words_List={}
New_Guess='Y'
global Num_Succ
global Num_Fail
Num_Succ=0
Num_Fail=0


def Starline():
    print("*******************************************************************")
def Starline_NL():
    print("*******************************************************************\n")

def Goodbye():
    print("I respect your choice. Hope to see you next time ^_^")

def score(NSucc,NFail):
    Total_Test=NSucc+NFail
    sco=NSucc*100/float(Total_Test)
    print(f"In the test, you tried {Total_Test} times, and your score is {sco}")

# load dictionary from the datebase
def Load_Dict(Filename):
    Dict={}
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

Words_List,df=Load_Dict("dic.csv")

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
Write_Dict("dic.csv",Words_List)
Num_Words=len(Words_List)
print(f"Congratulation! You have a new dictionary with {Num_Words} words totally.")

Starline_NL()

Review=input("Do you want to go through the words first? (Y/N)>")
if Review == 'Y':
    Review_Dict(0,Num_Words-1,df)
else:
    print("Good! I believe you made a smart choice!")



# take a test 
New_Guess=input("Do you want to take a test of vocabulary? (Y/N)>")
if New_Guess == 'N':
    Goodbye()
while New_Guess =='Y':
    idx=random.randint(0,Num_Words-1)
    idx_word=0
    for key,val in Words_List.items():
        if(idx_word == idx):
            first_letter=key[0]
            second_letter=key[1]
            print("Please guess the word which has the meaning:")
            Starline_NL()
            print(f"{val}." "\n")
            Starline_NL()
#            hint1=input("Do you need the first hint? (Y/N)>")
            hint1 = 'N'
            if hint1 == 'Y':
                print(f"The first letter is {first_letter}.")
#                hint2=input("Do you need the second hint? (Y/N)>")
                if hint2 == 'Y':
                    print(f"The second letter is {second_letter}.")
                    print("There is no further hint.\n")
                    guess=input(f"Please enter your answer here >")
                elif hint2 == 'N':
                    print("Yes! I believe you know it\n")
                    guess=input(f"Please enter your answer here >")
                else:
                    print("You should enter either Y or N.\n")
                    guess=input(f"Please enter your answer here >")
            elif hint1 == 'N':
                print("Yes! I believe you know it\n")
                guess=input(f"Please enter your answer here >")
            else:
                print("You should enter either Y or N.\n")
                guess=input(f"Please enter your answer here >")
            lower_guess = guess.lower()
            lower_key = key.lower()
            if(lower_guess == lower_key):
                New_Guess=input("Congratulation ^_^! Your guess is correct!" "\n" 
                            "Do you want to guess another word? (Y/N)>")
                Num_Succ += 1
                if(New_Guess == 'Y'):
                    print("Good! Please be ready for the next guess.")
                elif(New_Guess == 'N'):
                    score(Num_Succ,Num_Fail)
                    Goodbye() 
                    exit(0)
            else:
                Num_Fail += 1
                print("Sorry! Your guess is wrong. ")
                print(f"The correct answer is {key}." "\n")
                New_Guess=input("Do you want to try another test? (Y/N)>")
                if(New_Guess == 'Y'):
                    print("Good! Please be ready for the next guess.")
                if(New_Guess == 'N'):
                    score(Num_Succ,Num_Fail)
                    Goodbye()
                    exit(0)
        idx_word +=1
#Goodbye()
#print(Num_Succ)
#for key,value in my_dict.items():
