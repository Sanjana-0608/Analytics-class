from print_statements import repeat_hello_name, hello_name


def print_even_up_to_number(input_number):
    list_of_numbers= list(range(1,input_number))
    for number in list_of_numbers:
        if number % 2 == 0:
            print(number)



if __name__ == "__main__":
    print("Hello World")
    repeat_hello_name(somename="Sanjana", n_times=7)
    hello_name("Sanjana")

    list_of_names = ["Rahul", "Prof Elizabeth", "Bahubali", "Pillu"]
    for name in list_of_names:
        hello_name(name)

    number_list = [1, 2, 3, 4, 5]
    print(number_list)

    for num in number_list:
        print(num)

    print_even_up_to_number(22)
