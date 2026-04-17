ArrayNodes=[[0 for x in range(3)] for y in range(20)]
RootPointer=-1
FreeNode=0


def AddNode(RootPointer, FreeNode, ArrayNodes):
    NodeData=int(input("Enter the data"))
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=0
        else:
            placed=False
            CurrentNode=RootPointer
            while placed==False:
                if NodeData<ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0]==-1:
                        ArrayNodes[CurrentNode][0]=FreeNode
                        placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2]==-1:
                        ArrayNodes[CurrentNode][2]=FreeNode
                        placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][2]
        FreeNode+=1
    else:
        print("Binary Tree is full")
    return ArrayNodes, RootPointer, FreeNode


def PrintAll():
    global RootPointer, ArrayNodes, FreeNode
    for i in range(FreeNode):
        print(str(ArrayNodes[i][0])+" ", str(ArrayNodes[i][1])+" ", str(ArrayNodes[i][2]))

def InOrder(RootPointer, ArrayNodes):
    if ArrayNodes[RootPointer][0]!=-1:
        InOrder(ArrayNodes[RootPointer][0], ArrayNodes)
    print(str(ArrayNodes[RootPointer][1]))
    if ArrayNodes[RootPointer][2]!=-1:
        InOrder(ArrayNodes[RootPointer][2], ArrayNodes)
    


for i in range(10):
    
    ArrayNodes, RootPointer, FreeNode=AddNode(RootPointer, FreeNode, ArrayNodes)
PrintAll()

InOrder(RootPointer, ArrayNodes)
