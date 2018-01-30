#!/usr/bin/env python
#模拟堆栈

stack = []

def pushit():
    stack.append(raw_input('Enter New string: ').strip())   #在堆栈（列表）中添加一个元素

def popit():
    if len(stack) == 0:                                     #删去堆栈中最新的一个元素
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed [',
        stack.pop()
        print ']'

def viewstack():                                            #查看堆栈中已有的元素
    print stack

CMDs = {'u' : pushit, 'o' : popit, 'v' : viewstack}         #字典

def showmenu():                                     
    pr = """
    p(U)sh
    p(O)o
    (V)iew
    (Q)uit
    Enter choice: """
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print '\nYou picked: [%s]'  %  choice
            if choice not in 'uovq':
                print 'Invalid option, try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()
if __name__ == '__main__':
    showmenu()