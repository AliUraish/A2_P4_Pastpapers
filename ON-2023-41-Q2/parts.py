Queue=["" for i in range(51)]
HeadPointer=-1
TailPointer=0

def Enqueue(Record):
    global TailPointer, Queue, HeadPointer
    if TailPointer==50:
        print("Queue is full")
    else:
        Queue[TailPointer]=Record
        TailPointer+=1
        if HeadPointer==-1:
            HeadPointer=0


def Dequeue():
    global TailPointer, Queue, HeadPointer
    if HeadPointer==0 or HeadPointer==TailPointer:
        print("Queue is empty")
        return "Empty"
    else:
        HeadPointer+=1
        return Queue[HeadPointer-1]
    
def ReadData():
    global TailPointer, Queue, HeadPointer
    try :
        ID=open("QueueData.txt", "r")
        for line in ID:
            Record=line.split(",")
            Enqueue(Record)
        ID.close()
    except FileNotFoundError:
        print("File not found")

class RecordData:
    def __init__(self, IDp, Totalp):
        self._ID=IDp
        self._Total=Totalp

    def SetID(self, Value):
        self._ID=Value
    def GetID(self):
        return self._ID
    def SetTotal(self, Value):
        self._Total=Value
    def GetTotal(self):
        return self._Total
    

Records=[] #50 elements of type RecordData
NumberofRecords=0

def TotalData():
    global TailPointer, Queue, HeadPointer, Records, NumberofRecords
    DataAccessed=Dequeue()
    Flag=False
    if NumberofRecords==0:
        Records[NumberofRecords].ID=DataAccessed
        Records[NumberofRecords].Total=1
        Flag=True
        NumberofRecords+=1
    else:
        for x in range(0,NumberofRecords-1):
            if Records[x].ID==DataAccessed:
                Records[x].Total+=1
                Flag=True
                break
        if Flag==False:
            Records[NumberofRecords].ID=DataAccessed
            Records[NumberofRecords].Total=1
            NumberofRecords+=1

def OutputRecords():
    global TailPointer, Queue, HeadPointer, Records, NumberofRecords
    for x in range(0, NumberofRecords):
        print("ID", Records[x].GetID(), "Total", Records[x].GetTotal())

#main program
ReadData()
while TailPointer!=HeadPointer:
    TotalData()
OutputRecords()