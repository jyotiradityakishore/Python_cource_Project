from tkinter import *
window = Tk()
global i
global oprator
window.geometry("400x500",)
window.title("calculator")
window.resizable(False, False)
window.configure(background="#808080")


entry = Entry(window, width=60,border=7)
entry.place(x=10,y=10)

def button_clicked(num):
    result = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(result) + str(num))

button1 = Button(window, text="1", command=lambda: button_clicked(1), padx=30, pady=20,activebackground="green", activeforeground="white",bg="#E0E0E0")
button1.place(x=10,y=100)

button2 = Button(window, text="2", command=lambda: button_clicked(2), padx=30, pady=20,activebackground="green", activeforeground="white")
button2.place(x=110,y=100)

button3 = Button(window, text="3", command=lambda: button_clicked(3), padx=30, pady=20,activebackground="green", activeforeground="white")
button3.place(x=210,y=100)

button4 = Button(window, text="4", command=lambda: button_clicked(4), padx=30, pady=20,activebackground="green", activeforeground="white")
button4.place(x=10,y=200)

button5 = Button(window, text="5", command=lambda: button_clicked(5), padx=30, pady=20,activebackground="green", activeforeground="white")
button5.place(x=110,y=200)

button6 = Button(window, text="6", command=lambda: button_clicked(6), padx=30, pady=20,activebackground="green", activeforeground="white")
button6.place(x=210,y=200)

button7 = Button(window, text="7", command=lambda: button_clicked(7), padx=30, pady=20,activebackground="green", activeforeground="white")
button7.place(x=10,y=300)

button8 = Button(window, text="8", command=lambda: button_clicked(8), padx=30, pady=20,activebackground="green", activeforeground="white")
button8.place(x=110,y=300)

button9 = Button(window, text="9", command=lambda: button_clicked(9), padx=30, pady=20,activebackground="green", activeforeground="white")
button9.place(x=210,y=300)

button0 = Button(window, text="0", command=lambda: button_clicked(0), padx=30, pady=20,activebackground="green", activeforeground="white", )
button0.place(x=10,y=400)

def add():
    result = entry.get()
    entry.delete(0, END)
    global i
    global oprator
    i = int(result)
    oprator = "add"

def sub():
    result = entry.get()
    entry.delete(0, END)
    global i
    global oprator
    i = int(result)
    oprator = "sub"

def mult():
    result = entry.get()
    entry.delete(0, END)
    global i
    global oprator
    i = int(result)
    oprator = "mult"

def div():
    result = entry.get()
    entry.delete(0, END)
    global i
    global oprator
    i = int(result)
    oprator = "div"

def equal():
    num_2 = entry.get()
    entry.delete(0, END)
    global i
    global oprator
    if oprator == "add":
        result = i + int(num_2)
    elif oprator == "sub":
        result = i - int(num_2)
    elif oprator == "div":
        if int(num_2) == 0:
            entry.insert(0, "can't divide by zero")
        else:
            result = i / int(num_2)
    elif oprator == "mult":
        result = i * int(num_2)


    entry.insert(0, str(result))

def clear():
    entry.delete(0, END)

button_ad = Button(window, text="+", command=add, padx=34, pady=20,activebackground="green", activeforeground="white",bg="#99FFFF")
button_ad.place(x=300,y=100)

button_ne = Button(window, text="-", command=sub, padx=34, pady=20,activebackground="green", activeforeground="white",bg="#99FFFF")
button_ne.place(x=300,y=200)

button_dv = Button(window, text="/", command=div, padx=34, pady=20,activebackground="green", activeforeground="white",bg="#99FFFF")
button_dv.place(x=300,y=300)

button_ml = Button(window, text="X", command=mult, padx=34, pady=20,activebackground="green", activeforeground="white", bg="#99FFFF")
button_ml.place(x=300,y=400)

button_eq = Button(window, text="=", command=equal, padx=80, pady=20,activebackground="green", activeforeground="white",bg="#66FF66")
button_eq.place(x=100,y=400)

button_cl = Button(window, text="CLEAR", command=clear, padx=166, pady=10,activebackground="green", activeforeground="white", bg="#FF6666")
button_cl.place(x=10,y=50)
mainloop()
