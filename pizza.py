import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
tray = 0
flashlight = 0

required = ("\nYou can only choose option A, 86yhgB, or C\n")
required2 = ("\nYou can only choose option A or B\n")

print("""It's time to make your own pizza!\n\n""")

def intro():
    choice = input("Would you like to start?\n >>> ")
    time.sleep(1) #this just means you are including a pause
    print("\n")
    if choice in yes: #see arrays above
        print("Then let's get started!\n")
    elif choice in no:
        print ("\nYou should probably leave then. Bye!")

        raise SystemExit #This will exit the program and bring you back to command line

def base():
  print ("""Here are the options for the base of the pizza. You would like to have:""")
  time.sleep(1)
  choice2 = input("""
    A. Thin Crust
    B. Deep dish
    C. Nothing\n
    >>> """)
  print("\n")
  if choice2 in answer_A:
        print("The dough is being spread out.")
  elif choice2 in answer_B:
        print("The dough is being spread out.\n")
  elif choice2 in answer_C:
        print ("\nUm I don't think you're making a pizza so you can just stop here. Bye!\n")
        raise SystemExit
  else:
        print(required)
        time.sleep(0.5)
        base()

def sauce():
    print("""  \nNext, what kind of tomato sauce would you like to work with? """)
    time.sleep(1)
    choice3 = input("""
    A. Canned tomato sauce
    B. Fresh tomato sauce
    C. Other\n
    >>> """)
    print("\n")
    if choice3 in answer_A:
          print("There is now an even layer of canned tomato sauce on the dough.\n")
          time.sleep(0.5)
    elif choice3 in answer_B:
          print("""There is an even layer of fresh tomato sauce on the dough.\n""")
    elif choice3 in answer_C:
          print("I'm sorry are you even making a pizza anymore????\n")
          time.sleep(1)
          raise SystemExit
    else:
          print(required)
          time.sleep(1)
          sauce()

def cheese():
    print("What kind of mozzarella cheese would you like\n")
    time.sleep(0.75)
    choice4 = input("""
    A. Shredded
    B. Fresh
    >>> """)
    print("\n")
    if choice4 in answer_A:
        print("No judgement but fresh mozzarella is the best:)\n")
    elif choice4 in answer_B:
        print("Smart move, that's the best kind!\n")
    else:
          print(required2)
          cheese()

def oven():
    print("""Now that you're done making the pizza, let's go to the oven!\n""")
    time.sleep(0.75)
    print("""You open the oven door and slide the pizza onto a baking stone so that the base can get to the temperature that it needs to.\n""")
    time.sleep(0.75)
    print("""Plus it also adds a great charred surface for additional texture and taste!\n""")
    time.sleep(0.75)
    print("""You take the pizza out and chop up some fresh basil to add on top for the finished margarita pizza.\n""")
    time.sleep(0.75)
    print("""You're done! You're basically a chef now!\n""")
    raise SystemExit

#This is where you call all the functions so they run
intro()
base()
sauce()
cheese()
oven()