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
