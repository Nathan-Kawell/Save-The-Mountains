import time
import random

#these can be changed to "0" to easily test game
short_pause = 1
long_pause = 2

#pause any text for a given time
def text_pause(message, pause):
    print(message)
    time.sleep(pause)

#introduction at start of game
def intro():
    text_pause("As the clouds roll away, you awake to find yourself in the mountains.", long_pause)
    text_pause("You look around and notice two prominate places on the horizon.", long_pause)
    text_pause("The first place you see is a fortress on top of the highest mountain.", long_pause)
    text_pause("The second place is an apparently abandoned mineshaft.", long_pause)

#give player choice to fight villain or run away
def fight_or_flee(villain):
    text_pause(f'{villain} stands up and says, "You will be crushed!"', long_pause)
    fight_or_flight = get_valid_input("Will you fight? Or flee?\n", ["fight", "flee"])
    return fight_or_flight

#after defeat or victory asks player to play again
def play_again(): 
    play_choice = get_valid_input("Would you like to play again? y/n\n", ["y", "n"])
    if play_choice == "y":
        play_game()
    elif play_choice == "n":
        print("Thanks for playing!")

#asks any given question and has player choose from the given options
def get_valid_input(question, options):
    response = input(question).lower()
    while response not in options:
        text_pause("Invalid input", short_pause)
        response = input(question)
    return response

#the place where the player encounters the villain and is the only place the player can win or lose
def fortress(items, villain, weapon):
    text_pause("You enter the dark fortress.", long_pause)
    text_pause(f"And you see {villain} himself.", long_pause)
    if weapon in items:
        text_pause(f"Drawing your {weapon}, you strut up to him, blasting him repeatedly.", long_pause)
        text_pause(f"As his feeble mind tries to grasp the improbability of a {weapon} in this century, "
                "he collapases without a sound.", long_pause)
        text_pause("Victory! At the loss of the time-space contunium...", long_pause)
        play_again()
    elif "Sword" in items and "Shield" in items:
        fight_choice = fight_or_flee(villain)
        if "fight" in fight_choice:
            text_pause(f"{villain} slowly approaches you.", long_pause)
            text_pause("He suddenly lunges forward!", short_pause)
            text_pause("You block with your shield!", short_pause)
            text_pause("You slash back with your sword, catching him in the neck!", short_pause)
            text_pause(f"Choking on his own blood, {villain} falls.", long_pause)
            text_pause("Victory! You have saved the mountains!", long_pause)
            play_again()
        elif "flee" in fight_choice:
            text_pause("You quickly run back to the saftey of the mountains.", long_pause)
            choices(items, villain, weapon)
    elif "Sword" in items:
        fight_choice = fight_or_flee(villain)
        if "fight" in fight_choice:
            text_pause(f"{villain} slowly approaches you.", long_pause)
            text_pause("He suddenly lunges forward!", short_pause)
            text_pause("You try to parry with your sword but are too slow!", short_pause)
            text_pause("You feel his weapon sink through your ribs and shred your heart.", short_pause)
            text_pause("You drop to the ground as your blood leaves your body.", long_pause)
            text_pause(f"Defeat! {villain}'s reign continues!", long_pause)
            play_again()
        elif "flee" in fight_choice:
            text_pause("You quickly run back to the safety of the mountains.", long_pause)
            choices(items, villain, weapon)
    elif "Shield" in items:
        fight_choice = fight_or_flee(villain)
        if "fight" in fight_choice:
            text_pause(f"{villain} slowly approaches you.", long_pause)
            text_pause("He suddenly lunges forward!", short_pause)
            text_pause("You block with your shield!", short_pause)
            text_pause("You try to fight back, but with nothing in your hand you can only defend.", short_pause)
            text_pause(f"{villain} bellows with laughter as he notices your lack of weapon.", long_pause)
            fight_again = input("Will you fight? Or flee?\n").lower()
            if "fight" in fight_again:
                text_pause("You continue to block his attacks, but grow weary over time.", short_pause)
                text_pause("Eventually he overwhelms you and you fall tasting the steel of his weapon.", long_pause)
                text_pause(f"Defeat! {villain}'s reign continues!", long_pause)
                play_again()
            elif "flee" in fight_choice:
                text_pause("You quickly run back to the safety of the mountains.", long_pause)
                choices(items, villain, weapon)
        elif "flee" in fight_choice:
            text_pause("You quickly run back to the safety of the mountains.", long_pause)
            choices(items, villain, weapon)
    else:
        text_pause("As you take in your surroundings, you notice your empty hands "
                    "and realize you might be horribly out of your depth.", long_pause)
        fight_choice = fight_or_flee(villain)
        if "fight" in fight_choice:
            text_pause(f"{villain} slowly approaches you.", long_pause)
            text_pause("He suddenly lunges forward!", short_pause)
            text_pause("You quikcly dodge roll to your right.", short_pause)
            text_pause("He follows with a sweeping blow from his weapon.", short_pause)
            text_pause("You wildly throw your hands up in a feeble attempt to block.", short_pause)
            text_pause("Your bones crack and limbs shred as his "
                    "weapon makes contact with your bare arms.", short_pause)
            text_pause("Mercilessly he wails away on your dying body.", short_pause)
            text_pause(f"Defeat! {villain}'s reign continues!", long_pause)
            play_again()
        elif "flee" in fight_choice:
            text_pause("You quickly return to the safety of the mountians.", long_pause)
            choices(items, villain, weapon)




#the place where the player can collect items
def mineshaft(items, villain, weapon):
    if "Sword" in items or "Shield" in items or weapon in items: #checks to see if player has done anything in the mineshaft yet
        text_pause("You re-enter the mineshaft intersection.", long_pause)
        if "Sword" in items and "Shield" in items and weapon in items: #checks to see what items player has. Tunnels are different depending on what the player has
            text_pause("On your right is a dark tunnel with a faint light at the end.", long_pause)
            text_pause("On your left is a foggy tunnel.", long_pause)
            text_pause("Straight ahead is pitch black.", long_pause)
        elif "Sword" in items and "Shield" in items:
            text_pause("On your right is a dark tunnel with a faint light at the end.", long_pause)
            text_pause("On your left is a foggy tunnel with things moving in the fog.", long_pause)
            text_pause("Straight ahead is pitch black.", long_pause)
        elif "Sword" in items and weapon in items:
            text_pause("On your right is a dark tunnel with a faint light at the end.", long_pause)
            text_pause("On your left is a foggy tunnel.", long_pause)
            text_pause("Straight ahead is pitch black with faint scuffling sounds.", long_pause)
        elif "Shield" in items and weapon in items:
            text_pause("On your right is a dark tunnel with a glimmering light at the end.", long_pause)
            text_pause("On your left is a foggy tunnel.", long_pause)
            text_pause("Straight ahead is pitch black.", long_pause)
        elif "Sword" in items:
            text_pause("On your right is a dark tunnel with a faint light at the end.", long_pause)
            text_pause("On your left is a foggy tunnel with things moving in the fog.", long_pause)
            text_pause("Straight ahead is pitch black with faint scuffling sounds.", long_pause)
        elif "Shield" in items:
            text_pause("On your right is a dark tunnel with a glimmering light at the end.", long_pause)
            text_pause("On your left is a foggy tunnel with things moving in the fog.", long_pause)
            text_pause("Straight ahead is pitch black.", long_pause)
        elif weapon in items:
            text_pause("On your right is a dark tunnel with a glimmering light at the end.", long_pause)
            text_pause("On your left is a foggy tunnel.", long_pause)
            text_pause("Straight ahead is pitch black with faint scuffling sounds.", long_pause)
    else:
        text_pause("As you crawl through the crumbling entrance, "
                "you enter a mineshaft with three directions", long_pause)
        text_pause("On your right is a dark tunnel with a glimmering light at the end.", long_pause)
        text_pause("On your left is a foggy tunnel with things moving in the fog.", long_pause)
        text_pause("Straight ahead is pitch black with faint scuffling sounds.", long_pause)
    text_pause("Which way will you go?", long_pause)
    direction = get_valid_input("Straight, right, left, or back?\n", ["straight", "right", "left", "back"])
    if "straight" in direction:
        if "Shield" in items:
            text_pause("You search the area where you found the shield, but to no avail.", long_pause)
            text_pause("You quickly exit the tunnel.", long_pause)
            mineshaft(items, villain, weapon)
        else:
            text_pause("Your senses slowly adjust to the utter darkness.", long_pause)
            text_pause("You hear pitter-pattering on metal, and move towards the sound.", long_pause)
            text_pause("As you approach you can feel rats scurring away "
                        "when your hand brushes a metal disk.", long_pause)
            text_pause("You collected the Ancient Shield!", long_pause)
            items.append("Shield")
            text_pause("You exit the dark tunnel.", long_pause)
            mineshaft(items, villain, weapon)
    elif "right" in direction:
        if "Sword" in items:
            text_pause("You look around the beam of light, but find nothing.", long_pause)
            text_pause("It seems the Ancient Sword was the only thing over here.", long_pause)
            text_pause("You leave the glowing tunnel.", long_pause)
            mineshaft(items, villain, weapon)
        else:
            text_pause("You head towards the light at the tunnels end.", long_pause)
            text_pause("As you approach you see there is light coming from a hole in the roof.", long_pause)
            text_pause("It is reflecting off something shiny....and sharp!", long_pause)
            text_pause("You collected Ancient Sword!", long_pause)
            items.append("Sword")
            text_pause("You leave the way you came.", long_pause)
            mineshaft(items, villain, weapon)
    elif "left" in direction:
        if weapon in items:
            text_pause(f"You rummage around the skeleton where you found the {weapon} "
                        "but come up empty.", long_pause)
            text_pause("You leave the foggy tunnel.", long_pause)
            mineshaft(items, villain, weapon)
        else:
            text_pause("You hesitantly make your way through the fog.", long_pause)
            text_pause("Pushing through the fog, "
                        "you realize what's moving is small electrical charges.", long_pause)
            text_pause('You see shattered pieces of blue wood, '
                        'some with a strange word on them, "Police".', long_pause)
            text_pause("Among the blue pieces of wood, you see a skeleton with strange clothes.", long_pause)
            text_pause("Grasped in it's hands is a strange weapon.", long_pause)
            text_pause(f"You recieved {weapon}!", long_pause)
            items.append(weapon)
            text_pause("Confused, you leave the foggy tunnel, noticing the charges are gone.", long_pause) 
            mineshaft(items, villain, weapon)
    elif "back" in direction:
        text_pause("You head back to the mountains the way you came.", long_pause)
        choices(items, villain, weapon)

#area where player chooses where to go
def choices(items, villain, weapon):
    text_pause("Enter 1 to approach the fortress.", long_pause)
    text_pause("Enter 2 to go into the mineshaft.", long_pause)
    text_pause("What would you like to do?", long_pause)
    choice = get_valid_input("(Please enter 1 or 2)\n", ["1", "2"])
    if choice == "1":
        fortress(items, villain, weapon)
    elif choice == "2":
        mineshaft(items, villain, weapon)



#main function. Plays game and resets randoms every time it's played
def play_game():
    items = []
    villain = random.choice(["The Dark Lord", "The Evil Warlord", "The Tyranical King"])
    weapon = random.choice(["Deagal", "Ray Gun", "AK-47"])
    intro()
    choices(items, villain, weapon)


play_game()

