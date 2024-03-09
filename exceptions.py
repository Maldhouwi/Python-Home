# Exceptions = errors

try:
    print(x)

except:
    print("Something went wrong")


try:
    num1 = 20
    num2 = 0
    print(num1 / num2)
except:
    print("Zerodivision error occurred")



# Usre defined functions
try:
    def multiply(number1, number2):
        print(number1 * number2)

except:
    print("Something went wrong")

finally:
    print("Success")


multiply(10, 20)