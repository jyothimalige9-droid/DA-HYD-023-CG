'''#control statments -->control the flow of execution of the program
conditional statements --> if,elif,else......
Repetition statements(Loops)-->for,while,(for with else),(while with else)....
Jumping statements --> break,continue,pass....

loop --> repetative process(loops are help for repetative)
#for keyword is help to iterate over a sequence / range
#syntax:

for <temp_var> in sequence / range:
    statment(s).....
    .......
#by default range picks 0 as start value
for i in range(10):
    print(i)

if i > 5 and i % 2 == 0:
    print(i)

#range
for i in range(1,10,2):
    print(i)
    print("Done")
    
for i in range(-10,0,1):
    print(i)
#[] --> we generally lists

names=['saketh','sairam','akash']
for i in range(len(names)):
    print(names[i])

#calculate the sum of first 10 numbers
#first understand your input --> range(11)-->10 numbers
result=0
for i in range(11):
    result=result+i
    print("result=",result)

sum=0
for i in range(1,21,1):
    sum=sum+i
    print("sum=",sum)

#understand the loops usage with fitness streak example
'''
work_log=[0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak=0
current_streak=0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak=current_streak+1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)





























