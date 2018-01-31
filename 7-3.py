import time
import datetime
dict1 = {1:'d', 4:'a', 3:'c'}
dict1_key = sorted(dict1.items(), key = lambda x:x[0])
for i in dict1_key:
    print i[0],
print ''
for i in dict1_key:
    print i,
print ''
dict1_value = sorted(dict1.items(), key = lambda x:x[1])
for i in dict1_value:
    print i,