'''class father:
    """usage of constructor in single inheritance"""
    def __init__(self,property):
        self.property=property
    def father_property(self):
        print(f'father property is {self.property}')
class kid(father):
    """now childclass will have constructor"""
    def __init__(self,cash,property):
ll;        self.cash=cash
        super().__init__(property) #calls superclass constructor with arguments
    def kid_property(self):
        print(f'kid property is {self.cash}')
        print(f'kid final property is {self.cash+self.property}')
obj=kid(250000,100000)
obj.kid_property()
obj.father_property()


#what if child class is haveing same method name as parent class-->method overriding
#area of square/rectangle


class square:
    """method overriding usage"""
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'area of square is {self.x**2}')
class Rectangle(square):
    def __init__(self,x,y):
        self.y=y
        super().__init__(x)
    def area(self):
        super().area()
        print(f'area of rectangle is {self.x * self.y}')
x,y=map(int,input("enter the values:").split(','))
obj=Rectangle(x,y)
obj.area()

#multiple inheritance

class parent1:
    .........
class parent2:
    ........
    class child(parent1,parent2):
        .......
....

class User:
    def voice_call(self):
        print("making voice Calls")
class Notifications:
    def notifications(self):
        print("sending notification..")
class premiumUser(User,Notifications):
    def verification_badge(self):
        print("blue Tick verififcation code")

user=premiumUser()
user.verification_badge()
user.voice_call()

#multilevel inheritance-->kevel by level

class grandparent:
    ...........
class parent(grandparent):
    ...........
class child(parent):
    ........'''

class user:
    def video_call(self):
        print("making video calls")
class bussinessuser(video_call):
    def create_controller(self):
        print("making create controlling")
class verify_bussinessuser(bussinessuser):
    def bluetick(self):
        print("blue tick verification code")
user=verify_bussinessuser()
user.bluetick()
user.video_call()
user.create_controller()




























    























