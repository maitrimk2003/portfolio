


import math
#starting page with background, USER "click to start" # we have to adjust the time after the users choose
#display checklist: hw, laundry, dishes, mirrors, mop/sweep, shower, organize room, set the table
#print("click to start")
# once button is pressed page is removed and game starts # the day start 8:32am
#objective is to finish chores before the family returns,however their are distractions that could interfer
name = input("What is your name?:")
print("Hello," + name)
print("Let's see how productive you are?")
# 1.distractions the user is in BED and thinks should I leave bed, check cellphone, or go back to sleep
print("The objective of the game is is to finish your chores at about 2:30 before your parents come back home. Manage your time wisely.")
print("Good Morning " + name)
print("It's 8:32 am")
print("Type in the number that corressponds to your answer:")
print("You wake up and choose to ... 1. Go and brush your teeth and then start your chores or 2. Check your cellphone or 3. Go back and sleep")
morning = eval(input("What will you do?"))
if (morning == 1):
	print("Great choice.")

#the character would move to the living room
elif (morning == 2):
  	print("You're newsfeed looked pretty lit")
    #"U LOST 45 MINUTES")
    #the character would stay in the room then move to the living room
elif (morning == 3):
  	print("Getting your beauty sleep is key.")

else:
  	print("Type in the number that corressponds to your answer:")
print("You choose how your gonna start your morning but then you were interrupted by a call from your Uncle Bob.")
print("He says ... Good morning, what are you doing today?")
uncle = eval(input("Do you say... 1. hello and tell him your busy or 2. talk to him and ask him how the family is"))
if (uncle == 1);
	print("")
print("Time for breakfast")
print("You should have ... 1. some fruit or 2.make some toast and boil some eggs?")
breakfast = eval(input("What will you have?:"))
if (breakfast == 1):
    print("Ok your not a breakfast person ,that's cool...")
    #you lost 5 minutes
if (breakfast == 2):
    print("You know what they say, breakfast is the most important meal of the day")
    #u lost 10 min
print("After that yummy breakfast, someone needs to wash the dishes.")
print("Will you... 1. Do them now or 2. Save them for later")
dishes = eval(input("What will you do?:"))
if (dishes == 1):
    print("Good, you got them out of the way. The kitchen looks good.")
elif (dishes == 2):
    print("Interesting choice...")
else:
    print("Type in the number that corressponds to your answer:")
print("Now lets finish up and clean these mirrors. You can barely see yourself in them!")
print(" Would you ... 1.clean the windows quickly or 2. daydream out the window longing to go outside")
mirrors = eval(input("What will you do?:"))
if (mirrors == 1):
    print("Wow, we should clean these more often.")
elif (mirrors == 2):
    print("Oh, it's so nice out today maybe hurry up and finish these chores.")
else:
    print("Type in the number that corressponds to your answer:")
print("You need to set the table for the feast that you and your family are gonna have for lunch")
print("Will you ... 1.set the table  using your inner desire to be an interior designer  or 2. set the table to the bare minimum standard")
table = eval(input("What will you do?:"))
if (table == 1):
    print("Your dining tabke looks as if it can be on HGTV!!!!")
elif (table == 2):
    print("Lunch, caveman style")
else:
    print("Type in the number that corressponds to your answer:")
print(" As your setting the table, the doorbell rings.\n")
print("Uncle Bob and Aunt Sylvia are at the door. Do you ... 1. invite them in, putting your chores on the back burner or 2. slam the door on them and continue your chores, risking being the talk of the next family reunion.\n")
guest = eval(input("What will you do?:"))
if (guest == 1):
      print("Such a great host")
elif (guest == 2):
      print("Watch out for chatty aunt Sylvia this Christmas")
