import string

str = raw_input()
i = 0
while str[i] == ' ':
    str = str[1:]
str = list(str)
str.reverse()
i = 0
while str[i] == ' ':
    str = str[1:]
    str = list(str)
str.reverse()
str = ''.join(str)
print str