'''strings --> Caseconversions ,searching and finding
string testing methods ,replace space removal

#searching ,finding ,replacing
a ="codegnan"
print(len(a))
print(min(a))
print(max(a))
b=a.index('g')
print(b)
c=a.index('n')
print(c)
d=a.index('n',6)
print(d)

#e=a.index('n',8)
#print(e)
#f=a.indexx('t')
#print(f)

a="codeganana"
b=a.index('a')
print(b)
c=a.index('a',8)
print(c)
d=a.index('a',4,8)
print(d)

#rindex-->returns last ocuurance
a="codegnan"
b=a.rindex('g')
print(b)
c=a.rindex('n',4,6)
print(c)

#count -->returns the number of times the object is repeating
print("codegnan".count('n'))
print("code".count('w'))
print("jfeyfwdgdgfhwgdvghdf".count('d'))

#find()-->first occurance but it returns -1 if substring is not found 
print('codegnan'.find('r'))
print('codegnan'.find('n'))

a="codegnan"
print(len(a))
for i in a:
    print(a.count(i))

#replacing,splitting,joining
#strings are imuutable

a="codegnan"
print(a.replace("g","s"))

a="code,saketh,python"
b=a.split()
print(b)
c=a.split(',')
print(c)


a="code"
b="gnan"
print(a.join(b))
print(b.join(a))
print(a.join(a))
print('#'.join('saketh'))
print(' '.join('saketh'))

#string testing methods (boolean)
#isaalpha(),isalnum,is digit(),isupper(),is lower()......

a='Codegnan123'
print(a.isalnum())#returns alpha and num
print(a.isalpha())#returns alpha
print(a.isdigit())
print(a.isupper())
print(a.islower())
print("9030253009".isdigit())
print("2345".isnumeric())
print("codegnan".startswith('n'))
print("codegnan".startswith('g',4))

print('codegnan'.islower())
print('Codegnan'.isupper())
print('Codegnan Python'.istitle())'''

a="  codegnan"
print(a.strip())
b=input("enter the string:").strip().lower()
print(b)


































































































