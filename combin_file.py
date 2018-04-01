#coding:utf-8
def write(so):
    fr = open(so, 'r')
    fw = open('newone.xlsx', 'w')
    for txt in fr:
        fw.write(txt)
    fw.close()
def showmenu():
    while True:    
        choice = input('''1-combin file
2-over
''')
        if choice == 1:
            so = raw_input('please enter the name you want to combin: ' )
            write(so)
        if choice == 2:
            break
if __name__ == '__main__':
    showmenu()