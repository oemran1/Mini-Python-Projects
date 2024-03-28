print("Welcome to my Premier League quiz!")

player = input("Do you want to play? ")

if player.lower() != "yes":
    print("Aww, maybe next time :(")
    quit()
else:
    print("Okay! Let's play :)")
score = 0

answer = input("Which team has won the most Premier Leagues titles? ")
if answer.lower() == "manchester united":
    print("Correct!")
    score +=1
else: 
    print("Incorrect! It was Manchester United.")

answer = input("Who is the all-time leading goalscorer in the Premier League? ")
if answer.lower() == "alan shearer":
    print("Correct!")
    score +=1
else: 
    print("Incorrect! It was Alan Shearer.")

answer = input("Who holds the record for the most clean sheets kept by a goalkeeper in a single Premier League season? ")
if answer.lower() == "petr cech":
    print("Correct!")
    score +1
else: 
    print("Incorrect! It was Petr Cech (24).")

answer = input("Which stadium has the largest seating capacity in the Premier League? ")
if answer.lower() == "old trafford":
    print("Correct!")
    score +=1
else: 
    print("Incorrect! It was Old Trafford (Manchester United's stadium).")

print(("You got ") + str(score) + (" out of 4 questions correct!"))
print(("You got ") + str((score/4) * 100) + ("%."))
