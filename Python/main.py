# making dictionary

# marks = {"Rahul": 99, "Sachin": 98, "Dhoni": 97}

# print(f"Marks of Students: {marks}")

# print(f"Rahul's Marks: {marks['Rahul']}")


# # copy()	Returns a copy of the dictionary

# copyMarks = marks.copy()
# print(f"Copy Marks: {copyMarks}")

# # clear()	Removes all the elements from the dictionary
# clearMark = marks

# print(f"Clear Marks: {clearMark}")

# clearMark.clear()
# print(f"Clear Marks: {clearMark}")


# # keys()	Returns a list containing the dictionary's keys

# StudentDetails = {
#     "NameOfStudent": "Rahul",
#     "Marks": 99,
#     "RollNo": 1,
#     "Class": 10,
#     "Section": "A",
#     "Gender": "Male",
#     "DateOfBirth": "01-01-2000",
#     "Address": "Pune",
#     "City": "Pune",
#     "State": "Maharashtra",
#     "Country": "India"
# }

# print(f"Keys: {StudentDetails.keys()}")

# # Values()	Returns a list containing the dictionary's values

# print(f"Values: {StudentDetails.values()}")

# # get()	Returns the value of the specified key

# print(f"Get: {StudentDetails.get('DateOfBirth')}")


# # items()	Returns a list containing a tuple for each key value pair

# items = StudentDetails.items()
# print(f"Items: {items}")

# print(f"Item type is {type(items)}")


# # update()	Updates the dictionary with the specified key-value pairs

# # "City": "Pune",
#     # "State": "Maharashtra",


# StudentDetails.update({"City": "Lucknow", "State": "Uttar Pradesh", "NameOfStudent": "Mohammad Danish"})
# print(f"Updated Dictionary: {StudentDetails}")





# making Set


set1  = {1, 2, 3, 4, 5}

set2  = set()


# add()	 	Adds an element to the set

set2.add(6)
set2.add(7)
set2.add(8)
set2.add(9)
set2.add(10)
print(f"Set2: {set2}")
print(f"Type of Set2: {type(set2)}")

print(f"Set1: {set1}")
print(f"Type of Set1: {type(set1)}")

# clear()	 	Removes all the elements from the set

set1.clear()
print(f"Set1: {set1}")
print(f"Type of Set1: {type(set1)}")



# copy()	 	Returns a copy of the set

set3 = set2.copy()
print(f"Set3: {set3}")
print(f"Type of Set3: {type(set3)}")


# difference()	-	Returns a set containing the difference between two or more sets

set3.remove(10)
setDifference = set2.difference(set3)
print(f"Set Difference: {setDifference}")
print(f"Type of Set Difference: {type(setDifference)}")