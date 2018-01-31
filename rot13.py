#coding:utf-8
import string
tran = raw_input('Enter string to rot13:')
print 'Your string to en/decrypt was: [%s]'  %  tran
newstring = list(tran)
k = 0
for i in tran:
    l = 0
    for j in string.uppercase:
        if i == j:
            if l >= 13:
                newstring[k] = string.uppercase[l - 13]
                break
            else:
                newstring[k] = string.uppercase[l + 13]
                break
        l += 1
    l = 0
    for j in string.lowercase:
        if i == j:
            if l >= 13:
                newstring[k] = string.lowercase[l - 13]
                break
            else:
                newstring[k] = string.lowercase[l + 13]
                break
        l += 1
    k += 1
print ''.join(newstring)