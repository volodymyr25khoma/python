# класи
class Person:
    name = "Volodya"
    age = 22
    money = 50000


print(Person.name, Person.age)
print(Person.__dict__)

person1 = Person()
person1.pet = "Jack"
print(person1.__dict__)

print(getattr(person1, "job", "Error"))
# якщо просто звернутись до неіснуючого атрибута через принт - отримаємо помилку
# за допомогою функції getattr ми страхуємо себе від помилки
# і задаємо третій параметр як те, що буде вказано після перевірки неіснуючого атрибуту

setattr(person1, "age", 23)
print(person1.age)
print(person1.__dict__)

print(hasattr(person1, "pet"))
print(hasattr(person1, "job"))

del Person.age
print(Person.__dict__)
print(hasattr(Person, "age"))

delattr(Person, "money")
print(Person.__dict__)
print(hasattr(Person, "money"))
