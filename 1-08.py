#打开一个文件，显示其中的内容
filename = raw_input()
fobj = open(filename, 'r')
for eachL in fobj:
    print eachL,
fobj.close()