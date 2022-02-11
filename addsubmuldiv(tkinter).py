from tkinter import *

root = Tk()
root.geometry("500x500")

Num1 = Entry(root)
Num1.pack()

Num2 = Entry(root)
Num2.pack()

def add():
    Number = int(Num1.get()) + int(Num2.get())
    label1 = Label(root,text=f"{Number}")
    label1.pack()
    
def sub():
	Subtract = int(Num1.get()) - int(Num2.get())
	labels = Label(root, text= f"{Subtract}")
	labels.pack()
	
def mul():
	Subtract = int(Num1.get()) * int(Num2.get())
	labelm = Label(root, text= f"{Subtract}")
	labelm.pack()
	


def div():
	division = int(Num1.get()) / int(Num2.get())
	labeld = Label(root, text= f"{division}")
	labeld.pack()

Button1 = Button(root,text="Add the numbers",command=add)
Button1.pack()

Button2 = Button(root,text="Subtract  the numbers",command=sub)
Button2.pack()

Button3 = Button(root,text="Multiply  the numbers",command=mul)
Button3.pack()

Button4 = Button(root,text="Divide  the numbers",command=div)
Button4.pack()

root.mainloop()