'''num=0
for i in [200,300,400]:
    num=num+i
print(num)

password = input("Enter a password: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for ch in password:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Uppercase letters :", uppercase)
print("Lowercase letters :", lowercase)
print("Digits            :", digits)
print("Special characters:", special)
'''

email=input().split()
for mail in email:
    print(mail.split("@")[1])


movie=list(map(int,input("enter the movie:").split('.')))
for i in movie():
    print(





















