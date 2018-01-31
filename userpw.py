#!/usr/bin/env python
import datetime
import string

db = {}
dt = {}

def md5(str):                                               #md5加密函数
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def newuser():                                              #新用户登录函数
    while True:
        name = raw_input('Enter your name:')
        for i in name:
            if i not in string.letters + string.digits:
                print 'your name must in alphabet or number'
                continue
        if name in db:
            print 'Name has existed, please enter again'
        else:
            break
    paw = raw_input('Enter your password:')
    db[name] = md5(paw)
    dt[name] = datetime.datetime.now()
    print 'success to join'

def olduser():                                              #老用户登录函数
    while True:
        name = raw_input('Enter your name: ')
        if name not in db:
            choice = input('''your name not exist
            1-continue login in
            2-creat new one
            ''')
            if choice == 1:
                continue
            if choice == 2:
                newuser()
                return
        else:
            break
    while True:
        password = raw_input('Enter your password: ')
        paw = md5(password)
        if db[name] != paw:
            print 'passward is error, please enter again'
        else:
            print 'success to enter'
            if (datetime.datetime.now() - dt[name]).seconds / 3600 < 4:
                print 'You already logged in at :', dt[name]
            dt[name] = datetime.datetime.now()
            break
def manager():                                              #管理员函数
    def delete():
        delete = raw_input('Enter the name you want to delete: ')
        del db[delete]
        del dt[delete]
    def view():
        print db
    while True:
        passward = input('please enter your passward: ')
        if passward == 5886:
            break
    while True: 
        pr = '''
        (D)elete
        (V)iwe
        '''
        choice = raw_input(pr).strip()[0].lower()
        if choice in 'dv':
            break
    if choice == 'd':
        delete()
    elif choice == 'v':
        view()



def showmenu():                                             #显示菜单
    while True:
        pr = '''
        (O)lduser
        (N)ewuser
        (M)anager
        (Q)uit
        '''
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
                if choice in 'qnomv':
                    break
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
                break
        if choice == 'o':
            olduser()
        elif choice == 'n':
            newuser()
        elif choice == 'm':
            manager()
        elif choice == 'q':
            break
if __name__ == '__main__':                                  #主程序入口                        
    showmenu()