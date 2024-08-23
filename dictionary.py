
#key:value
student = {
    "name": "Rahul",
    "age": 25,
    "courses": ["Math", "Computer Science"],
    "graduated": True
}
print(f"student = {student}")


print(f"name of student = {student['name']}")
print(f"age of student = {student['age']}")
print(f"what courses did the student have = {student['courses']}")
print(f"did student graduate = {student['graduated']}")

#add GPA
student['gpa'] = 9.8
print(f"student has {student['gpa']}")

#looping over dictionary: method 1
print("method 1")
for key in student:
    print(f"key = {key}, value = {student[key]}")

print("-"*100)
#method 2
print("method 2")
for key in student.keys():
    print(f"key = {key}, value = {student[key]}")

print("-"*100)
#method 3
print("method 3")
for key,value in student.items():
    print(f"key = {key}, value = {value}")

#nested dictionaries
#dictionaries can contain other dictionaries, allowing for complex dara structure
students_dictionary = {
    "student1": {"name": "Rahul", "age": 25, "GPA": 8},
    "student2": {"name": "Paro", "age": 22, "GPA": 3},
}
print("-"*100)
print("Student 1 details:")
print(f"student name = {students_dictionary['student1']['name']}")
print(f"student age = {students_dictionary['student1']['age']}")
print(f"student GPA = {students_dictionary['student1']['GPA']}")

print("Student 2 details:")
print(f"student name = {students_dictionary['student2']['name']}")
print(f"student age = {students_dictionary['student2']['age']}")
print(f"student GPA = {students_dictionary['student2']['GPA']}")

print("-"*100)
print("method 2")
for student in students_dictionary:
    print(f"student name = {students_dictionary[student]['name']}")
    print(f"student age = {students_dictionary[student]['age']}")
    print(f"student GPA = {students_dictionary[student]['GPA']}")

print("-"*100)
print("method 3")
for student in students_dictionary:
    print(f"student name = {students_dictionary[student]['name']}")
    print(f"student age = {students_dictionary[student]['age']}")
    print(f"student GPA = {students_dictionary[student]['GPA']}")

# Nested Dictionaries
# Dictionaries can contain other dictionaries, allowing for complex data structures.
students_dictionary = {
    "student1": {"name": "Rahul", "age": 25, "GPA": 8},
    "student2": {"name": "Atheendra", "age": 24, "GPA": 9},
}

# List of Dictionaries
students_list = [
{"name": "Rahul", "age": 25, "GPA": 8},
{"name": "Atheendra", "age": 24, "GPA": 9}
]
print("-"*100)
print("method 1")
print("-"*100)
for student in students_list:
    print(f"student name = {student['name']}")
    print(f"student age = {student['age']}")
    print(f"student GPA = {student['GPA']}")

print("-"*100)
print("method 2")
print("-"*100)
for i in range(len(students_list)):
    print(f"student name = {students_list[1]['name']}")
    print(f"student age = {students_list[1]['age']}")
    print(f"student GPA = {students_list[1]['GPA']}")

print("-"*100)
print("method 3")
print("-"*100)
for index, student in enumerate(students_list):
    print(f"name of student number {index + 1} = {students_list[index]['name']}")
    print(f"age of student number {index + 1} = {students_list[index]['age']}")
    print(f"gpa of student number {index + 1} = {students_list[index]['GPA']}")

# List of Dictionaries
students_list = [
{"name": "Rahul", "age": 25, "GPA": 8},
{"name": "Atheendra", "age": 24, "GPA": 9}
]
print("-"*100)
print("method 1")
print("-"*100)
for student in students_list:
    print(f"student name = {student['name']}")
    print(f"student age = {student['age']}")
    print(f"student GPA = {student['GPA']}")

print("-"*100)
print("method 2")
print("-"*100)
for i in range(len(students_list)):
    print(f"student name = {students_list[i]['name']}")
    print(f"student age = {students_list[i]['age']}")
    print(f"student GPA = {students_list[i]['GPA']}")

import pandas as pd

my_class = {
    "Name": ["Rishabh", "Sanjana Nayak", "Shaina Michael", "Monali", "Chaitanya", "Anish", "Nandey", "Rishabh", "Adarsh", "Simran", "Anish", "Siddharth", "Atheendra", "Aayushi"],
    "Age": [22, 24, 23, 25, 27, 26, 22, 24, 25, 23, 26, 27, 28, 24], "GPA": [3.8, 3.9, 3.7, 3.5, 3.6, 3.8, 3.4, 3.9, 3.2, 3.7, 3.5, 3.6, 3.9, 3.8],
    "Major": ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Computer Science", "Data Science", "Computer Science", "Data Science", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering", "Mechanical Engineering", "Computer Science", "Data Science"]
}

data_frame = pd.DataFrame(my_class)
print(data_frame)

print('looping over columns')
for column in data_frame.columns:
    print(f"column = {column}")
    print(f"column values = {data_frame[column]}")

print("-"*100)

print("looping over rows")
for index, row in data_frame.iterrows():
    print(f"Student number = {index + 1}")
    print(f"Name = {row['Name']};\n Age = {row['Age']}; GPA = {row['GPA']}; Major = {row['Major']}")


#let is get the minimum and maximum and mean and mode and median age
print("-"*100)
print("statistics of age")
print(f"minimum age of students = {min(data_frame['Age'])}")
print(f"minimum age of students = {max(data_frame['Age'])}")
print(f"minimum age of students = {data_frame['Age'].mode()[0]}")
print(f"minimum age of students = {data_frame['Age'].median()}")
print(f"minimum age of students = {data_frame['Age'].mean()}")

print("-"*100)
print("statistics of GPA")
print(f"minimum GPA of students = {min(data_frame['GPA'])}")
print(f"minimum GPA of students = {max(data_frame['GPA'])}")
print(f"minimum GPA of students = {data_frame['GPA'].mode()[0]}")
print(f"minimum GPA of students = {data_frame['GPA'].median()}")
print(f"minimum GPA of students = {data_frame['GPA'].mean()}")