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

