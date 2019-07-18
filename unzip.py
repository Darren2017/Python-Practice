#-*-coding:utf-8-*-
import zipfile
 
Pos_find='/Users/darren/Documents/program/ccnu-network-culture-festival'    #需要解压缩的目录
Pos_mved="/Users/darren/Documents/program/Python-Practice/test/"  #解压缩之后文件的储存目录

import os
for(dirpath,dirnames,files)in os.walk(Pos_find): #遍历当前目录下的全部文件以及子文件
    for filename in files:
        # print(filename.split('.')[0])
        try:
            if filename.split('.')[1] == 'html':
                filepath = os.path.join(dirpath, filename)  #构造当前文件的路径
                with open(filepath) as f:
                    content = f.read()
                    namelist = [
                        "丁亨通",
                        "秦广友",
                        "肖博文",
                        "尹航",
                        "郭彦炳",
                        "万翠红",
                        "朱成周",
                        "徐勇",
                        "王恩科",
                        "朱英",
                        "王泽龙",
                        "王健",
                        "张礼知",
                        "张铁锐",
                        "邓大才",
                        "李遇春",
                        "彭南生",
                        "吴元芳",
                        "徐杰",
                        "杨浩",
                        "周少林",
                        "余新国",
                        "陈绍龙",
                        "郭军",
                        "陈靓影",
                        "吴凡",
                        "洪建中",
                        "刘合力",
                        "孙春友",
                        "晏成林",
                        "李新强",
                        "辛欣",
                        "谢跃红",
                        "Paolo Bartalini",
                        "Meng Fai Lim",
                        "张兆曙",
                        "黑谷一夫",
                        "范炤",
                        "程晓荣",
                        "晏挺",
                        "刘政",
                        "谢波",
                        "邱涛涛",
                        "郝格非",
                        "蒋兴鹏",
                        "龚欣",
                        "刘珂",
                        "郎贤军",
                        "徐添喜",
                        "杨玉芹",
                        "唐岚",
                        "赵蕴杰",
                        "罗竹",
                        "PRASHANT SINGH"
                    ]
                    for n in namelist:
                        if n in content:
                            print(n + "|MOVED|" + str(filename))
                            os.rename(filepath, Pos_mved+filename)
                            break
                    
        except Exception as e:
            pass