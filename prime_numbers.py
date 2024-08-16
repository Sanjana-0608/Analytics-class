

def is_prime(input_num):
    list_of_numbers_from_2_to_nminusone = list(range(2, input_num))
    print(f"list of numbers = {list_of_numbers_from_2_to_nminusone}")
    for num in list_of_numbers_from_2_to_nminusone:
        if input_num % num == 0:
            return False
    return True

if __name__ == "__main__":
    print("This is a file for testing prime numbers")

    input_numbers = [2,3,4,5,6,7,8,9,10,11,12,14]
    for num in input_numbers:
        if is_prime(num):
            print(f"input number is {num}. It is a prime")
        else:
            print(f"input number is {num}. It is a not a prime")