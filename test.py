num = 7
num_is_prime = True

if num > 1:
    for i in range(2,int(num ** 0.5) + 1):

        if num % i == 0:
            num_is_prime = False
            break

        if num_is_prime:
            print(num,"is a prime number")
        else:
            print(num,"is not a prime number")
else:
    print(num,"is not a prime number")