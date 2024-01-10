'''
a="hello"
print(a)

i=int(input("Enter the value:"))
a=1
while(i>0):
    print(a)
    a=a*i
    i-=1
    print(a)

    
a=int(input("Enter the value:"))
n=a
c=0
while(a>0):
    r=a%10
    c=(c*10)+r
    a//=10
    print(c)
if(n==c):
    print("It is palindrone:")
else:
    print("It is not palindrone:")


def my__function(food):
    for x in food:
        print(x)
fruits=["apple","banana"]
my__function(fruits)


def my__func(n):
    return lambda a:a*n
m=my__func(2)
print(m(11))
print(m(45))    
'''
class person:
 def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
 def printname(self):
    print(self.firstname,self.lastname)
class student(person):
 def __init__(self,fname,lname,year):
    super().__init__(fname,lname)
    self.graduationyear=year
x=student("mike","jack",2010)
print(x.graduationyear)
x.printname()