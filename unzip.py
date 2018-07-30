#-*-coding:utf-8-*-
import zipfile
 
Pos_zip='/Users/darren/Downloads/do/article'    #需要解压缩的目录
Pos_unzip="/Users/darren/Downloads/unzip/article/"  #解压缩之后文件的储存目录
import os
for(dirpath,dirnames,files)in os.walk(Pos_zip): #遍历当前目录下的全部文件以及子文件
    for filename in files:
        # print(filename.split('.')[0])
        if filename.split('.')[1] == 'zip':
            filepath = os.path.join(dirpath, filename)  #构造当前文件的路径
            # print(filename.split('.')[0])
            zf = zipfile.ZipFile(filepath, 'r')
            zf.extractall(Pos_unzip+filename.split('.')[0])