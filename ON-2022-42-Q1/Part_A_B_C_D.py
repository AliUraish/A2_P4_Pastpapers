#PartA
# Declare a global string array "Animals" to store 10 items
Animals: list[str]=[]

#PartB
#Store the given names in the Animals array
#They should be stored in the order given and in lower case
Animals=["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]

#PartC
#Write a code for procedure SortDescending to sort the items in the Animals array into descending order
#The pseudocode is already given in the question paper with 4 incomplete statements
#Descending order according to the first letter of each animal name
def SortDescending():
    global Animals 
    for x in range (len(Animals)-1):
        for y in range (len(Animals)-1):
            if (Animals[y])[0]<(Animals[y+1])[0]:
                temp=Animals[y]
                Animals[y]=Animals[y+1]
                Animals[y+1]=temp

