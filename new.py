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


# комбіновані умови
def check_connection(username, count_tries, priority):
    if priority >= 10:
        finish = 5
        for attempt in range(1, count_tries + 1):
            if attempt == finish:
                print("Succesful connect!")
                break
            print(f"Attempt № {attempt} to connect to {username}")

    elif priority >= 5 and priority < 10:
        finish = 3
        for attempt in range(1, 6):
            if attempt == finish:
                print("Succesful connect!")
            print(f"Attempt № {attempt} to connect to {username}")

    else:
        print("Sorry, but your priority is too low")


check_connection(count_tries=10, username="Volodya", priority=20)


# модулі
# створив свій модуль і підключив його у окремій папці
import turtle


def draw(size, color):
    turtle.speed(1)
    turtle.color(color)
    turtle.begin_fill()

    def move(len):
        turtle.forward(len)
        turtle.left(90)

    for _ in range(4):
        move(size)

    turtle.end_fill()


draw(100, "green")
turtle.goto(100, 100)
draw(200, "purple")
