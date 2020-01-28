import collections
d = {"a":20, "b":30, "c":40, "d":10, "e":80, "f":50}
d = collections.Counter({i:d[i] for i in d}) 
print(d.most_common(3))