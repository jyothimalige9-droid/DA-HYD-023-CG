'''OOP--> class,object,methods(__init__)
encapsulation-->public,protected,private
inheritance -->it is one of key feature of oop where we inherit the properities(attributes/methods from one class to another
class  (base class (parent class) --> derived class (child class )
whatsupp -->personal User,bussiness User (catalog),community admin
features -->code reuse
code maintainability,polymorphysm,(method overriding,method overloading,operator overloading__add__,__str__)

Types of inheritance
 1.single inheritance(finger print)
    one child class inheriting properties from one parent class
 2.multiple inheritance(mother,father-->child)
    one child class inheriting properties from two parent classes
 3.multilevel inheritance(grandparent --> parent -->child)
    level by level
 4.hierarchical inheritance
    multiple child classes imheriting from single parent
 5.hybrid inheritance
    it can carry one or more type of inheritances


syntax:

class baseclass:
    statement(s)...
    class Derivedclass(baseclass):
        ..........
        .........

#whatsupp scenario-->personal user,bussiness user

class User:
    def send_message(self):
        print("sending message")
    def voice_call(self):
        print("making voice calls")
    def video_call(self):
        print("making video calls")
class Bussinessuser(User):
    #pass
    def create_catalog(self):
        print("Display products catalog")
u1=Bussinessuser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()
u1.create_catalog()   
        
#social media login --> users--> update_users

class Users:
    company="codegnan"
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname+self.lname
#u1=Users("saketh","kallepu")
#print(u1.full_name())
#print(u1.company)

class Update_users(Users):
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()
u1=Update_users("saketh","kallepu")
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2=Users("sai","jyo")
print(u2.full_name())
print(u2.company)'''

#what if we have constructor in child class else...

#father -->kid (property)

class Father:
    def __init__(self):
        self.property=1000000
    def father_property(self):
        print(f'father property is {self.property}')
class Kid(Father):
    def __init__(self):
        super().__init__()
        self.cash=200000
    def kid_property(self):
        print(f'kid final property is {self.cash+self.property}')
obj=Kid()
obj.father_property()
obj.kid_property()   

#parent class is having constructor and child class is having constructor
#super__init__()
#super__init__(args)
#super().method()-->method overriding 




















 






























    

        
 






























    
