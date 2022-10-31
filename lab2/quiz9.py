# Given a positive integern, assign True to is_prime if n has no factors other than 1 and itself. (Remember,
#  m is a factor of n if m divides n evenly.)
def computePrime(n:int)->bool:
    count = 0
    for x in range(1, n):
        if n % x == 0:
            count = count + 1

    if count == 1:
        is_prime = True
    else:
        is_prime = False
    return is_prime


n = int(input("Input an integer  : "))
is_prime:bool = False

print(f"is {n} prime : ",computePrime(n))
