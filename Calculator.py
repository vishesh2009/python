from tkinter import *
import math
from math import sin, cos, tan, sqrt
root = Tk() #
root.geometry("700x840")

root.title("The best calculator") 
root.config(bg="Dark Blue")
root.resizable(height=False,width=False)
###################Starting with functions ####################
# 'btn_click' function :
# This Function continuously updates the
# input field whenever you enter a number

def btn_click(item):
    global expression
    expression=input_text.get()
    expression = expression + str(item)
    input_text.set(expression)

#-----------------------------------------------------------------------------------------------
def bt_clear():
    global expression
    expression = ""
    input_text.set("")
 
# 'bt_equal':This method calculates the expression
# present in input field

#-----------------------------------------------------------------------------------------------

def squareroot():
    global experession
    expression=input_text.get()
    result = str(eval(expression))
    vibgyor =  math.sqrt(float(result))
    
    input_text.set(vibgyor)
    
    
#---------------------------------------------------------------------------------------------------
pisymbol='π'  
multiply="*"


def pie():
         global expression
         global pisymbol
         expression=input_text.get()
         if expression=="":

             expression=str(expression) + str(pisymbol)
             input_text.set(expression)

         else:
             expression=str(expression) + "*" +str(pisymbol)
             CodeX = expression.replace("*","",-1)
             

         input_text.set(CodeX)      
#-----------------------------------------------------------------------------------------------
def delete():
    global experession
    expression=input_text.get()
    a=len(expression)
    b=str(expression[0:a-1])
    expression=b
    input_text.set(b)                                               
   
#-----------------------------------------------------------------------------------------------
def bt_equal():
    try:
        global expression
        pi=22/7
        expression=expression.replace("²", "**2",-1)
        expression=expression.replace("³", "**3",-1)
        
        expression=expression.replace("^", "**",-1)
        
        expression=expression.replace("π", str(pi),-1)
        if expression == "":
            expression=expression.replace("π", str(pi),-1)
        else:
            if expression[-1]=="+" or "-" or "*" or "/":
                expression=expression.replace("π",str(pi),-1)
            else:
                expression=expression.replace("π", str(pi),-1)
                input_text.set(expression) 
        if "√" in expression:
            expression=expression.replace("√", "",-1)
            result = str(eval(expression)) 
            
            vk=math.sqrt(int(expression))
            
            input_text.set(vk)
        result = str(eval(expression)) 
        input_text.set(result)
        expression = ""
    
    
      
    except:
        input_text.set("OH! COULD NOT EVALUATE THE EXPRESSION")
        #input_text.set("OH! YOU DUMBO CAN U PUT A PREETY FUNCTION")
        expression=""
expression = ""
#----------------------------------------------------------------------------------------------- 
# 'StringVar()' :It is used to get the instance of input field 
 
input_text = StringVar()
firstnum = str()
secondnum = str()
mathsign = str()
current = "" 
defxworking = False
# Let us creating a frame for the input field
 
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)

input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="red", bd=0, justify=RIGHT, state = "disabled", disabledforeground = "Lime", disabledbackground="Black")
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'

btns_frame = Frame(root, width=312, height=272.5,bg="Blue")
 
btns_frame.pack()
 
# first row
#Clear Button 
clear = Button(btns_frame, text = "Clear", fg = "black", width = 40, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: bt_clear(),font=('Helvetica', 8, 'bold','italic')).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1,sticky=W+E)
#divide 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click("/"),font=('Helvetica', 8, 'bold','italic'), activebackground='White').grid(row = 0,column = 3, padx = 1, pady = 1,sticky=W+E)
 
# second row
#Seven 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(7 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 1, column = 0, padx = 1, pady = 1,sticky=W+E)
#Eight 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(8 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 1, column = 1, padx = 1, pady = 1,sticky=W+E)
#Nine 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(9 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 1, column = 2, padx = 1, pady = 1,sticky=W+E)
#Multiply 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click("*"),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 1, column = 3, padx = 1, pady = 1,sticky=W+E)
 
# third row
#Four 
four = Button(btns_frame, text = "4", fg = "black", width = 13, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(4 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 2, column = 0, padx = 1, pady = 1)
#Five 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(5 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 2, column = 1, padx = 1, pady = 1,sticky=W+E)
#Six 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(6 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 2, column = 2, padx = 1, pady = 1,sticky=W+E)
#Minus 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click("-" ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 2, column = 3, padx = 1, pady = 1,sticky=W+E)

pie = Button(btns_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = pie,font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 6, column = 0, padx = 1, pady = 1,sticky=W+E,columnspan=1) 
# fourth row
#One 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(1 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 3, column = 0, padx = 1, pady = 1,sticky=W+E)
#Two 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(2 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 3, column = 1, padx = 1, pady = 1,sticky=W+E)
#Three
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(3 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 3, column = 2, padx = 1, pady = 1,sticky=W+E)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click("+"),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 3, column = 3, padx = 1, pady = 1,sticky=W+E)
 
# fourth row
delete = Button(btns_frame, text = "⌦", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command =delete,font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 7, column = 1, padx = 1, columnspan = 1 ,pady = 1,sticky=W+E)

sqrt = Button(btns_frame, text = "√x", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command =squareroot,font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 7, column = 0, padx = 1, columnspan = 1 ,pady = 1,sticky=W+E)

zero = Button(btns_frame, text = "0", fg = "black", width = 26 , height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(0 ),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 4, column = 0,columnspan = 2, padx = 1, pady = 1,sticky=W+E)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click("."),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 4, column = 2, padx = 3, pady = 1,sticky=E+W)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 9, height = 3, bg = "red", cursor ="hand2", command = lambda: bt_equal(),font=('Helvetica', 8, 'bold'), activebackground="White").grid(row = 4, column = 3, padx = 1, pady = 1,sticky=W+E)

doublezero = Button(btns_frame, text = "00", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click("00"),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 5, column = 0, columnspan = 1, padx = 1, pady = 1,sticky=W+E) 

oneby = Button(btns_frame, text ="1/x", fg = "black", width = 10, height = 3, bd = 0, bg="red", cursor= "hand2", command = lambda: btn_click("1/"),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 5, column=2, padx =1, pady=1,columnspan = 1,sticky=W+E) 


quit = Button(btns_frame, text= "Quit", fg="black", width = 10, height = 3, bd = 0, bg="red" , cursor="hand2", command=btns_frame.quit,font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row=5, column=3, padx=1, pady=1,sticky=W+E)

 
percentage = Button(btns_frame, text = "%", fg = "black", width = 9, height = 3, bd = 0, bg="red", cursor= "hand2", command = lambda: btn_click("/100 *"),font=('Helvetica', 8, 'bold'), activebackground="White").grid(row = 5, column=1, padx =1, pady=1, columnspan = 1,sticky=W+E)



bracket_open = Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click("("),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 7, column =2, columnspan = 1, padx = 1, pady = 1,sticky=W+E)


bracket_close = Button(btns_frame, text =")", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(")"),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 7, column = 3, columnspan = 1, padx = 1, pady = 1,sticky=W+E)

xsquare = Button(btns_frame, text = "x²", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2",command=lambda: btn_click("²"),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 6, column = 1, columnspan = 1, padx = 1, pady = 1,sticky=W+E)

xcube = Button(btns_frame, text = "x³", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2",command=lambda: btn_click("³"),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 6, column = 2, columnspan = 1, padx = 1, pady = 1,sticky=W+E)



exp = Button(btns_frame, text = "x^y", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2",command=lambda: btn_click("^"),font=('Helvetica', 8, 'bold','italic'), activebackground="White").grid(row = 6, column = 3, columnspan = 1, padx = 1, pady = 1,sticky=W+E)



root.mainloop()
