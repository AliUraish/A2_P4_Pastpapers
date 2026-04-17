def SearchValue(Root, ValueToFind):
    global ArrayNodes
    if Root==-1:
        return -1
    elif ArrayNodes[Root][1]==ValueToFind:
            return Root
    elif ArrayNodes[Root][1]==-1:
            return -1
    if ArrayNodes[Root][1]>ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    
    if ArrayNodes[Root][1]<ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    

def PostOrder(rootnode):
    if rootnode[0] != -1:
        PostOrder(ArrayNodes[rootnode[0]])
    if rootnode[2] != -1:
        PostOrder(ArrayNodes[rootnode[2]])
    print(str(rootnode[1]))





ArrayNodes=[[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]
FreeNode=6
RootPointer=0

Returnval=SearchValue(RootPointer, 15)
if Returnval==-1:
    print("Value not found")
else:
    print("Found at"+ str(Returnval))
PostOrder(ArrayNodes[RootPointer])