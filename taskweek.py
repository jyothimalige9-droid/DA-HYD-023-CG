'''number=[20,10,30,20,40,20]
number.sort()
print("sorted:",number)
number.reverse()
print("reversed:",number)
search_num=int(input("enter the number:"))
if search_num in number:
    print("count:",number.count(search_num))
    print("first index:",number.index(search_num))
else:
    print("not found")
print("smallest:",min(number))
print("largest:",max(number))
print("total:",sum(number))'''


marks=[]
for i in range(3):
    val=int(input("enter the marks:"))
    marks.append(val)
marks.insert(0,90)
marks.extend()
if 75 in marks:
    marks.remove(75)
removed=marks.pop
print("popped value:",removed)
print("final list:",marks)
print("its length:",marks)
