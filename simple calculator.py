from tkinter import *

root=Tk()
# title
root.title("CALCULATOR")
operator=""
text_input=StringVar()
# input
e=Entry(root,font=("arial",20,"bold"),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)

# defining a functions
def button_input(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)
def button_clear():
    global operator
    operator=""
    text_input.set("")
def button_equal():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
button7=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='7',command=lambda: button_input(7)).grid(row=1,column=0)
button8=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='8',command=lambda: button_input(8)).grid(row=1,column=1)
button9=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='9',command=lambda: button_input(9)).grid(row=1,column=2)
addition=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='+',command=lambda: button_input('+')).grid(row=1,column=3)

#------------------------------------------------------------------------------------------------------------------------------------
button4=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='4',command=lambda: button_input(4)).grid(row=2,column=0)
button5=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='5',command=lambda: button_input(5)).grid(row=2,column=1)
button6=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='6',command=lambda: button_input(6)).grid(row=2,column=2)
substraction=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='-',command=lambda: button_input('-')).grid(row=2,column=3)

#************************************************************************************************************************************
button1=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='1',command=lambda: button_input(1)).grid(row=3,column=0)
button2=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='2',command=lambda: button_input(2)).grid(row=3,column=1)
button3=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='3',command=lambda: button_input(3)).grid(row=3,column=2)
multiplication=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='*',command=lambda: button_input('*')).grid(row=3,column=3)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
button0=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='0',command=lambda: button_input(0)).grid(row=4,column=0)
equal=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='=',command=button_equal).grid(row=4,column=1)
clear=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='C',command= button_clear).grid(row=4,column=2)
division=Button(root,padx=16,pady=16,fg="black",bd=8,bg="powder blue",font=("arial",20,"bold"),text='/',command=lambda: button_input('/')).grid(row=4,column=3)

root.mainloop()
