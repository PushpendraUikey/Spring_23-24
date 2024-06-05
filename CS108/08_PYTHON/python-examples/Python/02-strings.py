#string assignment; 
a = "hello"
#multiline string assignment, notice """
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#strings as arrays
print(a)
print(a[1]) # what is at the index one.
print(len(a))  # what is the length of the string
print(a[2:5]) # Start from 2 and go till 5th  index which is 4
print(a[:5])  # from first to 5th index
print(a[120:]) # from 120th index to last.
#negative index means slice from the end of the string
#Negative indices count from the end of the sequence, 
#with -1 representing the last element
print(a[-5:-1])  #negative indexing starts from last 

#Use of operators
#Is the word sit in the variable a?
print("sit" in a)
print("dolor" not in a)


#Built in methods on strings 
a = "      hello world !!!     "
print(a.upper())
print(a.strip()) #  removes spaces only at beginning and end
print(a.replace("l","i"))  #replaces the value of l to i.

#format string, this is another way, 
#more recent is use of f-string as covered in 01-example.py
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) # old, no need to remember- USE f""
