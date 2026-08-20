# Strings (Concatenation, Slicing and Other methods) :
 
# 1. String Concatenation: Write a Python program that takes two strings 
# i.e string 1 “Hello ”, string 2 get name as input from the user and concatenates them together.
# Display the concatenated string as the output.
  
Name = input("Enter your Name")
Result = "Hello" + " " + Name
print(Result)

# Now concatenate string 3 “, welcome to Python programming” to the existing string 
# and display the output string. 

Result1 = Result + "," + "Welcome To Python Programming"
print(Result1)

#String Slicing and Indexing:

# Write a Python program using the above concatenated string as input and performs the following tasks: 

Name = input("Enter your Name")
text = "Hello " + Name + ", Welcome to Python Programming"
#  a. Print the first character of the string.
print("First Character:",text[0]) 
#  b. Print the last character of the string.
print("Last Character:",text[-1])
#  c. Print the first 5 characters of the string. 
print("First 5 Character:",text[:6])
#  d. Print the last 11 characters of the string. 
print("Last 11 Characters:",text[-11:])
#  e. Print the string in reverse. 
print("Reverse",text[::-1])
#  f. Use slicing and print the word “Python” from the existing string.
print(text[25:32]) 
 
# 3. String Methods:
#Write a Python program that takes a string, strM = “Python beginner tutorial” and
#perform the following tasks:

# a. Convert the sentence to uppercase.
strM = "Python beginner tutorial"
print("Uppercases:",strM.upper())

# b. Convert the sentence to lowercase.
print("Lowercase:",strM.lower())

# c. Use Capitalize and return the sentence to the original input form.
print("Capitalize:",strM.capitalize())

# d. Count the total number of occurrences of character ‘t’ in the string.
print("Number of t:",strM.count('t'))

# e. Replace all occurrences of “Python” with “Machine Learning” in the input string
#strM = “Python beginner tutorial”
print("Replaced Python:",strM.replace("Python","Machine Learning"))

# Tuples (Creation, Modification and Access) :
#Create 1st tuple with values -> (10, 20, 30), 2nd tuple with values -> (40, 50, 60):

tup1 = (10,20,30)
tup2 = (40,50,60)

# a. Concatenate the two tuples and store it in “t_combine”
t_combine = tup1 + tup2
print("Combined Tuple:",t_combine)

# b. Repeat the elements of “t_combine” 3 times
print("Repeated tuple:",t_combine*3)

# c. Access the 3rd element from “t_combine”
print("Thrid element:",t_combine[2])

# d. Access the first three elements from “t_combine”
print("First three element:",t_combine[:3])

# e. Access the last three elements from “t_combine”
print("Last three element:",t_combine[-3:])