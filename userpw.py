#!/usr/bin/env python

db = {}

def newuser():
    while True:
        name = raw_input('Enter your name:')
        if name in db:
            print 'Name has existed, please Enter again'
        else:
            break
    db[name] = raw_input('Enter your password:')
    print 'success to join'

def olduser():
    while True:
        name = raw_input('Enter your name: ')
        if name not in db:
            print 'Name has not existed, please enter again'
        else:
            break
    while True:
        passward = raw_input('Enter your password: ')
        if db[name] != passward:
            print 'passward is error, please enter again'
        else:
            print 'success to enter'
            break


def showmenu():
    while True:
        pr = '''
        (O)lduser
        (N)ewuser
        (Q)uit    '''
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
                if choice in 'qno':
                    break
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
                break
        if choice == 'o':
            olduser()
        if choice == 'n':
            newuser()
        if choice == 'q':
            break
if __name__ == '__main__':
    showmenu()