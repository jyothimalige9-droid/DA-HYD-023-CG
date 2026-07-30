'''
#Numeric datatype -->int,float,complex,bool....

#input formatting -->accepting input from the user

#Accepting integer input form user

age=(float(input("enter the age:")))
print(age)
print(type(age))


age=(int(input("enter the age:")))
print(age)
print(bool(age))

name=input("enter the name:")
print(name)
print(type(name))

f5
marks=int("enter the  marks:")
print(marks)


    
b=input().split()
Mlritm spoorthy seven

age=(float(input("enter the age:")))
print(age)
print(type(age))

a=input("enter the values:")
print(a)

a=input("Enter the values:").split(',')
print(a)

#lists of integers

marks=list(map(int,input("enter the marks:").split(',')))
print(marks)

#now we want to accept 2 values from user

age,salary=map(int,input("enter the values:").split())
print(age,salary)

age,salary=map(float,input("enter the values:").split(','))
print(age,salary)
               
#accepting input from user --> int,float  --> input formatting

#operators --> operators perform operations between values (operands)
#7 types --> arithmetic,assignment,comparison,membership,identity,logical,bitwise

#arithmetic operators --> mathematical operations

print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5%3)
print(5//3)

a=3
b=2
print(a**b)

#area=length * breadth

length=3;breadth=5
area=length*breadth
print(area)

#assignment operator-->assign the values

name=45
name=name+5  #updating the value of name
print(name)
b=35
b-=name
print(b)


#comparision operators --> we compare the values --> boolean
# == (equal to), != (not equal), <(less than), >(greater than)
# <=(less than or equal to), >=(greater than or equal to)

age=25
print(age==25,age==35)

price=100
print(100>=price)

#membership operator(present or not present) -->in,not in

marks=[56,75,85,95]
print(35 not in marks)
print(75 in marks)


#logical operators logical decision making --> and,or,not
#and --> all conditions to be satisfied
#or --> any one condition to be satisfied

a=(25 in [25,45,65]) and 45 < 56
print(a)
b=45>56 or 65<56
print(b)
'''
#identitiy operators --> check for identity of an object --> id()
#is,is not

a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)


a=[1,2,3,4]
print(id(a))
c=a
print(c is a)






















