#PART A
#Declare the global 1D array "arraydata"
arraydata = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

#PART B(i)
#A linear search to search the value in arraydata
def linear_search(value: int):
    global arraydata
    for index in range (len(arraydata)):
        if arraydata[index]==value:
            return True
    else:
        return False
        
#PART B(ii)
#Take a value from the user to search in arraydata using linear search
value=int(input("Enter a value "))
result=linear_search(value)
print("Value found:", result)

#PART B(iii)
#Search the value in arraydata using linear search with a value in arraydata and a value not in arraydata
inside_array=(7)
result=linear_search(inside_array)
print("Value found:", result)
outside_array=(20)
result=linear_search(outside_array)
print("Value found:", result)



#done working. 