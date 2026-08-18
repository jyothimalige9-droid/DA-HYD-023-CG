'''tokens,datatypes --> control flow statements --> if,elif,else,for,while,break
continue....

procedure oreiented programming
functions--< is a block of code to perform a specific task,its a reusable block of code,where we define using
def keyword
advatanges of functions are:
1.code reuasability
2.code maintainability
3.debugging
4.avoiding code duplication....
5.modularity

len()
min()
max()
print()
type()
sorted()
eval()
map()

def fname(parameters):
    """doc string"""//description
    statements().....
    ........
    return value(s)
fname(args)

#to perform sum of given objects

def add(a,b):
   c=a+b
   return c
print(add(12,3))#adding
print(add("code","gnan"))#concatenation
print(add([12,5],[12,34]))#merging
c,d=map(int,input("enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    print(a+b)
add(12,35)

#usage of return
name,age,salary='jyothi',20,30000
def details():
    return name,age,salary
print(details())

there are 5 types of arguments:'

--> positional arguments
--> default  ""
--> keyword  ""
--> variable length ""
--> keyword varibale ""

#positional arguments --> number of arguments in function define should
#match with function call (order has to be maintained)

def details(name,place):
     return name,place
print(details("codegnan","hyderabad"))
print(details("sai","vizag"))
print(details("vizag","shyam",34))#its shows typeerror because we give 2 parameters in the function

def details(name,place):
    name(name is {name})
    place(place is {placed})
c,d=map(str,input("enter the values:").split(','))
details(c,d)

def grocery(item="cheese",price=35):
    print(f"the item is {item} and price is {price}")
grocery()
grocery("milk",32)
grocery("bread")
grocery("bread",45)
'''

#keywords arguments --> whenever we want to specify the name of argument
def employee(name,salary,role,place="codegnan"):
    print(f"employee name is {name},and salary is {salary},and role is {role},and place is {place}")
employee("sai",20000,"admin")
employee(25000,"controller","asha")                 
employee("akash",25000,"it","jspiders")






















































