from tkinter import *


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btncleardisplay():
    global operator
    operator = ""
    text_input.set('')


def btnequalinput():
    global operator
    evaluation = eval(operator)
    text_input.set(evaluation)
    operator = ""


def btnpercentage(number):
    global operator
    operation = float(eval(operator))
    per = operation * 100
    text_input.set(per)

root = Tk()

root.title('Calculator')
root.resizable(width=False, height=False)
root.attributes('-alpha', 0.9)
text_input = StringVar()
operator = ""

text_display = Entry(root, font='raleway 20', textvariable=text_input, justify='right').grid(columnspan=4, sticky='ewns')


b7 = Button(root, text='7', font='raleway 25', padx=15, command=lambda: btnclick(7)).grid(row=1, column=0)
b8 = Button(root, text='8', font='raleway 25', padx=15, command=lambda: btnclick(8)).grid(row=1, column=1)
b9 = Button(root, text='9', font='raleway 25', padx=15, command=lambda: btnclick(9)).grid(row=1, column=2)
percentage = Button(root, text='%', font='raleway 25', padx=16, command=lambda: btnpercentage('%')).grid(row=1, column=3, sticky='w')

b4 = Button(root, text='4', font='raleway 25', padx=15, command=lambda: btnclick(4)).grid(row=2, column=0)
b5 = Button(root, text='5', font='raleway 25', padx=15, command=lambda: btnclick(5)).grid(row=2, column=1)
b6 = Button(root, text='6', font='raleway 25', padx=15, command=lambda: btnclick(6)).grid(row=2, column=2)
division = Button(root, text='/', font='raleway 25', padx=26, command=lambda: btnclick('/')).grid(row=2, column=3, sticky='w')

b1 = Button(root, text='1', font='raleway 25', padx=15, command=lambda: btnclick(1)).grid(row=3, column=0)
b2 = Button(root, text='2', font='raleway 25', padx=15, command=lambda: btnclick(2)).grid(row=3, column=1)
b3 = Button(root, text='3', font='raleway 25', padx=15, command=lambda: btnclick(3)).grid(row=3, column=2)
multiple = Button(root, text='*', font='raleway 25', command=lambda: btnclick('*')).grid(row=3, column=3, sticky='we')

b0 = Button(root, text='0', font='raleway 25', padx=15, command=lambda: btnclick(0)).grid(row=4, columnspan=2, sticky='ewns')
b_period = Button(root, text='.', font='raleway 25', padx=19.5, command=lambda: btnclick('.')).grid(row=4, column=2)
subtraction = Button(root, text='-', font='raleway 25', padx=25, command=lambda: btnclick('-')).grid(row=4, column=3)

b_clear = Button(root, text='AC', font='raleway 25', padx=15, command=btncleardisplay).grid(row=5, columnspan=2, sticky='ewns')
b_equal = Button(root, text='=', font='raleway 25', padx=14, command=btnequalinput).grid(row=5, column=2)
addition = Button(root, text='+', font='raleway 25', command=lambda: btnclick('+')).grid(row=5, column=3, sticky='we')

root.mainloop()
