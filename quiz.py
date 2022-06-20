print("Hello There, Welcome!")

play = input("Would you like to play a game? (yes or no) ")

if play.lower() != "yes" :
    quit()

print("Excellent, Lets Begin...")

question = input("In Star Wars, Which Character Debuted With A Red Double-bladed Lightsaber? ")
if question.lower() == "darth maul":
    print("Correct! :)")
else: 
    print("Sorry that's Incorrect! :( ")


question = input("In 'The Witcher', Geralt has a steel sword and a ____ sword? ")
if question.lower() == "silver":
    print("Correct! :)")
else: 
    print("Sorry that's Incorrect! :( ")


question = input("What symbol is House Tyrell in 'Game of Thrones'? ")
if question.lower() == "rose":
    print("Correct! :)")
else: 
    print("Sorry that's Incorrect! :( ")


question = input("What year does Marty McFly get sent too in 'Back to the Future'(1985)?  ")
if question.lower() == "1955":
    print("Correct! :)")
else: 
    print("Sorry that's Incorrect! :( ")


question = input("In the series 'My Hero Academia', which character has the quirk of fire and ice?  ")
if question.lower() == "todoroki":
    print("Correct! :)")
else: 
    print("Sorry that's Incorrect! :( ")

