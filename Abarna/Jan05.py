from tkinter import *
r=Tk()
i=IntVar()
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
l1=Label(r,text="Select the Gender ")
l1.grid(row=5,column=1)
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
r1=Radiobutton(r,text="Male",variable=i,value=1)
r1.grid()

r1.grid(row=5,column=2)
r2=Radiobutton(r,text="Female",variable=i,value=2)
r2.grid(row=5,column=3)
b=Button(r,text="Submit",command=lambda:Submit())
b.grid(row=6,column=3)
r.mainloop()