list_of_sets = list()
for num_of_set in range(3):
    list_of_sets.append(set( ( input("input set "+ str(num_of_set+1) +": ") ).split(" "))) 
    
print("set #3 is subset of set #1 and set #2: ", 
    list_of_sets[2].issubset(list_of_sets[0])  and
    list_of_sets[2].issubset(list_of_sets[1]))   
#print(list_of_sets[0])