# from tkinter import *
# r=Tk()
# r.geometry("600x600")
# l1=Label(r,text="Enter the first value")
# l1.grid(row=0,column=1)
# l2=Label(r,text="Enter the second value")
# l2.grid(row=1,column=1)
# l3=Label(r,text="Enter the result ")
# l3.grid(row=2,column=1)
# e1=Entry(r)
# e1.grid(row=0,column=2)
# e2=Entry(r)
# e2.grid(row=1,column=2)
# e3=Entry(r)
# e3.grid(row=2,column=2)
# def add():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a+b
#     e3.delete(0,END)
#     e3.insert(0,c)
# def sub():
#     d=int(e1.get())
#     e=int(e2.get())
#     f=d-e
#     e3.delete(0,END)
#     e3.insert(0,f)
# def mul():
#     g=int(e1.get())
#     h=int(e2.get())
#     i=g*h
#     e3.delete(0,END)
#     e3.insert(0,i)
# def div():
#     j=int(e1.get())
#     k=int(e2.get())
#     l=j%k
#     e3.delete(0,END)
#     e3.insert(0,l)
# b1=Button(r,text="Add",command=lambda:add())
# b2=Button(r,text="sub",command=lambda:sub())
# b3=Button(r,text="mul",command=lambda:mul())
# b4=Button(r,text="div",command=lambda:div())
# b1.grid(row=3,column=3)
# b2.grid(row=4,column=3)
# b3.grid(row=5,column=3)
# b4.grid(row=6,column=3)
# r.mainloop()



from tkinter import *


def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)


root = Tk()
var = IntVar()

R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                 command=sel)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                 command=sel)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                 command=sel)
R3.pack(anchor=W)

label = Label(root)
label.pack()
root.mainloop()


