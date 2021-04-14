from tkinter import *
root=Tk()
root.title("simple calaculator")
search=Entry(root,borderwidth=5)
search.grid(row=0,column=0,columnspan=3,padx=40,pady=10)

def button_click(num):
        current=search.get()
        search.delete(0,END)
        search.insert(0,str(current)+str(num))
        
def button_clear():
        search.delete(0,END)

def button_add():
        first_num=search.get()
        global f_num
        global math
        math="addition"
        f_num=int(first_num)
        search.delete(0,END)

def button_sub():
        first_num=search.get()
        global f_num
        global math
        math="subtraction"
        f_num=int(first_num)
        search.delete(0,END)

def button_mul():
        first_num=search.get()
        global f_num
        global math
        math="multiplication"
        f_num=int(first_num)
        search.delete(0,END)

def button_div():
        first_num=search.get()
        global f_num
        global math
        math="division"
        f_num=int(first_num)
        search.delete(0,END)

def button_equal():
        second_num=search.get()
        search.delete(0,END)

        if(math=="addition"):
                search.insert(0,f_num + int(second_num))
        if(math=="subtraction"):
                search.insert(0,f_num - int(second_num))
        if(math=="multiplication"):
                search.insert(0,f_num * int(second_num))
        if(math=="division"):
                search.insert(0,f_num / int(second_num))

        
        
        
button1=Button(root,text="1",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(1))
button2=Button(root,text="2",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(2))
button3=Button(root,text="3",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(3))
button4=Button(root,text="4",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(4))
button5=Button(root,text="5",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(5))
button6=Button(root,text="6",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(6))
button7=Button(root,text="7",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(7))
button8=Button(root,text="8",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(8))
button9=Button(root,text="9",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(9))
button0=Button(root,text="0",padx=40,pady=20,fg="black",bg="white",command=lambda:button_click(0))
button_add=Button(root,text="+",padx=39,pady=20,fg="black",bg="white",command=button_add)
button_sub=Button(root,text="-",padx=40,pady=20,fg="black",bg="white",command=button_sub)
button_div=Button(root,text="/",padx=39,pady=20,fg="black",bg="white",command=button_div)
button_mul=Button(root,text="x",padx=40,pady=20,fg="black",bg="white",command=button_mul)
button_equal=Button(root,text="=",padx=40,pady=20,fg="black",bg="white",command=button_equal)
button_clear=Button(root,text="clear",padx=31,pady=20,fg="black",bg="white",command=button_clear)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=1)
button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=0)
root.mainloop()
