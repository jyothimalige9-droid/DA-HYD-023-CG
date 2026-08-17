'''sequences --> strings,lists,tuples,set,frozenset,
mapping-->dictionary

#sets --> a set is a unique collection of objects,unordered,mutable,hashing
#unordered,unique,hashing,heterogeneous
#set(),{}

a={}
print(type(a))#dictionary

a={123,234,345,567,234}
print(a)
print(type(a))
print(len(a))
#print(a[2])#beacause it is a list(type error)
print(234 in a)
print(a*2)#it removes duplicates ,it is not possible in sets
print(a+a)#type error

data={1,2,3,4,5,[22,23,34],4}
print(data)#no lists inside a set (hashing technique),lists are mutable

data={1,2,3,4,5,(22,23,34),4}
print(data)
print(len(data))
for i in data:
    print(i)
#methods on sets --> add(),update(),remove(),discard(),popo()
'''
names={'set','saketh','kiran','codegnan'}
'''print(names)
print(len(names))
names.add('python')
print(names)
#names.add('saketh','poll')
#print(names)
print.add(('poll','python'))
print(names)

da_names={'mani','akash','sai','sonu'}
names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
#remove,discard,pop,clear

da_names={'mani','akash','sai','sonu'}
da_names.remove('sai')
print(da_names)
#da_names.remove('sai')#key error (its removed already)
#print(da_names)
da_names.discard("sai")
da_names.discard("codegnan")#discard will remove an element if its present else it ignores

''''''
da_names.pop()
print(da_names)
da_names.pop()
print(da_names)
da_names.clear()
print(da_names)
da_names.add("sai")
print(da_names)
print(len(da_names))
print(type(da_names))
da_names.remove("sai")

da_names.update(["sai","akash"])
print(da_names)

#copy
da_names={'mani','akash','sai','sonu'}
d=da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)


#mathematical operations  --> union(),intersection(),difference(),symmetric
#issubset,issuperset,isdisjoint
'''
da_23={12,23,34,45,23,36}
da_24={34,46,47,23}|{23,2,12,12,78}
'''print(da_23.union(da_24))
print(da_23.intersection(da_24))

common=da_23.intersection_update(da_24)
print(common)
print(da_23)

diff=da_23.difference(da_24)
print(diff)
f=da_23-da_24
print(f)


symm=da_23.symmetric_difference(da_24)
print(symm)
h=da_23^da_24
print(h)'''

#issubset()
print(da_24.issubset(da_23))
print(da_23.issubset(da_24))

#isdisjoint
print(da_23.isdisjoint(da_24))
print(da_24.isdisjoint(da_23))













