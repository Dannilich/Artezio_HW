dict_1 = {1:"a", 2:"b", 3:"c"}
dict_2 = {1:"A", 2:"B", 3:"C", 4:"C"}


list_of_values = list()

list_of_values.append(list())
for key in dict_1:
    list_of_values[0].append(dict_1[key])

list_of_values.append(list())
for key in dict_2:
    list_of_values[1].append(dict_2[key])

merge_values = list(zip(list_of_values[0],list_of_values[1]))
print(merge_values)

keys = set(dict_1).union(dict_2)
print(keys)

