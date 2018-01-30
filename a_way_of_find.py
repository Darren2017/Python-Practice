def findchr(string, char):
    for i in range(len(str)):
        if char in string[i]:
            return i
    else:
        return -1
str = raw_input()
char = raw_input()
print findchr(str, char)