#Lists use Square brackets
#List allow duplicate values
mylist = ["apple", "banana", "cherry", 32, "apple", 6, 2.5]
print("0", mylist)
print("1", len(mylist))   # len() function tells the length of anything we want.

#List items are indexed, first index starts at 0
print("2", mylist[2])              # second element
#negative measns start from end
print("3", mylist[-1])            # last element
print("4", mylist[3:6])           # 3rd to 5th index

#List items are mutable i.e. can be changed
#last index is not included, it changes for 1 and 2 i.e. banana and cherry
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["mango", "watermelon"]  # first and second updated to given
print("5", thislist)

#Can insert more items than specified by index
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]      # here since specified index is less than given items, inserted
print("6", thislist) 

#can inser less items than specified
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]    # DOUBT
print("7", thislist) 

#can insert without replacement via insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")            # inserted into the second index
thislist.append("orange")                   # inserted in the end.
print("8", thislist)

#can remove items as well
thislist.remove("orange")                   
#pop is used to remove from specific index
thislist.pop(1)                             # remove the indexed element
print("9", thislist)
#no argument, removes last element
thislist.pop()                              # remove the last element
#can use del also
thislist = ["apple", "banana", "cherry"]
del thislist[0]                             # function {del} removes the element
print("10", thislist)
#removes entire list
del thislist                                # no specification then remove everything.

#List comprehension
#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("11", newlist)                        # checks if a's are present in the names of element then add those to newlist
newlist = [x.upper() for x in fruits]       # Converts every element into uppercase then present
print("12", newlist) 


#Join lists; + creates a new list; while extend, extends the first list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2                       # add to concatenate the the lists.
print("13", list3) 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)                         # extending the list1 only.
print("14", list1) 


#Few other methods
#sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()                             # lexicographical sorting
print("15", thislist)
#descending sort
thislist.sort(reverse = True)
print("16", thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# reverses current order
thislist.reverse()                          # reverses the current list.
print("18", thislist)  

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()  # copies the list.
print("19", mylist)
