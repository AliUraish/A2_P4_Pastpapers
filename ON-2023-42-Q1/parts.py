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
