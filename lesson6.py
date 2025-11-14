# функції
def say_hello(username, age):
    print(f"Hello, {username}!")
    print(f"Your age is {age}, awesome!")
    print("----------------------------")


def print_numbers(start, finish):
    for num in range(start, finish):
        print(f"the number is: {num}")
    print("------------------------")


user_data = {"Volodya": 22, "Anya": 18, "Jack": 5}
range_list = [(1, 10), (2, 9), (3, 8)]

for name, age in user_data.items():
    say_hello(name, age)

for start_pos, last_pos in range_list:
    print_numbers(start_pos, last_pos)
