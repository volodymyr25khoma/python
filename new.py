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
