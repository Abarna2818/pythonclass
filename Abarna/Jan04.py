'''
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combobox Example")
root.geometry('300x300')
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])
combo.pack()
root.mainloop()

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combobox Example")
root.geometry('500x500')
combo = ttk.Combobox(root,values=["India","Australia","New Zealand","Canada","Singapore"])
combo.pack()
root.mainloop()

'''
from tkinter import *
r=Tk()
r.geometry("500x500")
l1=Label(r,text="Enter the Name")
l1.grid(row=0,column=1)
l1=Label(r,text="Enter the Employee Number")
l1.grid(row=1,column=1)
l1=Label(r,text="Enter the Age")
l1.grid(row=2,column=1)
l1=Label(r,text="Enter the Salary")
l1.grid(row=3,column=1)
l1=Label(r,text="Enter the Experience")
l1.grid(row=4,column=1)
e1=Entry(r)
e1.grid(row=0,column=2)
e1=Entry(r)
e1.grid(row=1,column=2)
e1=Entry(r)
e1.grid(row=2,column=2)
e1=Entry(r)
e1.grid(row=3,column=2)
e1=Entry(r)
e1.grid(row=4,column=2)
b=Button(r,text="Submit",command=lambda:Submit())
b.grid(row=5,column=3)
r.mainloop()


