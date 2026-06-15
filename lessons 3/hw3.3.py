list = [1, 2, 3, 4, 5, 6]
#list = [1, 2, 3]
#list = [1, 2, 3, 4, 5]
#list = [1]
#list = []

old_list = list.copy()

middle_index = len(list) // 2
if len(list) % 2 != 0:
    middle_index += 1

first_part = list[:middle_index]
second_part = list[middle_index:]

result = [first_part, second_part]
print(f"{old_list} => {result}")