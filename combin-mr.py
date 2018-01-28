#合并两个文档

flist = ['makeTextFile.py', 'readTextFile.py']
ofile = open('combin.py', 'w')
for fr in flist:
    for txt in open(fr, 'r'):
        ofile.write(txt)
ofile.close()