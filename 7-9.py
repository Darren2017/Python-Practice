#coding:utf-8
srcstr = raw_input('请输入要翻译的字符:')
dststr = raw_input('请输入翻译后的结果：')
string = raw_input('请输入要翻译的字符串：')
stringlist = list(string)
l = 0
for i in srcstr:
    k = 0
    for j in string:
        if i == j:
            stringlist[k] = dststr[l]
        k +=1
    l += 1
newstring = ''.join(stringlist)
print newstring