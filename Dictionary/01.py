# # Create a dictionary containing:
# student = {
#     "name": "soyab",
#     "age":  22,
#     "city": "himcachal",
#     "course": "BCA"
# }

# print(student.keys())
# print(student.values())



# Create a student dictionary and update the student's age.
# student = {
#     "name": "soyab",
#     "age":  22,
#     "city": "himcachal",
#     "course": "BCA"
#  }

# student["age"] = 33
# print(student)



# Check whether a particular key exists in a dictionary.
# student = {
#     "name": "soyab",
#     "age":  22,
#     "city": "himcachal",
#     "course": "BCA"
#  }
# if "age" in student:
#     print("yes")



 # Count the number of keys in a dictionary.
# student = {
#     "name": "soyab",
#     "age":  22,
#     "city": "himcachal",
#     "course": "BCA"
#  }
# print(len(student))
# or
# key = 0
# for i in student.keys():
#     key+=1

# print(key)




# Create a dictionary containing marks of 5 subjects and calculate the total marks.

# marks = {
#     "English": 80,
#     "Math": 90,
#     "Science": 85,
#     "cs": 99,
#     "c++": 78
# }

# totalMarks = 0

# for i in marks.values():
#     totalMarks+=i

# print(totalMarks)




# Find the subject with the highest marks.

marks = {
    "English": 80,
    "Math": 90,
    "Science": 85,
    "cs": 99,
    "c++": 78
}

subjectWithMarks = 0
subjects = ""

for subject, marks in marks.items():
    if marks>subjectWithMarks:
        subjectWithMarks=marks
        subjects = subject

print(f"subject with the highest is = {subjects}: {subjectWithMarks}")
