'''key=2345
secret_key=int(input("enter the secret_key:"))

while True:
    if secret_key==key:
        print("you entered secret_key is correct")
        break
    else:
        print("you entered secret_key is incorrect")
        secret_key=int(input("enter the secret_key again:"))


otp=1234
password=int(input("enter the password:"))
current=0
max=7
while current<max:
    current=current+1
    if password==otp:
        print("otp successfull")
        break
    else:
        print("otp unsuccessfull")
        if current==max:
            print("unlock")
            break
        password=int(input("enter the password again:"))

food=input("enter the food items:")
count=0
while food!='exit':
    count=count+1
    food=input("enter the food items again:")    
print("total",count)

'''

cse = "python"
language = input("Enter the language: ")

current = 0
max = 3

while current < max:
    current += 1

    if language == cse:
        print("correct")
        break
    else:
        print("wrong")

        if current == max:
            print("unlock")
            break

        language = input("Enter the language again: ")
