

def sum_of_numbers_upto_n(num):
    output = 0
    for i in range(1, num + 1):
        output += i
    return output


def is_prime(i):
    pass


def multiply_primes_upto_n(num):
    product = 1
    for i in range(2, num + 1):
        if is_prime(i):
            product *= i
    return product

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Product of primes up to {i} = {multiply_primes_upto_n(i)}")

print()