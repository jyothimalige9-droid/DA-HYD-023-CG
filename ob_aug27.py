'''polymorphysim operator overloading

print(3+4) #addition
print('code'+'gnan')  #concatination 
print([23,45]+[4,5])
#print(3,__add__(4))
a=25;b=3
print(a.__add__(b))
a=[12,3,4];b=[3,4,5]
print(a.__add__(b))
print(a.__len__())
print(a.)

#let's apply the above scenario hotstar watch history

class Watchhistory:
    def__init__(self,hours):
    self.hours=hours
varun=watchhistory(100)
print(varun.hours)
akash=watchhistory(120)
print(akash.hours)
#print(varun+akash)
print(varun.hours + akash.hours)'''

class watchhistory:
    def __init__(self,hours):
         self.hours=hours
    def __add__(self,other):
        return self.hours + other.hours
    def __str__(self):
        return f'watchhistory is {self.hours}'
varun = watchhistory(300)
print(varun)
print(varun.hours)
akash =watchhistory(50)
print(akash)
print(varun+akash)






