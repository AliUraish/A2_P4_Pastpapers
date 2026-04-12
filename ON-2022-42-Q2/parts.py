class SaleData:
    def __init__(self,SaleIDp, Quantityp):
        self.ID=SaleIDp
        self.Quantity=Quantityp

CircularQueue=[]
Head=0
Tail=0
NumberofItems=0

def Enqueue(Record):
    global Tail, NumberofItems, CircularQueue, Head
    if NumberofItems==5:
        return -1
    else:
        CircularQueue[Tail]=Record
        if Tail==4:
            Tail=0
        else:
            Tail+=1
        NumberofItems+=1
        return 1
    
def Dequeue():
    global Tail, NumberofItems, CircularQueue, Head
    if NumberofItems==0:
        return -1
    else:
        Record=CircularQueue[Head]
        if Head==4:
            Head=0
        else:
            Head=+1
        NumberofItems-=1
        return Record
    
def EnterRecord():
    SaleID=int(input("Enter Sale ID: "))
    Quantity=int(input("Enter Quantity:"))
    Record=SaleData(SaleID, Quantity)
    Result=Enqueue(Record)
    if Result==-1:
        print("Queue is full")
    else:
        print("Record added successfully")


#main program
for i in range(5):
    EnterRecord()
Return=Dequeue()
if Return==-1:
    print("Queue is empty")
else:
    print("SaleID", Return.ID)
EnterRecord()
for i in range(5):
    print("SaleID", CircularQueue[i].ID, "Quantity", CircularQueue[i].Quantity)