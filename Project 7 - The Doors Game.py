


#Defining the doors, and what means open and closed
doors = []
win = []
lose = []
open = 1
closed = 0

initial = input("There are 100 doors.\nDo you want the doors open or closed: ")
initial = initial.lower()
if initial == "open":
  for i in range(1,100):
    doors.append(open)
if initial == "closed" :
  for i in range(1,100):
    doors.append(closed)

requirement = input("If you open every nth door in a turn, do you think\nyou can finish will all the doors open or closed: ")
requirement = requirement.lower()
if requirement == "open":
  for i in range(1,100):
    win.append(open)
    lose.append(closed)
if requirement == "closed" :
  for i in range(1,100):
    win.append(closed)
    lose.append(open)

def toggle(n):
  for i in range(1,100):
    if i % n == 0:
      if doors[i-1] == open:
        doors[i-1] = closed
      else:
        doors[i-1] = open

turns = 1
list = []
for i in range(1,100):
  list.append(i)



while True:
  for n in list:
    turns +=1
    toggle(n) 
  if doors == win:
    print("You win!")
    print(f"It only took you {turns} attempts to win!")
    print("Thanks for playing!")
    break
  elif doors == lose:
    print("You lose!")
    print(f"It only took you {turns} attempts to lose!")
    print("Thanks for playing!")
    break 