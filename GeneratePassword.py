from tkinter import *
import random as r

root = Tk()
root.title('Генератор пароля')
root.geometry('800x600+350+100')


def show_password():
    out.config(bg='#B0C4DE')
    out.delete(0.0, END)
    out.insert(END, get_password(spin_var.get(), rad_var.get(), rad_var2.get()))


def get_password(length, digits, symbols):
    password = ''
    if not digits and not symbols:
        for i in range(length):
            password += chr(r.choice((r.randint(65, 90), r.randint(97, 122))))
    elif digits and not symbols:
        for i in range(length):
            password += chr(r.choice((r.randint(65, 90), r.randint(97, 122), r.randint(48, 57))))
    elif not digits and symbols:
        for i in range(length):
            password += chr(r.choice((r.randint(33, 47), r.randint(58, 126))))
    else:
        for i in range(length):
            password += chr(r.randint(33, 126))
    return password


rad_var = IntVar()
rad_var.set(1)
rad_var2 = IntVar()
rad_var2.set(1)
spin_var = IntVar()


say_hello = Label(text='Добро пожаловать в генератор надежного пароля!', font=('Arial Bold', 13))\
    .grid(column=0, row=0, columnspan=4, ipadx=5, sticky=W)
say_enter = Label(text='Укажите количество символов (8-100):', font=('Arial Bold', 11))\
    .grid(column=0, row=1, ipadx=5, sticky=W)
spin = Spinbox(from_=8, to=100, width=7, textvariable=spin_var)\
    .grid(column=1, row=1, ipadx=1, sticky=W)
ask_digits = Label(text='Нужны ли цифры в пароле:', font=('Arial Bold', 11))\
    .grid(column=0, row=2, ipadx=5, sticky=W)
rad1 = Radiobutton(text='Да', value=1, variable=rad_var)\
    .grid(column=1, row=2, ipadx=0, sticky=W)
rad2 = Radiobutton(text='Нет', value=0, variable=rad_var)\
    .grid(column=2, row=2, ipadx=1, sticky=W)
ask_symbols = Label(text='Нужны ли символы в пароле:', font=('Arial Bold', 11))\
    .grid(column=0, row=3, ipadx=5, sticky=W)
rad2_1 = Radiobutton(text='Да', value=1, variable=rad_var2)\
    .grid(column=1, row=3, ipadx=0, sticky=W)
rad2_2 = Radiobutton(text='Нет', value=0, variable=rad_var2)\
    .grid(column=2, row=3, ipadx=1, sticky=W)
button = Button(text='Создать пароль', font=('Arial Bold', 11), bg='#B0C4DE', activebackground='#FFFFFF', command=show_password)\
    .grid(column=1, row=4, ipady=10, ipadx=5, pady=30, columnspan=3)
out = Text(width=68, height=2)
out.grid(column=0, row=5, columnspan=6, sticky=E)

root.mainloop()
