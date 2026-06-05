#program to create a list 20 number given by user
# Create an empty list to store number
numbers=[]
print("enter any 20 number:")
for x in range(20):
    num=int(input())
    #append int list
    numbers.append(num)
print("--------------------------")
element=int(input("enter any nunmber to remove its duplicate:"))
#--------------------------------------------------------
#finding the frequency of given number
frequency= numbers.count(element)
if frequency==0:
    print("element not found")
else:
    #reversing the list
    numbers.reverse()
    for i in range(1,frequency):
        numbers.remove(element)
        #reversing the list again
        numbers.reverse()
        print("after removing duplicates")
        print(numbers)



