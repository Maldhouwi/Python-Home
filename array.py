courses = ["datascience", "computerscience", "MIT"]

# Accessing an element in an array
print(courses[1])

# looping through an array - printing each element in a variable

for course in courses:
  print(course)


# Adding an element to an array
courses.append("android development")

# Removing an element from an array
courses.remove("computerscience")
print(courses)