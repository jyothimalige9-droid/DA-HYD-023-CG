'''class car:
    """Understanding the usage of OOP"""
    def data(self,brand,price,color,name):
        self.brand=brand
        self.price=price
        self.color=color
        self.name=name
        #Methods(behaviour)
    def display(self):
        print(f'car brand  is {self.brand}')
        print(f'car price is {self.price}')
        print(f'car color is {self.color}')
        print(f'car name is {self.name}')
u1=car()
u1.data("bmw","2000000","red","i20")
u1.display() 
print(u1.__dict__)
u2=car()
u2.data("bmw","3000000","white","i20")
u2.display() 
print(u2.__dict__)


Constructor --> Instance methods --> public attributes encapsulation

constructor --> it is a special  method (__init__())

class Car:
    """Understanding the usage of Constructor"""
    def __init__(self,brand,price,color,name):
        self.brand=brand
        self.price=price
        self.color=color
        self.name=name
        #Methods(behaviour)
    def display(self):
        print(f'car brand  is {self.brand}')
        print(f'car price is {self.price}')
        print(f'car color is {self.color}')
        print(f'car name is {self.name}')
u1=Car("tata","nexon","9lakhs","blue")
u1.display()
print(u1.__dict__)
u2=Car("bmw","nexon","25lakhs","white")
u2.display()
print(u2.__dict__)

class Car:
    """Understanding the usage of Constructor"""
    def __init__(self):
        self.brand="bmw"
        self.price="50lakhs"
        self.color="white"
        self.name="sedans"
        #Methods(behaviour)
    def display(self):
        print(f'car brand  is {self.brand}')
        print(f'car price is {self.price}')
        print(f'car color is {self.color}')
        print(f'car name is {self.name}')
u1=Car()
print(u1.brand,u1.price,u1.color,u1.name)
u1.display()

encapsulation:
    it is one of the main feature of oop.
    it binds(bundles)the data (attributes)and the methods (beha into a single unit (class)-->multiple objects
  -->attributes-->public,proteted,private

#public attributes --> attributes defines inside the class(and can be modified outside the class
                                                           
class Codegnanportal:
    def __init__(self,username):
        self.user=username
    def display(self):
        print(f'student username is{self.user}')
u1=Codegnanportal(" jyothimalige")
u1.display()
print(u1.__dict__)          
u2=Codegnanportal(" pranayamalige")
u2.display()
print(u2.__dict__)       

#protected attributes --> we use single underscore before an
#attribute moreover it can be modified also outside the class
#and exev excessible is subclass'''


class Codegnanportal:
    def __init__(self,username,_otp,password):
        self.user=username
        self._otp=_otp#protected attribute
        self.__password=password
    def display(self):
        print(f'student username is{self.user}')
        print(f'student has received OTP is{self._otp}')
       # print(f'student password is {self.__password}')
u1=Codegnanportal(" jyothi",23456,"jyothi2644")
print(u1.__dict__)
print(u1._Codegnanportal__password)
def get_password(self):
    return "*****"
def set_password(self,new_password):
    if len(new_password<=6:
           print("wrong password not satisfied number of characters")
           else:
               self.__password=new_password
               print("new password
    

























#
