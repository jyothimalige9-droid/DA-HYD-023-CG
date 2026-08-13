'''list,tuples...
#list --> mutable,ordered,heterogeneous

#index(),count(),copy()sort(),reverse()

details=['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index("codegnan"))
details.extend([7,21,45,21])
print(details.index(21))
print(details.index(21,6))

print(details.count(21))
print(details.count('python'))


data=['codegnan','saketh','python','java']

for obj in data:
    print(data.index(obj),":",obj)


#copy()---> shallow copy of the given collection

new=data.new()
print(new)
print(type(new))
print(len(new))

new[2]="agentic ai"
print(new)
print(data)

data.append=("saketh")
print(new)
print(data)

data=[1,4,5,[21,34,45],23]
print(data)
new=data.copy()
print(new)

new[3][2]='agents'
print(new)
print(data)

new[1]='python'
print(new)
print(data)
'''
marks=[14,65,-45,27,35]
'''print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
#marks.insert(2,"code")#strings not possible 
#marks.sort()
print(marks)
marks.reverse()
print(marks)
marks.sort()
print(marks)
print(marks[::-1])
#type,len,min,max,print

print(sorted("codegnan"))
print(sorted(['code',23,34,45]))#error
#tuples-->indexed,ordered,heterogeneous,immutable collection
#dimesnions,coordinates,database records

a=()
print(type(a))
print(len(a))

dimensions=1.5,2.5
print(dimensions)
print(len(dimensions))
print(type(dimensions))

#operations --> indexing,slicing,striding,membership,merging,repetition
courses=("pfs","jfs",("da","ds"),"agenticai",[100,6,6])
print(len(courses))
print(type(courses))
print(courses[3][2:])
courses[-1].append("codegnan")
print(courses)

courses=("pfs","jfs",("da","ds"),"agenticai",[100,6,6])

d=courses*2
print(d)
e=courses+(2,3,4,5)
print(e)

#tuples immutable-->count(),index()
courses=("pfs","jfs",("da","ds"),"agenticai",[100,6,6])

print(courses.index("agenticai"))
print(courses.index("agenticai"))
#print(couses.sort("agents")#attribute error not applicable

print(sorted(courses[-1]))
d=tuple(sorted((23,12,3,4,5)))
print(d)

#accept group of integers

a=tuple(map(int,input("enter the values:").split(',')))
print(a)
'''

#eval
a=eval(input("enter the list:"))
print(a)
print(type(a))

'''1)give the count of each repeating character
test case 1:programming

r is expecting 2 times
g is repeating 2 times
m is repeating 2 times'''

2)
r is expecting 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is repeating 2 times
index=[6,7]











































































































































































































































































































































































