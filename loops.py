# While loop
# Incrementing a number
number = 5
while number <= 10:
    print(number)
    number += 1

# Decrementing a value
num = 15
while num >= 10:
    print(num)
    num -= 1

# Break - makes the program to stop a specific number during printing
x = 1
while x <= 10:
    print(x)
    if x == 6:
      break
    x += 1



# Continue - skips the specific number mentioned and continues printing the rest
count = 19
while count < 25:
    count +=1
    if count == 23:
        continue
    print(count)


#For loop
languages = ["Python", "Java", "c++"]
for lang in languages:
    print(lang)


# Range
for z in range(6):       # When you don't want to specify the first and last number
    print(z)

for y in range(20,31):   # When you want to specify the first and last number
    print(y)

for i in range(1,11,2):   # When you put three values in the brackets the last number shows the increment value
    print(i)


for p in str("hello world"):
    print(p)