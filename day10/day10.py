'''sequences --> strings,lists,tuples,sets
mapping --> Dictionary

#lists --> collection of heterogeneous elements(items)
#where list is a index,ordered collection,mutable,heterogeneous elements,we use same braces to store the data

marks=[35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)

#operations :indexing,slicing,membership,merging,repetition'names[0]=names[0][::-1]
print(names[0][::2])
print(names[3])
print(len(marks[3]))
names[2]='python'
print(names)


nested list --> a list inside another list

names=['codegnan',25,4,6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(names[3])
print(names[0][:4])
print(names[0][4:])
print(names[0][:2])

]
'names[0]=names[0][::-1]
print(names[0][::2])
print(names[3])
print(len(marks[3]))
names[2]='python'
print(names)
names=['codegnan',25,4.6,[45,35,25,65],'DA23',34]
names[4]=['codegnan','pfs','jfs','da','aaa','ds']
print(names)
print(len(names))
print(names[4][0][4:])
print(names[4][1][1:])

names[2:4]='abhiram','sai','saketh','sairam'
names[1::4]='python','java'
print(names)

#in slicing whatever elements a pass as per the logic length keeps on increase
names=['codegnan',25,4.6,[45,35,25,65],'DA23',34]
names[4]=['codegnan','pfs','jfs','da','aaa','ds']
names[2:4]='abhiram','sai','saketh','sairam'
print(names)
names[3:6:2]=["python","java"]
print(names)


      
#create a nested list with strings ,lists,and work on indexing,slicing,striding,

#append(single element end of the list)
names=["codegnan","saketh"]
names.append("data")
print(names)
#names.append("analysis","agents")#cant pass 2 elements
names.append(["analysis","agents"])
print(names)
names[3].append("chatgpt")
print(names)

#extend() -->inserts multiple elements to the end of list
names=["codegnan","saketh"]
names.extend("analysis")
print(names)
names.extend(["analysis"])
print(names)
names=[]
names.extend("analysis")
print(names)

names.insert(0,'python')
print(names)
names.insert([1:4],['a','b'])#syntax error

#pop,remove,clear

#pop by default last,else given index
names=["codegnan","saketh"]
names.pop(0)
print(names)
'''
#remove() we can remove a specific value
names=[1,2,3,4,5]
'''names.remove(5)
print(names)'''

del names[1:3]
print(names)

names.clear()
print(names)


#data =['codegnan','saketh','python','java']
#ouput
0:codegnan
1:saketh
2:python
3:java















































