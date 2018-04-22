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

#Colors class:reset all colors with colors.reset; two sub classes fg for foreground and bg for background; use as colors.subclass.colorname.
#i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable, 
#underline, reverse, strike through, and invisible work with the main class i.e. colors.bold

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def Dashline():
    print("---------------------------------------------------------------------------------------------------------")
def Starline():
    print("*********************************************************************************************************")
def Starline_NL():
    print("*********************************************************************************************************\n")

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


def Get_Key_Val(Words_List,idx):
    idx_word=0
    for key,val in Words_List.items():
        if(idx_word == idx):
            word=key
            meaning=val
            break
        else:
            idx_word += 1
    return word,meaning
            

def Option(label,key):
    print(f"{label}: {key}")



# Test program

def Test(Dict,df):
    Num_Words=len(Dict)
    NSucc=0
    NFail=0
    # get the indices for the words 
    id_test=random.randint(0,Num_Words-1)
    id_1=random.randint(0,Num_Words-1)
    id_2=random.randint(0,Num_Words-1)
    id_3=random.randint(0,Num_Words-1)
    while id_1 == id_test:
        id_1=random.randint(0,Num_Words-1)

    while id_2 == id_test or id_2 == id_1:
        id_2=random.randint(0,Num_Words-1)

    while id_3 == id_test or id_3 == id_1 or id_3 == id_2:
        id_3=random.randint(0,Num_Words-1)

    
    
    Key,Val=Get_Key_Val(Dict,id_test)
    Key1,Val1=Get_Key_Val(Dict,id_1)
    Key2,Val2=Get_Key_Val(Dict,id_2)
    Key3,Val3=Get_Key_Val(Dict,id_3)

    # start to test
    print(colors.fg.blue,"Please choose the correct word which has the following meaning:" "\n \n")
    print(colors.fg.red, "--> {}".format(Val))
    Dashline()
    print(colors.fg.black)

    ABCD=['A','B','C','D']

    id_A=random.randint(0,3)
    id_B=random.randint(0,3)
    id_C=random.randint(0,3)
    id_D=random.randint(0,3)
    while id_B == id_A:
        id_B=random.randint(0,3)
    while id_C == id_A or id_C == id_B:
        id_C=random.randint(0,3)
    while id_D == id_A or id_D == id_B or id_D == id_C:
        id_D=random.randint(0,3)

#  id_A is the correct answer
    Set={}
    Set[ABCD[id_A]]=Key
    Set[ABCD[id_B]]=Key1
    Set[ABCD[id_C]]=Key2
    Set[ABCD[id_D]]=Key3

    print('A:', Set['A']) 
    print('B:', Set['B']) 
    print('C:', Set['C']) 
    print('D:', Set['D']) 

    reply=input("Enter (A/B/C/D) >")

    if reply == ABCD[id_A] or reply == ABCD[id_A].lower():
        NSucc +=1
        print("Correct!")
    else:
        NFail +=1
        print(f"Wrong! The correct answer is {ABCD[id_A]}")

    return NSucc,NFail
#print(f"Key_test={Key}, Val_test={Val}")

def Main():
    # initialization
    Num_Succ=0
    Num_Fail=0
    # load dictionary
    Dict,df=Load_Dict("dic.csv")
    Num_Test = 0 
    New_Test='Y'
    while New_Test == 'Y' and Num_Test <10:
        Starline_NL()
        # start to test
        NSucc = 0
        NFail = 0

        NSucc,NFail=Test(Dict,df)
        Num_Test += 1
        Num_Succ +=NSucc
        Num_Fail +=NFail
        if(Num_Test == 10):
            New_Test = input("You have tried 10 tests. Do you want to continue the test? (Y/N)")
            if(New_Test == 'Y'):
                Num_Test = 0
            else:
                print(f"# of correct answers:{Num_Succ}; # of wrong answers: {Num_Fail}.")
                score(Num_Succ,Num_Fail)
# 
Main()
