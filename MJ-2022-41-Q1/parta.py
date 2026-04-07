FileData=[[0] * 2 for i in range(11)]

def ReadHighScores():
    global FileData
    try:
        File=open("HighScores.txt", "r")
        for line in File:
            Data=line.split()
            FileData[int(Data[0])][0]=int(Data[1])
            FileData[int(Data[0])][1]=Data[2]
        File.close()
    except FileNotFoundError:
        print("File not found")

def OutputHighScores():
    global FileData
    for i in range(11):
        print(FileData[i][0], FileData[i][1])
    
ReadHighScores()
OutputHighScores()



name=input("Enter a name: ")
while len(name)!=3:
    print("Invalid input")
    name=input("Enter a name: ")

score=int(input("Enter a score: "))
while score<1 or score>100000:
    print("Invalid input")
    score=int(input("Enter a score: "))


def ArrangeHighScores(name, score):
    global FileData
    for i in range(0, 10):
        if score>FileData[i][1]:
            Temp1=FileData[i][0]
            Temp2=FileData[i][1]
            FileData[i][0]=name
            FileData[i][1]=score
            count=i+1
            while(count<10):
                secondname=FileData[count][0]
                secondscore=FileData[count][1]
                FileData[count][0]=Temp1
                FileData[count][1]=Temp2
                Temp1=secondname
                Temp2=secondscore
                count=count+1
            break      

