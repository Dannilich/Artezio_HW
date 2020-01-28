import collections
l_1 = list([1,1,1,1,1,2,2,2,2,3,3,3,4])
l_2 = list([1,1,1,2,2,3,3,3])



c_1 = collections.Counter(l_1)
c_2 = collections.Counter(l_2)

if(len(c_1) > len(c_2)):
    c_1.subtract(c_2)
    diff = c_1
else:
    c_2.subtract(c_1)
    diff = c_2
    
print(diff)