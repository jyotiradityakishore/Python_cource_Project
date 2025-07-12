from tkinter import *

window = Tk()
window.geometry("400x500")  # -----------> Tab Detail & Initialization
window.configure(bg="gray")
window.resizable()
window.title("Python Calculator")


def click_value(num):
    result = Entry_box.get()
    Entry_box.delete(0, END)
    Entry_box.insert(0, str(result) + str(num))


Entry_box = Entry(window, width=60, borderwidth=7, )
Entry_box.place(x=10, y=10)

butten_1 = Button(window, text="1", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(1))
butten_1.place(x=10, y=110)

butten_2 = Button(window, text="2", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(2))
butten_2.place(x=110, y=110)

butten_3 = Button(window, text="3", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(3))
butten_3.place(x=210, y=110)

butten_4 = Button(window, text="4", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(4))
butten_4.place(x=10, y=210)

butten_5 = Button(window, text="5", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(5))
butten_5.place(x=110, y=210)

butten_6 = Button(window, text="6", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(6))
butten_6.place(x=210, y=210)

butten_7 = Button(window, text="7", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(7))
butten_7.place(x=10, y=310)

butten_8 = Button(window, text="8", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(8))
butten_8.place(x=110, y=310)

butten_9 = Button(window, text="9", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(9))
butten_9.place(x=210, y=310)

butten_0 = Button(window, text="0", padx=30, pady=20, activeforeground="blue", activebackground="green",
                  command=lambda: click_value(0))
butten_0.place(x=10, y=410)


def equal():
    n2 = Entry_box.get()
    Entry_box.delete(0, END)
    global math
    if math == "add":
        f3 = i + int(n2)
        Entry_box.insert(0, str(f3))  # ------------> problem 1 (not printing in box)

    elif math == "sub":
        Entry_box.insert(0, i - int(n2))  # ------------> problem 2 (expecting string but got int instead)
    elif math == "mult":
        Entry_box.insert(0, i * int(n2))  # ------------> problem 3       ''   ''     ''
    elif math == "div":
        Entry_box.insert(0, i / int(n2))  # ------------> problem 4       ''    ''    ''


butten_Equal = Button(window, text="=", padx=80, pady=20, activeforeground="blue", activebackground="green",
                      command=equal)
butten_Equal.place(x=110, y=410)


def add():
    n1 = Entry_box.get()
    global math
    math = "add"
    global i
    i = int(n1)
    Entry_box.delete(0, END)


butten_Plus = Button(window, text="+", padx=35, pady=20, activeforeground="blue", activebackground="green", command=add)
butten_Plus.place(x=310, y=110)


def neg():
    n1 = Entry_box.get()
    global math
    math = "Neg"
    global i
    i = int(n1)
    Entry_box.delete(0, END)


butten_Neg = Button(window, text="-", padx=35, pady=20, activeforeground="blue", activebackground="green", command=neg)
butten_Neg.place(x=310, y=210)


def div():
    n1 = Entry_box.get()
    global math
    math = "Div"
    global i
    i = int(n1)
    Entry_box.delete(0, END)


butten_Div = Button(window, text="%", padx=30, pady=20, activeforeground="blue", activebackground="green", command=div)
butten_Div.place(x=310, y=310)


def clear():
    Entry_box.delete(0, END)


butten_Clr = Button(window, text="CLEAR", padx=20, pady=20, activeforeground="blue", activebackground="green",
                    command=clear)
butten_Clr.place(x=310, y=410)

window.mainloop()


