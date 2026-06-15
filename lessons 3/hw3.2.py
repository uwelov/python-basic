list = [12, 3, 4, 10]
#list = [1]
#list = []
#list = [12, 3, 4, 10, 8]
old_list =list.copy()
if len(list) == 0:
    print(f"{old_list} => {list}")
else:
    last_number = list[len(list) - 1]
    list.remove(last_number)
    list.insert(0,last_number)
    print(f"{old_list} => {list}")