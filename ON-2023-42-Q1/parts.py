from enum import Flag


StackVowel=[] #string 100
StackConsonant=[] #string 100


VowelTop=0
ConsonantTop=0

def PushData(data):
    global StackVowel, VowelTop, StackConsonant, ConsonantTop
    if VowelTop==100:
        print("Stack Overflow")
    else:
        if data in "aeiou":
            StackVowel[VowelTop]=data
            VowelTop=VowelTop+1
        else:
            if ConsonantTop==100:
                print("Stack Overflow")
            else:
                StackConsonant[ConsonantTop]=data
                ConsonantTop=ConsonantTop+1

def ReadData():
    global StackVowel, VowelTop, StackConsonant, ConsonantTop
    try:
        File=open("Stack.txt", "r")
        for line in File:
            data=line.strip()
            PushData(data)
        File.close()
    except FileNotFoundError:
        print("File not found")


def PopVowel():
    global StackVowel, VowelTop, StackConsonant, ConsonantTop
    if VowelTop-1>=0:
        VowelTop=VowelTop-1
        popped=StackVowel[VowelTop]
        del StackVowel[-1]
        return popped
    else:
        return "No Data"

def PopConsonent():
    global StackVowel, VowelTop, StackConsonant, ConsonantTop
    if ConsonantTop-1>=0:
        ConsonantTop=ConsonantTop-1
        popped=StackConsonant[ConsonantTop]
        del StackConsonant[-1]
        return popped
    else:
        return "No Data"



VowelTop = 0
ConsonantTop = 0
ReadData()
Letters = ""
Flag = False

for x in range(0, 5):
    Flag = False
    while Flag == False:
        Choice = input("Vowel or Consonant: ").lower()
        if Choice == "vowel":
            DataAccessed = PopVowel()
            if DataAccessed != "No data":
                Letters = Letters + DataAccessed
                Flag = True
            else:
                print("No vowels left")
        elif Choice == "consonant":       
            DataAccessed = PopConsonent()
            if DataAccessed != "No data":
                Letters = Letters + DataAccessed
                Flag = True
            else:
                print("No consonants left")
        else:                             
            print("Invalid choice")

print(Letters)
