# умовні оператори

string = "Hello world!"

if "Hello" not in string:
    print("Hello in string")
elif "world" in string:
    print("world in string")
else:
    print("Word is not in string")


# умови з числами
a = 10
b = 20
if a >= 10 and b > 20 or b < 30:
    print(a + b)
else:
    print("error 404")


# умови зі списками
test_list = ("Hello", "Anya", 1, 2, 3)

if "Hello" in test_list and 1 in test_list:
    print("Hello 1")
elif "Anya" in test_list and 5 not in test_list:
    print("Anya not 5")
else:
    print("You are wrong like your conditions")

# додатково
a = 10
b = 20
c = "chat is active"
d = "count of users"
print(len(c), len(d))

if len(c) >= b:
    print(c)
elif len(d) <= a:
    print(d)
else:
    print("error")


# вкладені умови
user_1 = {
    "name": "Volodya",
    "age": 22,
    "balance": 50000,
    "currency": "USD",
    "status": True,
}

user_2 = {
    "name": "Anya",
    "age": 18,
    "balance": 10000,
    "currency": "EUR",
    "status": True,
}

user_3 = {
    "name": "Roman",
    "age": 28,
    "balance": 100000,
    "currency": "PLN",
    "status": False,
}

currency_list = {"USD", "UAH", "EUR", "PLN", "GBP"}

if user_2["name"] and user_2["age"] >= 18 and user_2["status"]:
    if user_2["balance"] >= 10000 and user_2["currency"] in currency_list:
        print(f"Hello and welcome to ByBit, {user_2['name']}")
    elif user_2["balance"] >= 1000 and user_2["currency"] in currency_list:
        print("You need more money for registration!")
    else:
        print("Critical not enough")
elif not user_2["name"]:
    print("Please, write your name in your account description")
elif user_2["age"] < 18:
    print("You have to be 18 or more years old for registration")
else:
    print("Something went wrong, try again")
