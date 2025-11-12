# списки
a = [1, 2, 3, 4, 5]
b = ["apple", "pear", "banana"]

print(a[0], a[1], a[-1])
print(b[1], b[-1])

print(a[1:4], a[::2])
print(b[::2])

print(a[::-1])
print(b[::-1])

# методи списку
a.append(6)
b.append("cherry")
print(a, b)

a.insert(2, 9.5)
b.insert(2, "rock")
print(a, b)

a.remove(9.5)
b.remove("rock")
print(a, b)

last_element1 = a.pop()
last_element2 = b.pop()
print(last_element1, last_element2)

print(a.index(3), b.index("banana"))

a.extend([7, 7, 7])
b.extend(["apple", "apple", "pear"])
print(a.count(5), b.count("pear"), b.count("apple"))


print(a, b)
a.sort()
b.sort()
print(a, b)
a.sort(reverse=True)
b.sort(reverse=True)
print(a, b)


# словники
test_dict = {"user": "Volodya", "age": 22, "country": "Poland"}
print(test_dict["user"], test_dict["age"], test_dict["country"])
print(test_dict.get("animal", "key not found"))

test_dict["country"] = "Ukraine"
print(test_dict["country"])

test_dict["animal"] = "Jack"
print(test_dict["animal"])

animal = test_dict.pop("animal")
print(animal)
print(test_dict)


# методи словника
copy_dict = test_dict.copy()
test_dict.clear()
print(test_dict)
print(copy_dict)

for key, value in copy_dict.items():
    print(f"Key: {key}, Value: {value}")


wrong_key = copy_dict.pop("currency", "key not found")
print(wrong_key)

dict_update = {"position": "junior", "salary": 1000}
copy_dict.update(dict_update)
print(copy_dict)
