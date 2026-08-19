'''functions --> variables length arguments (*args)
          -->keyword variable length arguments (**kwargs)

variable length arguments --> the number of positional arguments are not limi
we can pass any number of arguments,but we need to use the * representation,
data is stored in tuple.

def sample(*args):
    print(args)
    print(type(args))
sample()
sample('codegnan','saketh',23)
details=[24,45,35,65]
sample(details)
sample(*details)

a,b,c=13,4,'da'
print(a,b,c)
#a,*b,c='python','codegnan',23,45,9,7,'data'
#a,b,*c='python','codegnan',23,45,9,7,'data'
a,b,*c=34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)

#task --> we wanted to calculate the sum of given objects using functions

def add(*a):
    print(a)
    print(type(a))
    result=0
    for i in a:
        if type(i)==int or type(i) == float:
            result=result+i
    return result
print(add())
print(add(12,3,4,5))
print(add(1,2,3,4,5))
print(add(3,4,5,'poll','dear',45,4.5))
print(add(23,4,5.5,2+4j,56,'code',23))
b=list(map(int,input("enter the values:").split(',')))
print(add(b))
print(add(*b))
for i in b:
    print(i,end="  ")

#keyword variable length arguments --> we can pass any number of keyword
arguments we use ** representation

def details(**kwargs):
    print(kwargs)
    print(type(kwargs))
details()
details(name="codegnan",place="hyd",batch="da")
batch={"number":"da23","place":"hyd"}
details(**batch)'''
def sample(*a,**b):
    result=0
    for i in a:
        if type(i) in (int,float,complex):
            result=result+i
    print(result)
    for key,value in b.items():
        print(f"key is {key}")
        print(f'value is {value}')
sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="hyd",
       batch ="da23")



















