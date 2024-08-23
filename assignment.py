

def product_of_numbers_upto_n(num):
    product = 1
    for i in range(1, num+1):
        product *= i
    return product

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"product_of_numbers_upto_n = {product_of_numbers_upto_n(i)}")


def factors_of_number(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    for i in range(1, 101):
        print(f"Factors of {i} = {factors_of_number(i)}")



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for n in range(1, 11):
        if is_prime(n):
            print(f"is_prime(n) = {is_prime(n)}")
        else:
            print(f"is_prime(n) = {is_prime(n)}")

def multiply_primes_up_to_n(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = 1
    for num in range(2, n + 1):
        if is_prime(num):
            result *= num
    return result

if __name__ == "__main__":
    for num in range(1, 12):
        print(f"multiply_primes_up_to_n(num) = {multiply_primes_up_to_n(num)}")

import math


def calculate_distance(x, y, z):
    return math.sqrt(x * 2 + y*2 + z * 2)


if __name__ == "__main__":
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))
    z = float(input("Enter the z-coordinate: "))
    distance = calculate_distance(x, y, z)

    print(f"The distance of the vector ({x}, {y}, {z}) from the origin (0, 0, 0) is {distance:.2f}")




