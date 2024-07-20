immutable_var = 38, "Anastasiia", True
print(immutable_var)
# immutable_var[0] = 39
# print(immutable_var)  # заменить элемент невозможно ,тк как сам элемент является неизменяемым
mutable_list = ["вода", "сок", "лимонад"]
print(mutable_list)
mutable_list[1] = "чай"
mutable_list.remove("лимонад")
mutable_list.append("coffe")
mutable_list.extend(["milk", "beer"])
print(mutable_list)
