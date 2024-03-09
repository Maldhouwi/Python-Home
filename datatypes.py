# Datatype

number = 60  # int

num = 34.78  # float

greeting = "Hello there"  # str

isPythonInteresting = "True"  # bool

# A variable with multiple values

# list - special brackets
languages = ["Python", "C++", "Java", "kotlin"]  # list

# tuple - normal brackets
fruits = ("mango", "apple", "banana", "pineapple")  # tuple

# set - calibraces
countries = {"England", "Ghana", "China"}  # set


# Dictionary
# Appears in form of a key and a value
# Uses calibraces
# The variable is separated from the content words by colon but each variable is separated by a comma


details = {
    "firstname": "Ashley",
    "course": "MIT",
    "age": "18",
    "nationality": "kenyan"
}





print(number)
print(num)
print(details["nationality"]) # Printing out something specific in the dictionary - use special brackets
print(details["firstname"])



# Determining data type of a  certain variable
print(type(details))
print(type(countries))
print(type(greeting))


#Typecasting - Converting one data type to another
print(float(number))
print(int(num))
