'''word=input("enter the word:")
a=word.upper()
print("upper:",a)
b=word.lower()
print("lower:",b)
c=word.title()
print("title:",c)
d=word.capitalize()
print("capitalize:",d)
e=word.swapcase()
print("swapcase:",e)



print("STUDENT REPORT".center(40))
print("Name".rjust(10),"Marks".rjust(10),"Grade".rjust(10))

for name,marks in [("Asha",85),("Rahul",63),("John",35)]:
    if marks>=80:
        grade="A"
    elif marks>=60:
        grade="B"
    elif marks>=40:
        grade="C"
    else:
        grade="Fail"

    print(name.ljust(10),str(marks).rjust(5),grade.rjust(10))n=input('enter the user:')
while n!=quit:
    if n.isalnum:
        print('contains only the letters and numbers')
    if n.isidentifier:
        print('vaild python identifier')
    if n.isascii:
        print('contains only ascii values')
    if n.isalpha:
        print('contains the letters')
    else:
        print('null')
    n=input('enter the user:')'''

text = input("Enter a line of text: ")

letters = 0
digits = 0
spaces = 0
printable = 0
non_printable = 0

for ch in text:
    if ch.isalpha():
        letters += 1

    if ch.isdigit():
        digits += 1

    if ch.isspace():
        spaces += 1

    if ch.isprintable():
        printable += 1
    else:
        non_printable += 1

print("\n----- TEXT REPORT -----")
print("Letters       :", letters)
print("Digits        :", digits)
print("Spaces        :", spaces)
print("Printable     :", printable)
print("Non-printable :", non_printable)
print("Lower case    :", text.islower())
print("Upper case    :", text.isupper())
print("Title case    :", text.istitle())























