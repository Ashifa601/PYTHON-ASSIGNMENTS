# Python Assignment 2: Data Structures - List, Dictionary, Set
# & Conditional Statements

# List (Creation, Modification and Access):
# 1. List Creation:
#a. Create a list named age_list with five integer elements. For eg., [24, 25, 26, 27, 28]
age_list = [24,25,26,27,28]
print ("Age List:", age_list)

# b. Create a list named name_list with five string elements.
name_list = ["Diya","Arun","Rahul","Arya","Aysha"]
print ("Name List:", name_list)

# 2. List Operations / Modifications:
#a. Append the string "Yazhini" to name_list.
name_list.append("Yazhini")
print("After Append:", name_list)
#b. Insert the element 30 at index 2 in age_list.
age_list.insert(2,30)
print("After Inserting 30:", age_list)

#c. Remove the string "Yazhini" from name_list.
name_list.remove("Yazhini")
print("After Removing Yazhini:", name_list)

#d. Pop the last element from age_list.
age_list.pop()
print("After Popping Last Element:", age_list)

#e. Extend the age_list with additional ages [29, 30, 26].
age_list.extend([29,30,26])
print("After extending:", age_list)

#f. Sort age_list in descending order.
age_list.sort(reverse=True)
print("Descending order:",age_list)

#g. Find Max age, Min age and sum of all ages from age_list.
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))

# 3. Accessing List Elements:
#a. Print the first element of name_list.
print("First element:", name_list[0])

#b. Print the last element of name_list.
print("Last element:", name_list[-1])

#c. Print the elements from index 2 to index 4 in name_list.
print("Elements from index 2 to 4:", name_list[2:5])

#d. Print the elements of name_list in reverse order.
print("Reverse order:", name_list[::-1])

# Dictionary (Creation, Modification and Access):
#a. Create a dictionary named student_marks that maps the names of five
#students to their marks (use scale of from 0 to 100).
student_marks = {
    "Anu": 85,
    "Rahul": 72,
    "Meera": 90,
    "Aisha": 78,
    "Vivek": 65
}


#b. Access and print the mark of a specific student, of your choice.
print("Meera's mark:", student_marks["Meera"])

#c. Add a new student "Janani" with a mark of 80 to the student_marks dictionary.
student_marks["Janani"] = 80
print("After adding Janani:", student_marks)

#d. Update the mark of any one older student to 82.
student_marks["Rahul"] = 82
print("After updating Rahul's mark:", student_marks)

#e. Use the keys(), values(), and items() methods to print all keys, values, and
#key-value pairs in the student_marks dictionary.
#Print all keys
print("Keys:", student_marks.keys())

# Print all values
print("Values:", student_marks.values())

# Print all key-value pairs
print("Key-value pairs:", student_marks.items())

#Sets (Operations):
#a. Create a set called my_set with following values:
#['a','e','i','o','u','a','a','i']
# Analyse the output and provide explanation for the same.
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print("my_set:", my_set)

#b. Attempt to change the value of my_set[4] = 's'. If code throws an error, provide
#an explanation.
# my_set[4] = 's'       #TypeError: 'set' object does not support item assignment
# Explanation: Sets are unordered and do not have indexes

#c. Create two sets:

#set1 with values: {1, 3, 5, 7, 9}
#set2 with values: {2, 3, 5, 8, 10}

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}


#d. Compute and print the union and intersection of set1 and set2.
union_set = set1.union(set2)

intersection_set = set1.intersection(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)

#Operators & Conditional Statements :
#(IF, ELIF, ELSE)
#Performance Category Program:
#1. Prompt user for Input. Score range should be from 0 to 10 (both inclusive).
# 2. Find the performance category based on the input score using following criteria:
#a. Above Average: Score greater than 7
#b. Average: Score between 4 and 7(both inclusive)
#c. Below Average: Score lesser than 4
#3. Output: Print the Performance category
#4. Additional Step: You can give a prompt of your choice to each category.

#For eg: If score below average “Need to Improve your performance, consistent
#practice will lead to better results”.

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent performance! Keep it up.")

elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")