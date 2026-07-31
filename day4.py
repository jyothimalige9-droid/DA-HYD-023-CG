'''Identity of operator --> checks the identity of an object --> id()
a=10
b=20
print(id(a))
print(id(b))
c=4
print(id(c))
print(a is b)
print(b is c)
print(5==5)

a=[2,3,4,5]
b=a
print(id(a))
print(id(b))
c=[1,2,3,4]
print(id(c))
print(a is not b)
print(a==c)

#Bitwise operators --> we perform bitwise operations over operands
#&(and),|(or),^(XOR),shifting operators(<<,>>)

a=10
b=5
#swaping two numbers
temp=a
a=b
b=temp
print(a)
print(b)

#number will be converted to binary format
print(5&3) #both 5 and 3 to be converted into binary and bitwise and is performed

print(5|3)  #bitwise OR

print(5^3) #bitwose XOR

print(5 and 3) #here and is logical operator checks for both existances
#returns 5 in above case

print(5 or 3) #returns 3 in this case

#leftshift operator << ,right shift operator

print(5 < 1)
print(5 << 1)

print(25 << 2)#convert 15 to binary and perform 2 times left shifting
print(15 >> 2)#same 2 lines right shifting

#input formatting --> input(),int(input()),float(input())
#yoy know --> single input
#2 or 3 inputs  --> map()
#group of integers --> list(map(int,input().split(','))

names=input("enter the names:").split(',')
print(names)

name1,name2=map(str(input("enter the names:").split(",")))
print(name1,name2)

#Tokens-->  n umeric datatypes --> operators --> flow of the program
#control block statements -->they control the flow of the program
#conditional statements --> if,else,(rely on condition to be executed)
#repetition statements (loops) --> for while

#Conditional statements -->if usage

Syntax:

if<conditon>:
statement(s)..
......

age=45
if age<=45:
    print("your age is :",age)
  
price=109
if price>105:
    print("price of the product:",price)

age=int(input("enter the age:"))
if age>18 and age in [19,20,21]:
    print("your age is:",age)
    
#if-else usage as below:
if<condition>:
    statement(s)...
    ......
else:
    stataement(s)......
    ........
........
        
'''
#vote eligibility --> to check his/her voter eligibility and give access..
age=int(input("enter the age:"))
if age>0:
 if age>=18:
    print("eligible")
 else:
    print("not eligible")
    print(age)
else:
    print("enter positive values")
#same case lets only nested --> if,else
    
    
























    
















