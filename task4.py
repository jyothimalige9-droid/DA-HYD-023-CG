'''write a python program to calculate the innings of a batsman and boundaries ,total score,dotballs

runs = [4, 6, 1, 0, 2, 4, 0, 6]

total_score = 0
boundaries = 0
dot_balls = 0

for i in runs:
    total_score = total_score + i

    if i == 4 or i == 6:
        boundaries = boundaries + 1

    if i == 0:
        dot_balls = dot_balls + 1

print("Total Score =", total_score)
print("Total Boundaries =", boundaries)
print("Dot Balls =", dot_balls)

#write program using while loop to unlock the pattern atleast 5 attemps  

current_pin = "5432"
max_attempts = 5
current_attempt = 0

while current_attempt < max_attempts:
    pin = input("Enter the pin: ")

    if pin == current_pin:
        print("Your entered PIN is correct")
        print("Phone unlocked")
        break
    else:
        current_attempt = current_attempt + 1
        print("Wrong PIN, try again")

if current_attempt == max_attempts:
    print("Your phone has been locked)


atm_pin = "1111"
max_attempts = 3
current_attempt = 0

while current_attempt < max_attempts:
    pin = input("Enter the pin: ")

    if pin == atm_pin:
        print("Your entered PIN is correct")
        print("Phone unlocked")
        break
    else:
        current_attempt = current_attempt + 1
        print("Wrong PIN, try again")

if current_attempt == max_attempts:
    print("Your phone has been locked")

'''


movies = ["Salaar", "Bahubali", "KGF"]

for i in range(len(movies)):
    print(i + 1, ".", movies[i])









          
