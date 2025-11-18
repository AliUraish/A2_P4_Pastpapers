# PART C
# Write a bubblesort() algorithm to sort the data in the "theArray" into descending order.
# The pseudocode is already given in the question paper.
# this Array was not given in the question, I have created it for testing purpose.
theArray=[5, 6, 2, 8, 1, 4, 9, 3, 7, 0]

def bubblesort():
    for x in range(len(theArray)-1):
        for y in range(len(theArray)-1):
            if theArray[y]<theArray[y+1]:
                temp=theArray[y]
                theArray[y]=theArray[y+1]
                theArray[y+1]=temp

#this test was not included in the question, you can run the code and test it yourself for your assurance. 
bubblesort()
print("Sorted array in descending order:", theArray)
