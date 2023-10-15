"""
powerOfK
Determine if a number, n, is a power of some other number k.
Return the exponent.
For example, for n = 9 and k = 3, return 2 because 3 to the power of 2 is 9.
If n is not a power of k, return -1.

We will not be testing with negative values or exponents
and k will be greater than 1.

"""


def powerOfK(n, k):
    if n == 1:
        return True

    div = k
    while div * div <= n:
        div = div * div

    if n % div != 0:
        return False
    return powerOfK(n / div, k)

print(powerOfK(9,3))