# цикли
test_list = [1, 2, 3, 4, 5, 6]

for num in test_list:
    print(f"You have got a {num}")


a = 0

while a < 10:
    a += 1
    print(a)


b = 7
while len(test_list) < 13:
    test_list.append(b)
    b += 1
    print(test_list)


# ітерація
test_list_2 = ["test", "python", "Anya"]

for s in test_list_2:
    print(s, "is updating...")
    if s == "test":
        print(s)
    elif s == "python":
        print(s)
    else:
        print(s)


# тест циклів
user_1 = {"username": "tester", "role": "admin", "connection": True}

user_2 = {"username": "junior", "role": "guest", "connection": False}

user_3 = {"username": "middle", "role": "user", "connection": True}

list_of_users = [user_1, user_2, user_3]

for user in list_of_users:
    print(f"Work with {user['username']} account |")
    if not user["connection"]:
        count_of_tries = 10
        while count_of_tries != 0:
            print("Trying to connect...")
            count_of_tries -= 1
            if count_of_tries == 5:
                print("Time to fix your internet")
                continue
            print("Count of tries left: ", count_of_tries)
    elif user["role"] == "admin":
        print(f"Welcome back, {user['username']}")
    else:
        print("Welcome on the board")
print("All users were checked!")
