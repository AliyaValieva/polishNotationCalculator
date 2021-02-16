# 2*3+1

# 2 3 * 1 +

# 2*(3+1)

# 2 3 1 + *

# * + 1 2 3

# (2+1)*(4+3)

# 2 1 + 4 3 + * # reverse polish notation

# (2+1)*4-3

# 2 1 + 4 * 3 -

# stack:
# 1 # teh end of a stack
# 2

# import  operator as o
# o.add(x,y)
# first class object

import tkinter as tk

root = tk.Tk()
inputValue = tk.StringVar()
inputValue.set('') #

e = tk.Entry(root, borderwidth=5,textvariable=inputValue)
e.grid(column=0, row=0,columnspan=4) # side effect - change of other obj, or print on screen, its result will be None therefore
# "hello {0}, {1}".format(42,13)
button_1 = tk.Button(root,text='1',command=lambda: inputValue.set(inputValue.get()+'1'))
button_1.grid(column=0, row=1)
button_2 = tk.Button(root,text='2',command=lambda: inputValue.set(inputValue.get()+'2'))
button_2.grid(column=0, row=2)
button_3 = tk.Button(root,text='3',command=lambda: inputValue.set(inputValue.get()+'3'))
button_3.grid(column=0, row=3)
button_4 = tk.Button(root,text='4',command=lambda: inputValue.set(inputValue.get()+'4'))
button_4.grid(column=1, row=1)
button_5 = tk.Button(root,text='5',command=lambda: inputValue.set(inputValue.get()+'5'))
button_5.grid(column=1, row=2)
button_6 = tk.Button(root,text='6',command=lambda: inputValue.set(inputValue.get()+'6'))
button_6.grid(column=1, row=3)
button_7 = tk.Button(root,text='7',command=lambda: inputValue.set(inputValue.get()+'7'))
button_7.grid(column=2, row=1)
button_8 = tk.Button(root,text='8',command=lambda: inputValue.set(inputValue.get()+'8'))
button_8.grid(column=2, row=2)
button_9 = tk.Button(root,text='9',command=lambda: inputValue.set(inputValue.get()+'9'))
button_9.grid(column=2, row=3)

button_0 = tk.Button(root,text='0',command=lambda: inputValue.set(inputValue.get()+'0'))
button_0.grid(column=0, row=4,columnspan=2,sticky=tk.EW)

button_add = tk.Button(root,text='+',command=lambda: inputValue.set(inputValue.get()+'+'))
button_add.grid(column=3, row=1)

button_1 = tk.Button(root,text='+',command=lambda: inputValue.set(inputValue.get()+'+'))
button_1.grid(column=3, row=1)
button_2 = tk.Button(root,text='-',command=lambda: inputValue.set(inputValue.get()+'-'))
button_2.grid(column=3, row=2)
button_3 = tk.Button(root,text='x',command=lambda: inputValue.set(inputValue.get()+'x'))
button_3.grid(column=3, row=3)
button_4 = tk.Button(root,text='/',command=lambda: inputValue.set(inputValue.get()+'/'))
button_4.grid(column=3, row=4)

button_5 = tk.Button(root,text='=',command=lambda: inputValue.set(polish(inputValue.get())))
button_5.grid(column=2, row=5)

# dodelat proble, clear button
# button_5 = tk.Button(root,text=' ',command=lambda: inputValue.set(polish(inputValue.get())))
# button_5.grid(column=2, row=4)

button_6 = tk.Button(root,text='AC',command=lambda: inputValue.set(''))
button_6.grid(column=2, row=4)

button_7 = tk.Button(root,text='space',command=lambda: inputValue.set(inputValue.get() + ' '))
button_7.grid(row=4,column=3)
# ok



# row =4, col=2
# operat = ['+','-','x','/']
# for i in range(1,5):
#
#     print('''button_{1} = tk.Button(root,text='{0}',command=lambda: inputValue.set(inputValue.get()+'{0}'))
# button_{1}.grid(column=3, row={1})'''.format(operat[i-1],i))


# num = 1
# for i in range(3):
#     for j in range(1,4): # rows
#
#         print('''button_{0} = tk.Button(root,text='{0}',command=lambda: inputValue.set(inputValue.get()+'{0}'))
# button_{0}.grid(column={1}, row={2})'''.format(num,i, j))
#         num += 1  # meta programming - program creates another program

def polish(a):

    dict = {'+': lambda x, y: x + y, '-': lambda x, y: y - x, '*': lambda x, y: x * y}
    stack = []

    a = a.split()

    a = [int(i) if i.isdigit() else i for i in a]  # if after for will delete all non digits

    # if len(stack) == 1: stack += [0]

    for i in a:
        if isinstance(i, int):
            stack += [i]

        else:
            stack += [dict[i](stack.pop(),  # but also returns it
                              stack.pop())]



    return stack[0]  # the result is on the top of stack

# def operator(stack):
#     stack[0] += 0
#     return stack[0]
# REPL
# while True:
#      try:
#         a = input()
#         print(polish(a))
#      except IndexError:
#          # operator(polish())
#          print('Insufficient number of operands')

root.mainloop()
# f(x,y)

# a = [2,1,'+',4,'*',3,'-']
# 'f u 77'.split()
# a = '32 5 + 5 *'   -> ['32','5','+',...]

# data science
# REPL = read eval print loop

# statement(assigning to a var, for, if ) vs expression(calling func, can be part of statement)

# will not stop the program but will throw a message 'not enough arguments for the current operation'

# 4328=  4*10**3+3*10**2+2*10*1+8*10**0

# sum([4 * 10 ** 3, 3 * 10 ** 2, 2 * 10 * 1, 8 * 10 ** 0])


def convert_to_int(a):
    voc = dict([[str(i), i] for i in range(10)])
    rez = 0
    j = 0
    for i in a[::-1]:
        rez += voc[i] * 10 ** j

        j += 1
    return rez


# print(convert_to_int('4238'))

def convert_to_int(a):
    voc = dict([[str(i), i] for i in range(10)])
    return sum(voc[j] * 10 ** i for i, j in enumerate(a[::-1]))


# print(convert_to_int('4238'))


# 1 2 3

# move form 1 to 2
# ...
# 1 -> 3
# 2 -> 1
# func for side effect(look up)
def hanoi_tower(n, from_, to_, spare):
    if n == 0: return
    hanoi_tower(n - 1, from_, spare, to_)
    print('move from', from_, 'to', to_)
    hanoi_tower(n - 1, spare, to_, from_)  # razberus

# print(hanoi_tower(4, 1, 4, 3))
