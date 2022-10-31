# Given a positive integern, assign True to is_prime if n has no factors other than 1 and itself. (Remember,
#  m is a factor of n if m divides n evenly.)
n = int(input("Input an integer  : "))
is_prime = False


def computePrime(n):
    count = 0
    for x in range(1, n):
        if n % x == 0:
            count = count + 1

    if count == 1:
        is_prime = True
    else:
        is_prime = False
    return is_prime


print(computePrime(n))
