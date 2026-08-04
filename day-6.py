'''
control statements --> control flow of execution of the program
                -->conditional statements-->if,elif,else
                -->repetition statements(loops)-->for,while(for with else)
                                                            (while with else)
                -->jumping statements-->break,countinue,pass
'''
#loops-->loops are helpful for repetition(automative tasks)
#for keyword will be heplful to iterate over a sequence/range
#sytax for(for keyword):
'''
for <temp_var> in sequence/range:
        statements
'''
#range(stop)-->default 0 ends at stop -1
#range(start,stop,step)
#by default range picks 0 as start value
'''
#stop
for i in range(10):
    print(i)


#in above case got 10 iterations
#start and stop
for i in range(1,10):
    #if i>5:
        #print(f'value of i is -->{i}')
    #now i want to get only even numbers with above condition
    if i>5 and i%2==0:
        print(i)

#step
for i in range(1,10,4):
    print(i)

for i in range(-10,0,1):
    print(i)

#[]-->we genrally lists
names=['sai','ram','ganesh']
#print(len(names)) #len(obj)-->returns the number of items in a container
for i in names:
    #print(i)
    if i=='sai':
        print('This is student name')


#caluclated the sum of first 10 numbers
#first understand your input -->range(11)--10 numbers
#secoud understand your output -->sum(number)
#third we need to map the logic

result=0
for i in range(11):
    result=result+i#result +=i
    print(result)


result=0
for i in range(21):
    if i%2==0:
        result=result+i
        print(result)

'''
#understand the loops usage with fitness streak example
#work_out -->1,work_out_missed==>0
work_log=[0,1,1,1,0,1,0]
#result variable-->longest_streak
longest_streak=0
current_streak=0
for i in work_log:
    if i==1:
        print(i)
        current_streak=current_streak+1
        if current_streak>longest_streak:
            longest_streak=current_streak
    else:
        current_streak=0 #streat break
print(longest_streak)
