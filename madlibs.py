import random

level = input("There are three levels as follows Easy, Medium, Hard \
    Choose:").lower()

if level == "easy":
    print("Easy level")
    
    i = random.randint(1, 5)

    if i==1:
        verb = input("Verb:")
        print(f"Madlib \
            I like my Donuts with extra '{verb}' on them.")    
    elif i==2:
        noun = input("Noun:")
        print(f"Madlib \
            Be careful not to vaccum the '{noun}' when you clean under your bed.")
    elif i==3:
        noun = input("Noun:")
        print(f"Madlib \
            Love is what makes the '{noun}' go round.")
    elif i==4:
        adjective = input("Adjective:")
        print(f"Madlib \
            Once that '{adjective}' music comes on, it's time to shut down your acceptance speech.")
    elif i==5:
        verb = input("Verb ending with 'ing':")
        print(f"Madlib \
            My daily exercise '{verb}' after my school bus in the morning.")

elif level == "medium":
    print("Medium")

elif level == "hard":
    print("hard")

else:
    print("Command not recognized")
    
