print("🎉 Welcome to the Premier League Quiz Extravaganza! 🎉")
print("🏟 Get ready to dive into the electrifying world of English football! ⚽")

player = input("👀 Are you ready to test your Premier League knowledge? (Yes/No) ")

if player.lower() != "yes":
    print("😔 Aww, no worries! Come back when you're ready for the challenge!")
    quit()
else:
    print("🔥 Let the games begin! Get ready for an adrenaline-fueled quiz adventure! 💪")

score = 0

answer = input("🏆 Which team has clinched the most Premier League titles? ")
if answer.lower() == "manchester united":
    print("🎉 Correct! Manchester United reigns supreme with their numerous triumphs (13)!")
    score += 1
else: 
    print("❌ Oh no! It's actually Manchester United, the kings of the Premier League!")

answer = input("⚽ Who holds the prestigious title of the Premier League's all-time leading goalscorer? ")
if answer.lower() == "alan shearer":
    print("👑 Correct! Alan Shearer's scoring prowess is unmatched in Premier League history (260 goals)!")
    score += 1
else: 
    print("🚫 Not quite! It's Alan Shearer, the goal-scoring legend of the Premier League!")

answer = input("🧤 Who stands tall as the record holder for the most clean sheets in a single Premier League season? ")
if answer.lower() == "petr cech":
    print("🌟 Absolutely right! Petr Cech's goalkeeping brilliance shines bright in the record books (24 cleansheets)!")
    score += 1
else: 
    print("🤔 Nope! It's Petr Cech, the guardian of the net with an astonishing 24 clean sheets!")

answer = input("🏟️ Which stadium boasts the largest seating capacity in the Premier League? ")
if answer.lower() == "old trafford":
    print("🎊 Spot on! Old Trafford stands tall as the iconic fortress of Manchester United (74,310)!")
    score += 1
else: 
    print("🙈 Not quite! It's Old Trafford, the legendary home ground of Manchester United!")

print(f"🎉 Congratulations! You scored {score} out of 4 questions correct!")
percentage = (score / 4) * 100
print(f"🌟 Your Premier League expertise shines with an impressive {percentage}% success rate!")
print("👏 Thanks for playing! Until next time, keep the Premier League spirit alive! ⚽🔥")
