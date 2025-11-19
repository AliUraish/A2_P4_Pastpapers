#PartA
#Declare the array TheData as the local variable and initialize it with the given values
TheData=[20, 3, 4, 8, 12, 99, 4, 26, 4]

#PartB
#Pseudocode for an insertion sort algorithm to sort the items in TheData array into ascending order
def InsertionSort(TheData):
    Inserted=0
    for count in range(1,len(TheData)):
        Datatoinsert=TheData[count]
        NextValue=count-1
        while NextValue>=0 and count!=1:
            if Datatoinsert<TheData[NextValue]:
                TheData[NextValue+1]=TheData[NextValue]
                NextValue=NextValue-1
                TheData[NextValue+1]=Datatoinsert
            else:
                Inserted=1


#PartC
#Procedure to output all the items in TheData array. It should use iteration. 
def output(Array):
    for items in Array:
        print(items)
#OutputArray=output(TheData)


#print(OutputArray) So the output is not repeated in part D. Used here as mentioned in question. 

#PartD (i)
#Show data in TheData array before sorting and after sorting using subroutines in part B and C
unsorted=output(TheData)
print(unsorted)
sorted=InsertionSort(TheData)
print(sorted)

#PartD (ii)
#Its about testing my project and pasting the screenshot of the output in evidence document. 
