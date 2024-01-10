'''
class employee:
    def __init__(self,name,id,salary,project):
        self.name=name
        self.id=id
        self.salary=salary
        self.project=project
    def show__sal(self):
        print("Name:",self.name,'salary:',self.salary)
    def proj(self):
        print(self.name,'is working on',self.project)
    def setproj(self,project):
        self.project=project
emp=employee('Jack',102,10000,'python')
emp.show__sal
emp.setproj("java")
emp.proj()

class person:
    def fact(self):
        return"It is a person"
class student(person):
    def fact1(self):
        return"It is a student"
ram=student()
print(ram.fact())
print(ram.fact1())

def demo():
    n=5
    while n<15:
        val=n*n
        yield val
        n+=1
a=demo()
for i in a:
    print(i)

mytuple=("Apple","Avacado","Orange")
myiter=iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myit))

mystr="All is well"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

def value():
    Designation="Engineer"
    return lambda : "Hello" + Designation
message=value()
print(message())
'''
def outer(x):
    def inner(y):
        return x+y
    return inner
add_five=outer(5)
result=add_five(6)
print(result)


        