dict = {
    "name":"Krishna",
    "age":18,
    "marks":[25,23,15]
}
print(dict)
print(dict["name"])
print(type(dict))
dict["age"]=19  # overwrites
print(dict)
dict["course"]="CSE"
print(dict)
null_dict = {}
print(null_dict)
null_dict["name"]="Krish"
print(null_dict)
# Nested Dictionaries:
dict2 = {"name":"Krish Ingle", "subjects": {"mech":15, "ladc":23,"chem":25},"roll no." : 46}
print(dict2)

# Dictionary Methods
print(dict2.keys())
print(list(dict2.keys()))
print(len(dict2))
print(list(dict2.values()))
pairs = list(dict2.items())
print(pairs)
print(pairs[0])
print(dict2.get("name"))
dict2.update({"City":"Pune", "Age":19})   # if same key is written with different name of value, then the new value overwrites old one
print(dict2)

# SETS
# Set is the colletion of unordered items. Each element mut be unique and immutable in set (Set is mutable). Set doesnt store ists and dictionaries in them
set1 = {1, 2, 3, 2, "Krish"}
print(set1)
print(type(set1))
print(len(set1))
null_set = set()

# Set Methods
set1.add(7)
print(set1)
set1.remove(2)
print(set1)
set1.pop()  # removes random element
print(set1)
set1.clear()
print(set1)
set2 = {1,2,3}
set3 = {3,4,5}
print(set2.union(set3))
print(set2.intersection(set3))

# Practice
# Store following word meanings in a python dictionary:
# table : "a piece of furniture", "list of facts and figures"
# cat : "a small animal"
dict3 = {"table":("a piece of furniture", "list of facts and figures"),"cat" : "a small animal"}
print(dict3)

# U are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "python","java","C++","python","javascript","java","python","java","C++","C"
set4 = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(set4)
Total_classrooms = len(set4)
print("Total Classrooms: ",Total_classrooms)

# WAP to enter marks of 3 subjects from the user and store them un a dictionary. Start with empty dictionary and add one by one. Use subject name as key & marks as value.
marks ={}
x = int(input("Enter Physics Marks:"))
marks.update({"phy" : x})
y = int(input("Enter Chem Marks:"))
marks.update({"chem" : y})
z = int(input("Enter Maths Marks:"))
marks.update({"maths" : z})
print(marks)

# Figure out a way to set 9 and 9.0 as separate values in set
# Solution 1
values = {9, '9.0'}
print(values)
# Solution 2
values1 = {('float',9.0),('int',9)}
print(values1)