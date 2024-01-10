'''a="Hello"
print (a)

a="Hai Everyone!"
print(a[10])

a="Hello,friends!"
print(a[2:5])

txt="The Best things in life!"
print("Best in txt")
print("Best not in txt")

a="Hello world!"
print(a[:5])

a="Hello world!"
print(a[-5:-2])

a="How are you!"
print(a.upper())
print(a.lower())
print(a)
print(a.strip())

a="hello"
b="world"
c=a+b
c=a+" "+b
print(c)

age=33
txt="My name is jack ,and I am {}"
print(txt.format(age))

a="Hello,world"
print(a.split(" "))

a=input("Enter the value:")
print(a)
a=int(input("Enter the value"))

x=5
print(x)
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x/=3
print(x)
x%=3
print(x)
x//=3
print(x)
x**=3
print(x)

a="i have a  good day"
print(a.replace("have","nice"))

a="Hai Friends"
print(a.replace("Hai","Hello"))

from tkinter import *
r=Tk()
i=IntVar()
r1=Radiobutton(r,text="new",variable=i,value=1)
r1.pack()
r2=Radiobutton(r,text="new1",variable=i,value=2)
r2.pack()
r3=Radiobutton(r,text="new2",variable=i,value=3)
r3.pack()
r.mainloop()

from tkinter import *
r=Tk()
i=IntVar()
r1=Radiobutton(r,text="Male",variable=i,value=1)
r1.pack()
r2=Radiobutton(r,text="Female",variable=i,value=2)
r2.pack()
r3=Radiobutton(r,text="Others",variable=i,value=3)
r3.pack()
r.mainloop()


from tkinter import *
root=Tk()
root.geometry('500x500')
l1=Label(root,text="Address")
l1.grid(row=0,column=0)
text1=Text(root,height="3",width="50")
text1.grid(row=0,column=1)
root.mainloop()

from tkinter import *
r=Tk()
r.geometry('500x500')
l1=Label(r,text="Contact Details")
l1.grid(row=0,column=0)
text1=Text(r,height="5",width="30")
text1.grid(row=0,column=1)
r.mainloop()

#Comparison Operator
a=50
b=25
print('a==b:',a==b)
print('a>b:',a>b)
print('a<b:',a<b)
print('a!=b:',a!=b)
print('a<=b:',a<=b)
print('a>=b:',a>=b)

'''
#Logical Operator
a=10
print('Is this statement true? :',a>5 and a<5)
print('Anyone statement is true? :',a>5 and a<12)
print('Each statement is true then return false and vice-versa:',not a>5 and a)


