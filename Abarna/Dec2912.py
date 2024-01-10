'''from tkinter import *
root=Tk()
for fm in['pink','blue','yellow','green','purple','black','orange']:
    Frame(height=50,width=50,bg=fm).pack()
root.mainloop()

'''
from tkinter import *
r=Tk()
r.geometry("500x500")
l1=Label(r,text="Enter the first value")
l1.grid(row=0,column=1)
l2=Label(r,text="Enter the second value")
l2.grid(row=1,column=1)
l3=Label(r,text="Enter the Result")
l3.grid(row=2,column=1)
e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)

def add():
 
    a=int(e1.get())
    b=int(e2.get())
    c=a+b  
    e3.insert(0,c)
b=Button(r,text="Add",command=add)
b.grid(row=3,column=3)
r.mainloop()
