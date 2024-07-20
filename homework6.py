# СЛОВАРИ
my_dict = {"Asya": 1985, "Gleb": 2021}
print(my_dict)
print(my_dict["Gleb"])  # вывод значения ключа
print(my_dict.get("Ivan"))  # вывод ключа,которго нет в словаре
my_dict.update({"Anton": 1993,
                "Marina": 1962})  # добавила две пары ключ-значение
n = my_dict.pop("Asya")  # удаление пары
print(n)  # вывод значения удаленной пары
print(my_dict)

# МНОЖЕСТВА
my_set = {1, 1, 1, "dog", "dog", True, (1, 2, 3, 4,)}
print(my_set)
my_set.add(5)
my_set.add("cat")
my_set.remove((1,2,3,4))
print(my_set)
