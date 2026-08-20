'''functions  --> arguments usage {variable length arguments}
           --> keyword variable length arguments (**kwars)

exception handling / scope of variables / built-in functions

exception handling -->  it is a mechanism that helps to respond or make the flow of execution
in normal way,without this errors will occur and disrup the flow of program

common exceptions --> ValueError,TypeError,IndexError,AttributeError,
zerodivision error,

syntax:

try:
    #code that will cause the exception
except exception as e:
    #code will catch the exception
finally:
#runs irrespective of try/except....

#basic exception handling

try:
    a=float(input("enter the value:"))
    result=20/a
    print(result)
#except Exception as e:

   # print(e)
except ValueError:
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possible') 
except NameError:
    print(f'Check the name of variable propoerly')

try:
    a=[10,20,30]
    a.apped(24)
    print(a[5])
except Exception as e:
    print(e)
except IndexError:
    print(f' check the length of list properly ')
except AttributeError:
    print(f'dont rush write the name properly')
    
#multiple exception handling

try:
    a=[10,20,30]
    a.apped(24)
    print(a[5])
except (IndexError,AttributeError) as e:
    print(e)
    a=list(map(int,input("enter the values:").split(',')))
    print(a)

#BMI --> bmi=(weight)/?((height)**2)
#feet=12 inches

while True:
    try:
        weight=int(input("enter the weight in kgs:"))
        height=float(input("enter the height in meters:"))
        if weight > 0 and height > 0:
            break
        else:
            print("make sure to enter only correct values")
    except ValueError:
        print(f'make sure to enter weight as integer only,height also as number')
bmi=((weight)/(height)**2)
print(bmi)
        
        
#else exception handling along with jumping statements in
#functions bmi taskscope of varibales --> scope is basically the region/area where it is
#accessible
#local scope,global scope
#global keyword,enclosing scopee(nested functions nonlocal keyword)
#local scope --> variables defined inside the function accessible inside

def display():
    name="codegnan"
    print(name)
display()
#print(name)#it is raises name error
#global
name="codegnan"
place="hyderabad"
def display():
        print(f'{name} is in {place}')
display()
print(name)
print(place)

count=20
def data():
    count=5 # local variable
    count=count+5
    print(f'value inside function is : {count}')
data()
print(f'value outside function is : {count}')'''

def outer():
    count=5
    def inner():
        nonlocal count
        count=count+10
        print(f'value inside is {count}')
    inner()
    print(f' value outside is {count}')
outer()
















    
