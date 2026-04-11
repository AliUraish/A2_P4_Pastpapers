

QueueData=["" for i in range(0, 20)]
StartPointer=0
EndPointer=0

def Enqueue(Data):
    global StartPointer
    global EndPointer
    if EndPointer==20:
        return False
    else:
        QueueData[EndPointer]=Data
        EndPointer=EndPointer+1
        return True 

def Readfile():
    global StartPointer
    global EndPointer
    global QueueData
    filename=input("Enter the filename")
    try:
        file=open(filename,"r")
        for line in file:
            data=line.strip
            result=Enqueue(data)
            if result==False:
                file.close()
                return 1
        file.close()
        return 2
    except FileNotFoundError:
        return -1


#main program
Readfile()
result=Readfile()
if result==-1:
    print("The text file could not be found")
elif result==1:
    print("The queue is full and not all data could be inserted")
else:
    print("All data is inserted")

def Remove():
    global StartPointer
    global EndPointer
    global QueueData
    if (EndPointer-StartPointer)<2:
        print("No Items")
    else:
        V1=QueueData[StartPointer]
        StartPointer=StartPointer+1
        V2=QueueData[StartPointer]
        StartPointer=StartPointer+1
        return(V1+V2)



        




