'''OOP --> object oriented programming

--> attributes and methods
class,object -->4 class is a bluprint(template) for an object
an object is an instant (physical thing)which utilises the class

chair(object) --> wood,tools,dimesnsions(blueprint),carpenter
ecommerce platform
--> mobiles -> price,features,(camera,storage,RAM)
-->variables,def mobile()
-->laptops --> price,features
variables,def laptop()
-->carpets --> price,features


features of DOP-->modularity,scalability,encapaulation(binding the data to the class)
abstraction-->show only relevent information to the class
inhertitance-->one class to another class
single-->finger print access
multiple -->parents(mother/parent)-->child
multilevel-->grandparent-->parent-->child
polymorpysm-->methods overloading and method overriding,operator overriding

#syntax for class creation:

class Class_name:
    attributes (characteristics)
    ..........
    def func(self):(behaviour of the object)
        ..........
        ..........
    ...........

obj=Class_name()

class Student():
    name=input("enter the name:")
    id=input("enter the id:")
    gender=input("enter the gender:")
    email_id=input("enter email_id:")
    def display(self):
        print(f' Student name is {self.name:}')
        print(f' Student id is {self.id:}')
        print(f' Student email_id is {self.email_id:}')
u1=Student()
u1.display()
u2=Student()
u2.display()
print(u1.__dict__)#it returns empty dictionaries
print(u2.__dict__)#it returns empty dictionaries'''

#students details with multiple objects

class Student():
    def data(self,name,id,gender,email_id):
        self.name=name
        self.id=id
        self.gender=gender
        self.email_id=email_id
    def display(self):
        print(f' Student name is {self.name:}')
        print(f' Student id is {self.id:}')
        print(f' Student email_id is {self.email_id:}')
u1=Student()
u1.data("jyothi","909","female","jyothimalige9@gmail.com")
u1.display()
print(u1.__dict__)

u2=Student()
u2.data("ram","10","male","ram2e@gmail.com")
u2.display()
print(u2.__dict__)
































