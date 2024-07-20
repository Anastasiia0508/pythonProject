first = input("Введите число:")
second = input("Введите число:")
third = input("Введите число:")
if first == second == third:
    print(3)
elif first == third or second == third or first == second:
    print(2)
elif first != second != third:
    print(0)
