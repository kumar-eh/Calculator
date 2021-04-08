from tkinter import *
from tkinter.messagebox import *
expression = ""


def onclick(num):
    global expression
    expression = expression + str(num)
    equ.set(expression)

def equal():
    try:
        global expression
        a = eval(expression)
        print(a)
        expression = str(a) 
        equ.set(expression)
    except ZeroDivisionError:
        a = "Division by zero not possible"
        expression = ""
        equ.set(a)
    except SyntaxError:
        a = "Syntax error"
        expression = ""
        equ.set(a)

def clear():
    global expression
    expression = ""
    equ.set(expression)


root = Tk()
root.title("Exp")
canvas = Canvas(root, width = 300 , height=400 , bg = "#111111")
canvas.pack()

Title_frame = Frame(canvas, bg= "#111111")
Title_frame.place(relx=0,rely=0,relwidth=1,relheight=0.3)

main_frame = Frame(canvas , bg = "#111111")
main_frame.place(relx= 0 , rely = 0.3 , relwidth = 1 , relheight = 0.7)

equ = StringVar()
number_display = Entry(Title_frame , textvariable = equ)
number_display.place(relx=0,rely=0,relwidth=1,relheight=1)

b1 = Button(main_frame ,highlightbackground='#000000' , command = lambda: onclick(1) ,  bg = "#111111" , text = "1" , height = 4 , width = 8)
b1.grid(row = 0 , column = 0 )

b2 = Button(main_frame ,highlightbackground='#000000', command = lambda: onclick(2), bg = "#111111" , text = "2" , height = 4 , width = 8)
b2.grid(row = 0 , column = 1 )

b3 = Button(main_frame ,highlightbackground='#000000', command = lambda: onclick(3) ,bg = "#111111" , text = "3" , height = 4 , width = 8)
b3.grid(row = 0 , column = 2 )

badd= Button(main_frame , highlightbackground='#ff9500' , command = lambda: onclick('+'), bg = "#111111" , text = "+" , height = 4 , width = 9)
badd.grid(row = 0 , column = 3 )

b4 = Button(main_frame  ,highlightbackground='#000000', command = lambda: onclick(4), bg = "#111111" , text = "4" , height = 4 , width = 8)
b4.grid(row = 1 , column = 0 )

b5 = Button(main_frame  ,highlightbackground='#000000', command = lambda: onclick(5), bg = "#111111" , text = "5" , height = 4 , width = 8)
b5.grid(row = 1 , column = 1 )

b6 = Button(main_frame  ,highlightbackground='#000000', command = lambda: onclick(6), bg = "#111111" , text = "5" , height = 4 , width = 8)
b6.grid(row = 1 , column = 2 )

bsub = Button(main_frame  , highlightbackground='#ff9500' , command = lambda: onclick('-'), bg = "#111111" , text = "-" , height = 4 , width = 9)
bsub.grid(row = 1 , column = 3 )

b7 = Button(main_frame  ,highlightbackground='#000000', command = lambda: onclick(7), bg = "#111111" , text = "7" , height = 4 , width = 8)
b7.grid(row = 2 , column = 0 )

b8 = Button(main_frame  ,highlightbackground='#000000', command = lambda: onclick(8), bg = "#111111" , text = "8" , height = 4 , width = 8)
b8.grid(row = 2 , column = 1 )

b9 = Button(main_frame  ,highlightbackground='#000000', command = lambda: onclick(9), bg = "#111111" , text = "9" , height = 4 , width = 8)
b9.grid(row = 2 , column = 2 )

bmul = Button(main_frame  , highlightbackground='#ff9500' , command = lambda: onclick('*'), bg = "#111111" , text = "*" , height = 4 , width = 9)
bmul.grid(row = 2 , column = 3 )

bc = Button(main_frame  , highlightbackground='#ff9500' , command = lambda: clear(), bg = "#111111" , text = "C" , height = 5 , width = 8)
bc.grid(row = 3 , column = 0 )

b0 = Button(main_frame  ,highlightbackground='#000000', command = lambda: onclick(0), bg = "#111111" ,fg = "#111111" ,  text = "0" , height = 5 , width = 8)
b0.grid(row = 3 , column = 1 )

bequal = Button(main_frame  , highlightbackground='#ff9500' , command = lambda: equal(), bg = "#111111" , text = "=" , height = 5 , width = 8)
bequal.grid(row = 3 , column = 2 )

bdiv = Button(main_frame  ,  highlightbackground='#ff9500' , command = lambda: onclick('/') ,text = "/" , height = 5 , width = 9)
bdiv.grid(row = 3 , column = 3 )

root.resizable(0,0)
root.mainloop()

