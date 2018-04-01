#coding:utf-8
a = input()
b = int(raw_input())
c = int(raw_input())
if (sum([a,b,c]) - max(a,b,c)) < max(a, b, c):
    print '无法构成三角形'
elif a == b == c:
    print '等边三角形'
elif a == b or a == c or b == c:
    print '等腰三角形'
else:
     print '普通三角形'
