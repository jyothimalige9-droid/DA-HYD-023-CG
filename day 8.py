'''Usage of else with for --> the else keyword will only be executed

# for with else
work_log = [0, 1, 1, 1, 0, 1, 0]

longest = current = 0
for x in work_log:
    current = current + 1 if x else 0
    longest = max(longest, current)

current = 0
for x in work_log[::-1]:
    if x:
        current += 1
    else:
        break

print("Longest:", longest)
print("Current:", current)

work_log = [0, 1, 1, 1, 0, 1, 0]

longest = current = 0

for x in work_log:
    if x == 1:
        current += 1          
        longest = max(longest, current)
    else:
        current = 0

print("Longest streak:", longest)

current = 0
for x in work_log:      
    if x == 1:
        current += 1
    else:
        break               

print("Current streak:", current)



worklog = [0, 1, 1, 1, 0, 1, 0]

current = 0
longest = 0

for day in worklog:
    if day == 1:
        current += 1
        if current > longest:
            longest = current
    else:
        current = 0

print("Current Streak:", current)
print("Longest Streak:", longest)

# for-else
notifications =[0,0,0,0]
notifications =list(map(int,input("enter the values --> 0 or 1:").split('.')))
print("notifications")
for notification in notifications:
    if notifications == 1:
        print("unread notification")
    break
else:
    print("all caught up")


#while --> it relies on condition ,it will be completely executed until the
#condition is satisfied

syntax while:
    
while <condition>:
    statements(s)......
    ..........
    .........

while True:
    print("yes")# it prints multiple times we need to press Ctrl+C (lryboard interrupt)

i=0
while i <=10:
    i=i+1
    print(i)
  
i=10
while i >= 1:
    print(i)
    i=i-1  #decrement
'''

#banking scenario -->? pin authentication if more than 3 attempts
#account locked.....

pin="2612"
max_attempts=3
current_attempt=0
while current_attempt < max_attempts:
    entered_pin = input("enter the ATM pin:")
    if entered_pin == pin:
        print("Login successfull")
        break
    else:
        print("enter pin is wrong..Try  again carefully")
        current_attempt+=1
else:
    print("Account Locked,try after 24 hours...")
    



































    


    

    



















































