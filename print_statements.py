print("hello world")
print("My name is Sanjana Nayak")
myname = "Honey"
print(f"Hello {myname}! How are you?")

def hello_name(somename):
    print(f"Hello {somename}! This is a function.")

def repeat_hello_name(somename, n_times):
    for i in range(n_times):
        print(f"Hello there {somename}! This is print statement number: {i}")

def repeat_hello_name(somename, n_times):
    for i in range(n_times):
        print(f"Hello there {somename}! This is print statement number: {i+1}")


if __name__ == "__main__":
    hello_name("Class")
    hello_name("Alex")
    hello_name("Folks")

    repeat_hello_name(somename="Sanajna", n_times=7)


