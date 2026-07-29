'''

Tokens --> variables,punctuators

variables-->Named memory location,its a place holder for data
#Rules are to be followed

#Multi assignment of varibales

name,age,place='codegnan',7,'hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep=',')

#Reassigning varibales

name="codegnan"
a,b=15,12
print(a,b)
a,b=b,a
print(a,b,sep=',')

#Deleting the variables

del a

#punctuators-->lists,tuples,{},(dict,sets)

name='codegnan';age=7

#Datatypes --> Numeric (int,float,complex),boolen,None
#sequences --> list,tiples,sets,strings,frozensets,mapping(dictionary)


#Numeric types --> int,float,complex

age=7
print(age)
print(type(age))
print(type(234))
print(type(12.5))

quantity=3  #it is not allowed(starting with 0)

#float datatype --> temp,salary,price

price=750.2;discount=2.5
print(price,discount)
print(type(price))

#complex -->combination of real and imaginary
i2=4
data=5+i2
print(data)
print(type(data))

data=5+2j
print(data)
print(type(data))

#Boolean  --> True/False
valid=True
print(valid)
print(type(valid))

#Typecasting --> Converting ont type to another type
#python by default follows implicit type(we need not mention the datatype)

#we will go for explicit conversion

#Every built-in datatype is a built-in function
'''
#typecastins --> int,float,complex,bool

age=35
print(type(age))
b=float(age)
print(b)

age=45.4
print(type(age))
b=int(age)
print(b)

price=50+0j
print(type(price))
b=bool(price)
print(b)

e=int(float(bool(45)))
print(e)

f=45+2.5+2+3j+True
print(f)

















