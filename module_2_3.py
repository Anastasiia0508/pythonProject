my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
if my_list[i] >= 1:
    print(my_list[i])
while i < len(my_list):
    i += 1
    if my_list[i] >= 1:
        print(my_list[i])
    if my_list[i] < 0:
        break
