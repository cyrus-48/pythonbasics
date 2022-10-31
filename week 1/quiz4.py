# Write a Python program to print the number of prime numbers which are less than or equal to a given integer.

def prime(number: int)->None:
    for number in range(1, number):
        # all prime numbers are greater than 1
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)


number: int = int(input("Enter number : "))
prime(number)
