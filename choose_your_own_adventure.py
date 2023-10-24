name = input("Type your name: ")
print("Welcome", name, "to the adventure!")

answer = input("You are on a dirt road. It has come to an end, and you can go left or right: ").lower()

if answer == "left":
    answer = input("You come to a river. Would you like to walk around it or swime across. (swim/walk): ").lower()

    if answer == "swim":
        print("You tried to swim and drowned!")
    elif answer == "walk":
        answer = input("You walk for miles and eventually come to a log. Do you want to cross on the log? (cross/go back): ")
        
        if answer == "cross":
            print("You slipped off the log and drowned in the river.")
        elif answer == "go back":
            print("You ran out of food and starved to death.")
    else:
        print("Not a valid selection. You lose.")

elif answer == "right":
    answer = input("You find an old decaying bridge. Would you like to cross? (cross/go back): ")

    if answer == "cross":
        answer = input("The bridge is wobbly, but you make it across. You meet a stranger in traveller's clothes, would you like to talk to him? (yes/no): ")

        if answer == "yes":
            print("He warns you that there are robbers ahead and then robs and kills you.")
        else:
            print("You ignore the stranger and he shoots you in the back.")
    
    elif answer == "go back":
        print("You ran out of food and starved to death.")

else:
    print("Not a valid selection. You lose.")