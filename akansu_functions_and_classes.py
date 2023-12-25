'''

Programmer: Eric, Yathusan, and Omar

Date of Creation: May 27, 2022

Description: Module of functions and classes for Ragnarok Akansu Village Arc

'''

import random
from pygame import mixer
from time import sleep
from sys import stdout
from PIL import Image
import akansu_fall

# Constantly used functions
def dead_end():
    '''Kills character and exits code'''

    sleep(3)

    print()

    mixer.init()
    death_sound = mixer.Sound("SFX/Other Sounds/You Died.wav")
    death_sound.play()
    slowprint("~You have perished.~", 0.1)

    sleep(3)

    exit()

def dice(dice_type):
    '''Rolls a certain dice'''

    if dice_type == "d2":
        return(random.randint(1, 2))

    elif dice_type == "d6":
        return(random.randint(1, 6))

    elif dice_type == "d12":
        return(random.randint(1, 12))

    elif dice_type == "d20":
        return(random.randint(1, 20))

    else:
        return None

def slowprint(message, delay):
    '''Slowly prints strings'''
    for i in message + '\n':
        stdout.write(i)
        stdout.flush()
        sleep(delay)

# Events that happen before the game
def pre_game():
    '''Pre-game notes'''

    print()
    print("Notes:")
    print("------")
    print("This is 99% copyrighted and a rip-off of everything we've watched.")
    sleep(2)

    print()

    slowprint("You're still here? Press enter to start.", 0.05)
    input()

    print("\n" * 100)

def title_screen():
    '''Fancy storytelling'''

    slowprint("~Once upon a time in the realm of Ragnarok...~", 0.08)
    sleep(1)

    print("\n" * 100)

def name_easter_egg(first_name, last_name):
    '''Name easter egg'''

    if first_name == "Hiroshima" and last_name == "Nagasaki":
        slowprint("~Hiroshima Nagasaki... I've heard of that name before.\n"
        "Things are gonna get explosive!~", 0.2)

    else:
        slowprint("~A fresh face...~", 0.1)
    sleep(1)

    print("\n" * 100)

# Transfer to the world of Ragnarok
def isekai(last_name):
    '''Transition to Ragnarok'''

    print('Are you ready to begin? Enter "Yes" or "No":')
    begin = input()

    if (begin == "Yes"):
        print("Open the minigame and beat it to continue! If you fail, you die!")
        win = akansu_fall.actual_game()

    if (begin == "Yes" and win):
        print("\n" * 100)
        mixer.init()
        mixer.music.load("SFX/Music/Arriving In Ragnarok.wav")
        mixer.music.play()

        sleep(2.2)

        print()
        print("~In times of trouble, an age of demise.~")
        sleep(1)
        print("~Calls for a hero, the legend will rise.~")
        sleep(3)

        print()
        print("~The arid deserts, or many trees!~")
        sleep(1)
        print("~The frozen tundras and open seas!~")
        sleep(3)

        print()
        print("~A realm of classes, the rich and the poor.~")
        sleep(1)
        print("~None of that matters, in cruel times of war.~")
        sleep(3)

        print()
        print("~Many opportunities, there's too much to try.~")
        sleep(1)
        print("~In the realm of Ragnarok, even death may die.~")
        sleep(3)

        print()
        print("~Kingdoms alike dignity, of dark and light.~")
        sleep(1)
        print("~No hopes for peace, an endless fight.~")
        sleep(3)

        print()
        print("~Where the truth can be found, more secrets lie.~")
        sleep(1)
        print("~For now a naked", last_name + ", falls from the sky.~")
        sleep(3)

        mixer.music.pause()

        record_scratch = mixer.Sound("SFX/Other Sounds/Record Scratch.wav")
        record_scratch.play()
        sleep(2)

        print()
        print(last_name + ": Wait...")
        sleep(3)
        print(last_name + ":", 'WHAT\'D YOU MEAN BY \"falls from the sky"!? Gimme a brea-')
        sleep(3)

        mixer.music.unpause()

        falling_yell = mixer.Sound("SFX/Other Sounds/Falling Yell.wav")
        falling_yell.play()

        for i in ["AAAAH", "AAAAAAAAh", "AAAAAAAAAAAah",
        "AAAAAAAAAAAAAAaah", "AAAAAAAAAAAAAAAAAaaah"]:
            sleep(1)
            print(last_name + ':', i)

        falling_yell.stop()
        bone_crack = mixer.Sound("SFX/Other Sounds/Bone Crack.wav")
        bone_crack.play()
        sleep(0.8)
        print()
        print("*Crack!*")

        print()
        slowprint("~Eric, Yathusan, and Omar Present~", 0.2)
        print("--------------------------")
        slowprint("Ragnarok: Akansu Village Arc", 0.1)
        sleep(19)

    else:
        '''Ends the program'''

        mixer.init()
        mixer.music.load("SFX/Other Sounds/Bruh.wav")
        mixer.music.play()

        print("\n" * 100)
        sleep(1)
        print("~Okay.~")

        dead_end()

# Arrival decisions
def arrival(first_name):
    '''Upon arrival in the realm of Ragnarok'''

    print("\n" * 100)

    '''Character gets up'''
    slowprint("~Heh, looks like you beat the minigame.\n"
    "Had you hit the branches, you would've snapped your neck.~", 0.05)
    slowprint("~You fell on a deer and rolled in deep snow,\n"
    "which broke your 10000m fall.\n", 0.05)
    slowprint(first_name + ": Eurghh... screw you...\n"
    "It\'s so cold and- WOAH, free deer! *Nom*\n", 0.05)
    print("The deer was 100% consumed.\n")
    slowprint("~...~", 0.5)
    slowprint("~Okay... I'll just ignore that... anyways...~\n", 0.05)
    slowprint("~Over a large snow valley you spot a village that seems to radiate warmth.\n"
    "Looking behind you, there is a snowy pine forest leading into a sakura forest even\n"
    "further back. You\'d guess it was about -20 degrees and the time is duskfall. Anyways,\n"
    "you may go seeking shelter or adventure. The choice is ultimately yours.~\n", 0.025)

    '''Display Akansu Village choice'''
    view_akansu = input('Would you like to imagine the scenery? Type "Yes" or "No": ')

    print()

    if view_akansu == "Yes":
        akansu_village = Image.open("Scenery\Akansu Village.jpg")
        akansu_village.show()

        input("Press enter when you are ready to continue.\n")

    '''Visit village or explore forest decision'''
    print("Would you like to enter the village or head into the forest behind you?\n")
    print("1 = Enter the village")
    print("2 = Explore forest")

    print()

    arrival_decision = int(input("Choose: "))

    return arrival_decision

# Enter village route
def enter_akansu(first_name, age):

    print("\n" * 100)

    slowprint("~As you begin to explore, the village strikes you as profoundly beautiful.~", 0.04)

    if (age >= 21):
        slowprint("~You've spent your entire life slaving away at a dead-end 9 to 5 office job and seeing something so simple,\n"
        "magical, and free... brings tears to your eyes.~\n", 0.04)

    else:
        slowprint("~You've spent your entire life being bullied and was never loved. Seeing such a welcoming village... brings\n"
        "tears your eyes.~\n", 0.04)

    slowprint(first_name + ": If this is a dream... may I never wake up. I've decided to live here forever.\n", 0.04)

    slowprint("~Anyways, enough of the sentimental stuff.\n"
    "You see a tavern that emits warm light and friendly chatter.\n"
    "Although this seems very inviting, your hunger also makes you\n"
    "notice an old man, who is cooking a pot of stew. He notices you\n"
    "and invites you to come sit by the community kitchen.~\n", 0.04)

    print("1 = Enter tavern")
    print("2 = Sit by old man\n")

    village_decision = int(input("Choose: "))

    return village_decision

def enter_tavern(first_name, last_name):
    '''Upon entry into the Akansu village tavern'''

    print("\n" * 100)

    slowprint("~As you step into the tavern, shocked stares trail you wherever you go.", 0.04)
    slowprint("~Ahem... they are gawking at your nudity " + last_name + ".\n", 0.05)

    slowprint(first_name + ": Augh! Dont't look!!!", 0.03)
    slowprint("Bartender: Hey, you pervert! Stop flashing my customers and get over here this instant!!! There ain't\n"
    "nothing to look at anyways.", 0.04)
    slowprint(first_name + ": EXCUSE M-\n", 0.04)

    slowprint("~The bartender grabs you by the ear and drags you into the staff room.~", 0.04)
    slowprint("~After a lecture on proper etiquette, some food, and a pair of clothes, the Bartender\n"
    "begins to question you.\n", 0.04)

    slowprint("Bartender: You look different and clearly aren't from around. Where are you from?\n", 0.04)
    slowprint(first_name + ": I come fom Canada and I fell out of the sky...", 0.04)
    slowprint("Bartender: Huh? Never heard of this Canada place. Sounds like an ingredient for maple syrup.\n"
    "So, what's your name?", 0.04)
    slowprint(first_name + ": My name is " + first_name + ".", 0.04)
    slowprint("Bartender: Well it's nice to meet ya, " + first_name + "! Can you tell me how\n"
    "you REALLLY found this humble little village?", 0.04)
    slowprint(first_name + ": I already said I literally fell out of the sky!\n"
    "You already saw me butt-naked. Is there really anything I can hide from you\n"
    "at this point?", 0.04)
    slowprint("Bartender: If you say so kid. Anyways, I assume you don't know the\n"
    "current circumstances of this village then?", 0.04)
    slowprint(first_name + ": Englighten me, generous clothes-giver.\n", 0.04)

    slowprint("The bartender explains that the village has been attacked by hordes of\n"
    "gremlins for many years. Though Akansu defends against these monsters well,\n"
    "a new threat has recently emerged and plunged the village into dark times.\n"
    "There exists a friendly neighbouring village to Akansu named Appleville. Ever since the\n"
    "strange political issues among central-world kingdoms, the once friendly Appleville became\n"
    "hostile. War has been declared by opposing kingdoms and the villages that are colonies\n"
    "of their respective kingdoms now fight amongst eachother as proxies. Akansu's\n"
    "loyalty lies with the Reaponic crown, whereas Appleville's loyalty lies with the Angelic Crown.\n"
    "Hence, the times of peace are over.\n", 0.05)

    slowprint(first_name + ": I have no ties with this new world I have arrived into. However, I cannot allow\n"
    "the person who has clothed and sheltered me lose their only home. I shall assist Akansu in this war.", 0.04)
    slowprint("Bartender: That would be great! Any help will benefit us! Currently, we are lacking infantry and\n"
    "other supports. Which one are you interested in?\n", 0.04)

    print("1 = Join infantry")
    print("2 = Other supports\n")

    job_decision = int(input("Choose: "))

    if (job_decision == 1):

        print("\n" * 100)

        slowprint("Bartender: So you're a brave one, eh? Well, you should get some rest.\n"
        "There's a small bedroom in the back where you can stay the night.\n"
        "I'll introduce you to the commander tomorrow morning, for I myself am just\n"
        "a mere bartender.", 0.04)
        slowprint(first_name + ": For a mere bartender, you sure have alot of scars. I'm sure\n"
        "we all have our own stories. Good night, friend.", 0.04)
        slowprint("Bartender: An observative one, eh? G'night, kiddo.\n", 0.04)

        slowprint("~You fall asleep and you wake up the next morning.~",0.06)
        slowprint("~Following the bartender out of the tavern, you arrive at the army camp.~\n", 0.04)

        slowprint("Bartender: Rise and shine! The chief in command here is Alexander.", 0.04)
        slowprint("Alexander: Hey barkeep, sendin' me 'nother scrawny one?", 0.04)
        slowprint("Bartender: Don't mind ol' Alex here, he's gruff but has a heart of gold.", 0.04)
        slowprint(first_name + ": Uhh... nice to meet you Alexander.", 0.04)
        slowprint('Alexander: Shut yer trap scrawny shrimp!!! You\'ll address me as "chief" from now on\n'
        'and answer with either "yes sir" or "no sir", understand!?', 0.04)
        slowprint(first_name + ": What! how am I even scrawny? I go to GoodLife Fitness once a month.", 0.04)
        slowprint("Bartender: What's GoodLife Fitness?", 0.01)
        slowprint("Alexander: Drop down and give me 20, maggot!!!!!!", 0.03)
        slowprint(first_name + ": Yes sir!", 0.01)
        slowprint("Bartender: Heh, seems like you two are getting along well. Welp, see ya around kiddo,\n"
        "gotta go open up shop for the day.", 0.04)
        slowprint(first_name + ": Nooooo! Don't leave meeeeee!\n", 0.03)

        slowprint("~I pity you " + last_name + ".~", 0.05)

    elif (job_decision == 2):

        print("\n" * 100)

        slowprint("Bartender: Nice choice! Infrastructure needs improvements and so do the defences.\n"
        "There's a small bedroom in the back where you can sleep for the night.\n"
        "I'll introduce you to the material support organization tomorrow morning.\n", 0.04)

        slowprint("~You fall asleep until the next morning.~\n", 0.04)

        slowprint("Bartender: Rise and shine! Time for us to head out\n"
        "into the forest and meet your future co-workers.", 0.04)
        slowprint("Bartender: I present to you the material\n"
        "harvesting unit. The chief in command here is Lumber Jack, and\n"
        "all that he wants is that you give your best by quickly\n"
        "increasing production so that this war can be won with as\n"
        "minimal destruction and heartbreak as possible. Are you ready\n"
        "to take on this task for our beloved village?", 0.04)
        slowprint(first_name + ": Ready as I'll ever be!", 0.04)
        slowprint("Lumber Jack: I like your attitude! Let's get started!", 0.04)

    return job_decision

def old_man(first_name, last_name, age):
    '''Upon approaching an old man'''

    slowprint("~You approach the old man and take a seat beside him.~\n", 0.04)

    slowprint("Old Man: Why are you naked? I haven't seen you around town in all\n"
    "my years in this humble village.", 0.04)
    slowprint(first_name + ": I-", 0.02)
    slowprint("Old Man: Before you answer, eat. You look like a starving animal.", 0.06)

    if (age >= 21):
        slowprint(first_name + ": (Aside) Sigh... I wouldn't look like a starving animal\n"
        "if I could actually cover my food expenses. My stupid boss never pays me on time.", 0.04)

    slowprint(first_name + ": Thanks for the food! *Nom nom nom*", 0.04)
    slowprint("Old man: Hey take it easy buckaroo! Don't choke on the bones.\n"
    "Also here wear this, you must be freezing!\n", 0.04)

    slowprint("~The old man hands you a pair of warm clothes and you put it on as soon\n"
    "as you wolf down your stew.~\n", 0.04)

    slowprint(first_name + ": How can I ever repay you for you hospitality? You saved my life.", 0.04)
    slowprint("Old Man: How about you enlighten this old one. Where do you come from?\n", 0.04)

    print("1 = Tell the truth")
    print("2 = Lie to him\n")

    truth_lie = int(input("Choose: "))

    if (truth_lie == 1):
        print("\n" * 100)

        slowprint(first_name + ": To be honest, as crazy as this sounds, I fell\n"
        "from the sky and landed at the outskirts of this village.\n"
        "I'm a newcomer that knows nothing about this world.", 0.04)

    elif (truth_lie == 2):
        print("\n" * 100)

        slowprint(first_name + ": I've been living in the forest very close to here ever\n"
        "since I was a child, for my family left their village to become\n"
        "one with nature. No one besides you even knows about me.", 0.04)

    slowprint("Old Man: How curious... well don't worry, this old one knows\n"
    "a thing or two about keeping secrets. Let me inform you on\n"
    "the current state of affairs.\n", 0.04)

    slowprint("~The old man explains that the village has been attacked by hordes of\n"
    "gremlins for many years. Though Akansu defends against these monsters well,\n"
    "a new threat has recently emerged and plunged the village into dark times.\n"
    "There exists a friendly neighbouring village to Akansu named Appleville. Ever since the\n"
    "strange political issues among central-world kingdoms, the once friendly Appleville became\n"
    "hostile. War has been declared by opposing kingdoms and the villages that are colonies\n"
    "of their respective kingdoms now fight amongst eachother as proxies. Akansu's\n"
    "loyalty lies with the Reaponic crown, whereas Appleville's loyalty lies with the Angelic Crown.\n"
    "Hence, the times of peace are over.~\n", 0.05)

    slowprint(first_name + ": Oh my goodness... I didn't know things were this serious. I shall aid\n"
    "your village in order to return your generous hospitality! What can I do?", 0.04)

    slowprint("Old Man: You don't understand how thankful we are to hear that!\n"
    "We could really use a sturdy young man like you. Essentially, you\n"
    "have two choices to pick from. Your first option is to go out in\n"
    "the front lines and help win the war through direct fighting,\n"
    "which would definitely be the most beneficial for us. The second\n"
    "option is to help bring in wood from the forest to support defences.\n"
    "Now then young fella, which option would you prefer?\n", 0.03)

    print("1 = Join the front lines")
    print("2 = Join the lumber squad\n")

    job_decision = int(input("Choose: "))

    if (job_decision == 1):

        print("\n" * 100)

        slowprint("Old Man: You're a really brave one aren't ya? I can't thank you\n"
        "enough. Well then, how about you go rest in that tavern for the\n"
        "night, and in the morning, I'll introduce you to the commander.", 0.04)
        slowprint(first_name + ": Sounds good sir, good night!\n", 0.04)

        sleep(2)

        slowprint("~The sun rises upon the new day.~\n", 0.04)

        slowprint("Old Man: Welcome back sonny. Here, I present to you the war unit.\n"
        "The chief in command here is Alexander, and all that he wants\n"
        "is that you devote all of your strength in enabling\n"
        "us to win this war. Are you prepared\n"
        "to exhaust your blood and tears for this village?", 0.04)
        slowprint(first_name + ": Of course!", 0.04)
        slowprint("Alexander: Hey old man, sendin' me 'nother scrawny one?", 0.04)
        slowprint("Old Man: Don't mind ol' Alex here, he's gruff but has a heart of gold.", 0.04)
        slowprint(first_name + ": Uhh... nice to meet you Alexander.", 0.04)
        slowprint('Alexander: Shut yer trap scrawny shrimp!!! You\'ll address me as "chief" from now on\n'
        'and answer with either "yes sir" or "no sir", understand!?', 0.04)
        slowprint(first_name + ": What! how am I even scrawny? I go to GoodLife Fitness once a month.", 0.04)
        slowprint("Old Man: What's GoodLife Fitness?", 0.01)
        slowprint("Alexander: Drop down and give me 20, maggot!!!!!!", 0.03)
        slowprint(first_name + ": Yes sir!", 0.01)
        slowprint("Old Man: Heh, seems like you two are getting along well. Welp, see ya around kiddo,\n"
        "gotta go make more stew for the community kitchen.", 0.04)
        slowprint(first_name + ": Nooooo! Don't leave meeeeee!\n", 0.03)

        slowprint("~I pity you " + last_name + ".~", 0.05)

    elif (job_decision == 2):

        print("\n" * 100)

        slowprint("Old Man: This old bag of bones would have taken the same position as you,\n"
        "had it been 40 years younger. Well then, how about you go\n"
        "rest in that tavern for the night. In the morning, I'll present\n"
        "you to the lumber squad.", 0.04)
        slowprint(first_name + ": Sounds good old man, G'night!\n", 0.04)

        sleep(2)

        slowprint("~The chickens painfully tell your ears a new day has arrived.~\n", 0.04)

        slowprint("Old Man: Welcome back sonny! Here, I present to you the material\n"
        "harvesting unit. The chief in command here is Lumber Jack, and\n"
        "all that he wants is that you give your best by quickly\n"
        "increasing production so that this war can be won with as\n"
        "minimal destruction and heartbreak as possible. Are you ready\n"
        "to take on this task for our beloved village?", 0.04)
        slowprint(first_name + ": Ready as I'll ever be!", 0.04)
        slowprint("Lumber Jack: I like your attitude! Let's get started!", 0.04)

    return job_decision

# Enter forest route
def enter_forest(first_name, last_name):
    '''Upon entering the forest'''

    '''Forest entry story block'''
    slowprint("~You decide that it would be better to not mingle\n"
    "with those who you do not know. Better to take your chances\n"
    "out in the snowy forest... right?~", 0.03)
    slowprint("~As you pass the pine forest and pink blossoms surround you,\n"
    "the weather begins to take a turn for the worse. With a blizzard\n"
    "that conceals even your feet, visibility is now\n"
    "extremely poor. And if things are not bad enough, you are\n"
    "freezing. You do remember that you are naked right?~\n", 0.04)
    slowprint(first_name + ": Brrr...", 0.03)
    sleep(3)
    slowprint(first_name + ": Brrr... it\'s freezing!", 0.03)
    sleep(5)
    slowprint(first_name + ": Hmmmm, my arm actually feels quite warm now...\n", 0.03)
    sleep(2)
    slowprint("~" + last_name + "... you aren't feeling warm.~", 0.04)
    sleep(4)
    slowprint("~You are bleeding.~\n", 0.1)
    sleep(2)
    slowprint(first_name + ": GAHHH!!!\n", 0.01)
    slowprint("~You stare at your arm and notice a considerable chunk has been\n"
    "torn off. The blizzard begins to clear and it reveals a pack of bloodthirsty\n"
    "gremlins.~", 0.03)
    slowprint("~These Piranha-like creatures that dwell in the snowy sakura forest are\n"
    "notorious for eating their prey alive. You'd better think of something\n"
    "quick, lest they tear you limb from limb.\n", 0.05)

    '''Prompts to show user what a gremlin looks like'''
    view_gremlin = input("Would you like to see what these gremlins look like (Yes/No)?\n")

    if (view_gremlin == "Yes"):
        gremlin = Image.open("Scenery\Gremlin.jpg")
        gremlin.show()

        mixer.init()
        gremlin_laugh = mixer.Sound("SFX/Other Sounds/Gremlin Laugh.wav")
        gremlin_laugh.play()

        input("Press enter when you are ready to continue.\n")

    '''Gremlin attack decision'''
    print("Would you like to enter the village or head into the forest behind you?\n")
    print("1 = Run back to the village")
    print("2 = Fight Back\n")

    gremlin_decision = int(input("Choose: "))

    '''Run away from the gremlins and head toward village'''
    if (gremlin_decision == 1):
        print("\n" * 100)
        slowprint("~The gremlins give chase as you dash back to the village you\n"
        "saw earlier.~", 0.04)
        slowprint("~As you approach the village, you see a large group of people\n"
        "standing at the edge of the border with weapons and torches in hand.~\n", 0.04)

        print("Village Chief: Quick! Get behind us traveller!\n")
        print("Press enter to dash behind the crowd.")
        input()

        print("\n" * 100)
        slowprint("~You dash behind the crowd of defending villagers and what happens\n"
        "next could only be decribed as chaos.~\n", 0.04)
        slowprint("Villager: Damn you! Take this fiend!!! *Stabs a gremlin*\n", 0.03)

        slowprint("~The fighting clears, leaving a mountain of gremlin carcasses.\n"
        "Not a single villager died or was injured.~", 0.04)
        sleep(1.5)

        print("\n" * 100)
        slowprint("~The village elder nods at you and leaves.~", 0.05)

    '''Fight the gremlins'''
    if (gremlin_decision == 2):
        print("\n" * 100)
        slowprint('~There\'s a saying by Sun Tzu in his famous "Art of War"...~\n', 0.05)

        slowprint("Sun Tzu: When you surround an army, leave an outlet free.\n"
        "Do not press a desperate foe too hard.\n", 0.05)

        slowprint("~Sun Tzu says this because a desperate foe will fight with their best; they will fight\n"
        "with their life. And on this day, you will fight with your best; you will fight with your life.\n", 0.05)

        slowprint("Press enter to roll for your life (1 you live, 2 you die).", 0.05)
        input()

        '''Life and death determined by dice as the character faces against a horde of gremlins'''
        survival = 2

        print("You rolled a...", str(survival) + ".\n")
        sleep(2)

        if (survival == 1):
            print("\n" * 100)
            slowprint("~You've done nothing short of defying heaven, for somehow you\n"
            "slaughtered all the enemies. Covered in severe in-\n", 0.04)

            slowprint(first_name + ": Okay, better go back to the village. This forest sucks!\n", 0.04)

            slowprint("~Okay thanks for interrupting me. Anyways, covered in severe injuries, you\n"
            "limp back towards the village you saw earlier, leaving a trail of blood in the snow.~", 0.04)
            slowprint('~Upon entry, you hear cheering.~\n', 0.04)

            sleep(1)
            for i in range(3):
                sleep(1)
                print("Villagers: Hero!")

            print()
            slowprint("~The village elder nods at you and leaves.", 0.05)

        if (survival == 2):
            slowprint("~You fought hard, but as the horde of gremlins tears away at you. I'm afraid\n"
            "there's nothing left. What an unpleasent way to go.~", 0.04)

            print("\n" * 100)
            dead_end()

# War support route
def lumberer(first_name, last_name):
    slowprint("~The day begins as expected. With the art of axe swinging, you\n"
    "hack away at the pine and sakura trees. As your hands begin to\n"
    "become covered in blisters, you notice a hard working fellow\n"
    "beside you.~", 0.04)
    slowprint("~He seems like a a young adult and his eyes gleam with\n"
    "determination. As if hacking down an enemy, he hacks at\n"
    "the trees non-stop. It seems that the frigid temperature\n"
    "does not faze him in the slightest.~", 0.04)
    slowprint("~Point is, he catches your curiosity.~\n", 0.04)

    print("1 = Talk to him")
    print("2 = Keep chopping and mind your own business\n")

    convo = int(input("Choose: "))

    if (convo == 1):

        print("\n" * 100)

        slowprint(first_name + ": Hey dude, you chop trees like time is running out! How are\n"
        "you so strong and persistent in such weather?", 0.04)
        slowprint("Salazar: Hm? Oh aren't you the newbie lumberer they sent?", 0.04)
        slowprint(first_name + ": Yup.", 0.04)
        slowprint("Salazar: What's your name?", 0.04)
        slowprint(first_name + ": " + first_name + " " + last_name, 0.04)
        slowprint("Salazar: Ah, I see, my name is Salazar and I will be your lumber\n"
        "teamate. I cut these trees like time is running out because\n"
        "time really is running out. War is upon us and I have a family\n"
        "to protect, therefore I must give it my all. After all, we can\n"
        "only win if everyone gives it their all right?", 0.04)
        slowprint(first_name + ": Still though... Your covered in bruises and your hands are\n"
        "as mess of blood. Are you okay dude?", 0.04)
        slowprint("Salazar: I have to be. Thank you for your kind consideration\n"
        "friend.", 0.04)
        slowprint(first_name + ": Not to worry, I have your back.", 0.04)

    if (convo == 2):

        print("\n" *100)

        slowprint("~You decide it is better not to bother him. Although, you know he\n"
        "is your lumber teamate, it is best not to have too much\n"
        "conversation while during work.~", 0.04)
        slowprint("~As you continue to chop the trees, an arrow whizzes by\n"
        "your face.~\n", 0.03)

    slowprint("Salazar: Not good, Wood elves! GO! Tell Lumber Jack now!!!\n",0.04)

    print("1 = Run to report Lumber Jack about the wood elves")
    print("2 = Stay and help Salazar fight\n")

    ambush_decision = int(input("choose: "))

    if (ambush_decision == 1):

        print("\n" * 100)

        slowprint(first_name + ": Got it! I'll report it immediately!\n", 0.04)

        slowprint("~As you dash off into the direction of the main lumber unit, you hear\n"
        "a wet thunk in the back.~",0.04)
        slowprint("~A 50 cm arrow protrudes through the back of your lumber teamate. After\n"
        "wobbling a few steps, he crumples to the floor.~", 0.04)
        slowprint("~You should see the look on your face.~\n", 0.04)

        print("Press enter to see, you have no choice.")
        input()

        mixer.init()
        oh_no = mixer.Sound("SFX/Other Sounds/Oh No.wav")
        oh_no.play()

        ohno_image = Image.open("Scenery\Oh No.jpg")
        ohno_image.show()

        print("Press enter to continue.")
        input()

        print("1 = Help Salazar (50%)")
        print("2 = Run back and report")

        sal_help = int(input("Choose: "))
        sal_success = 1

        if (sal_help == 1):
            if (sal_success == 1):

                slowprint(first_name + ": Ugh!!! I won't let you die here my friend!", 0.04)

                slowprint("~You put Salazar over your shoulder and dash back to the lumber camp.~", 0.04)
                slowprint("~After a few zig zags, you manage to lose the wood elves.~\n", 0.04)

                slowprint("Salazar: Cough... thank you friend. I think I'll be okay now.", 0.04)
                slowprint(first_name + ": Just be quiet for now, I'll make sure a medic takes a good look at that\n"
                "wound.\n", 0.04)

                slowprint("~After arriving at the camp you explain to Lumber Jack what happened.\n"
                "Hearing this news, he summons the combat squadron.~", 0.04)
                slowprint("~After a few wood elf shrieks in the distance, the head of the wood elf\n"
                "chief is up for display in the middle of the camp.~\n", 0.04)

                slowprint("Lumber Jack: You two did good out there. Have some lunch and recover, while I get a medic.", 0.04)
                slowprint(first_name + ": Thanks.", 0.04)
                slowprint("Salazar: Thanks.", 0.04)

            elif (sal_success == 2):

                slowprint(first_name + ": Ugh!!! I won't let you die here my friend!", 0.04)

                slowprint("~You put Salazar over your shoulder and dash back to the lumber camp.~", 0.04)
                slowprint("~After a few zig zags, you manage to lose the wood elves.\n~", 0.04)

                slowprint("Salazar: Cough... thank you friend. I think I'll be okay now.\n", 0.04)

                slowprint("~Those were the final words of Salazar, for he died right there on your\n"
                "shoulders.~", 0.04)

                slowprint(first_name + ": NOOOOOOO, Salazar!!!", 0.04)

                slowprint("~You find a patch of snow and place Salazar back into the earth.~", 0.04)
                slowprint("~After heading back to the camp, you break the news to the lumber\n"
                "team.~\n", 0.04)

                slowprint("Lumber Jack: DAMN WOOD ELVES!!! COMBAT SQUADRON, SLAUGHTER THEM ALL!\n", 0.04)

                slowprint("~After a few wood elf shrieks in the distance, the head of the wood elf\n"
                "chief is up for display in the middle of the camp.~\n", 0.04)

                slowprint("Lumber Jack: You did good out there. Have some lunch and recover. I'm sorry\n"
                "for what you had to see.", 0.04)
                slowprint(first_name + ": Thank you.\n", 0.04)

                slowprint("~The day ends.~", 0.04)

        elif (sal_help == 2):

            slowprint("~You heed the words of your lumber teammate and dash toward the camp.~", 0.04)
            slowprint("~You here the the wet thunk of arrows in the back, followed by the\n"
            "scream of your teammate.~\n", 0.04)

            slowprint(first_name + ": Salazar my friend, please be okay...\n", 0.04)

            slowprint("~When you finally arrive back to the camp, you explain what happened to\n"
            "Lumber Jack.~\n", 0.04)

            slowprint("Lumber Jack: DAMN WOOD ELVES!!! COMBAT SQUADRON, SLAUGHTER THEM ALL!\n", 0.04)

            slowprint("~After a few wood elf shrieks in the distance, the head of the wood elf\n"
            "chief is up for display in the middle of the camp.~", 0.04)
            slowprint("~You are horrified to see Salazar. He has been reduced to nothing less of a\n"
            "human porcupine. The combat squad lay him on a stretcher in front of you.~\n", 0.04)

            slowprint(first_name + ": Salazar... why...", 0.04)
            slowprint("Salazar: Think nothing of this brother... win the war and tell my mother I love her.\n", 0.04)

            slowprint("~Salazar has perished.~", 0.05)

            slowprint(first_name + ": *Sniff* I will.", 0.04)

            slowprint("Lumber Jack: You did the best you could. Have some lunch and recover. I'm sorry\n"
            "for this...", 0.04)
            slowprint(first_name + ": Thank you.\n", 0.04)

            slowprint("~The day ends.~", 0.04)

    elif (ambush_decision == 2):

        print("\n" * 100)

        slowprint(first_name + ": Never, friend. Scars on the back are a warrior's shame!\n", 0.04)

        slowprint("~Well said.~\n", 0.03)

        slowprint("Salazar: HAHA, With that attitude, you should've joined the army!\n"
        "Let's send these elves to hell.", 0.04)

        fight_success = dice("d2")
        if (fight_success == 1):

            slowprint("~Since this is a fantasy world, things are bound not to make sense.~", 0.04)
            slowprint("~So don't blame this narrator for leaving out the part where you are\n"
            "a master of shuriken arts.~", 0.04)
            slowprint("~With that being said, you grab the rocks lying in the snow and hurl\n"
            "them at random directions.~", 0.04)
            slowprint("~Somehow, flying at the speed of bullets, those rocks deflect off one\n"
            "another perfectly and hit every single wood elf in the trees.~", 0.04)
            slowprint("~Almost as it were raining cats and dogs, it is now raining wood elf\n"
            "carcasses.~\n", 0.04)

            slowprint("Salazar: That was insane! Are you some sort of ninja " + first_name + "?!", 0.04)
            slowprint(first_name + ": I have the power of god and anime on my side!", 0.04)
            slowprint("Salazar: You should tell me about this anime thing sometime. Anyways, let's finish\n"
            "what we've started.",0.04)
            slowprint("Salazar: You elves took my father from me when I was young...\n"
            "Now I pay you back twenty-fold!", 0.04)
            slowprint(first_name + ": I never knew that was how it was...", 0.04)
            slowprint("Salazar: It is okay, friend. I didnt mean for things to get so personal.", 0.04)

            slowprint("~However, things do get personal. Past the corpses of these wood elves,\n"
            "you both notice a settlement in the trees. Suddenly, it all made sense.~\n", 0.04)
            sleep(3)
            slowprint("~With treehouse like homes, elders, women, and children, you realise that\n"
            "these elves were not evil by nature. They were simply defending their\n"
            "homes from humans that cut the forest down.", 0.04)
            (2)
            slowprint("~But glancing at the face of Salazar, this victory did not seem enough.\n"
            "He had an aura of a man who was about to single handedly wipe out an army.~\n", 0.04)

            slowprint("Salazar: ... these wood elves have taken so much from me. My father that\n"
            "I hold so dearly lost his life to these scum. I don't think I can stop myself.\n", 0.04)

            print("1 = Stop him")
            print("2 = ...")

            stop_sal = int(input("Choose: "))

            if (stop_sal == 1):

                print("\n" * 100)

                slowprint(first_name + ": An eye for an eye, makes the whole world blind.\n"
                "Let this matter end here, friend.", 0.04)
                slowprint("Salazar: ...", 0.06)
                slowprint("Salazar: You're right. I'd be no different from them if I went for their families\n"
                "as well. Let's head back, brother. It's been a long day.", 0.04)
                slowprint(first_name + ": Agreed.", 0.04)

                slowprint("~The two of you head back to the camp and are warmly greeted by Lumber Jack.~", 0.04)

                slowprint("Lumber Jack: Hey, kiddos! I see a nice clearing of trees over\n"
                "from where you came from. You must've been busy , eh? Don't\n"
                "worry, some roast beef will make you feel better!\n", 0.04)

                slowprint("~The roast beef looks like a delicacy, you reflexively drool.~\n", 0.04)

                slowprint("Lumber Jack: Haha! Ain't nobody in the village can resist my\n"
                "homemade roast beef! Dig in lads.", 0.04)
                slowprint(first_name + ": Thank you for the food!", 0.04)
                slowprint("Salazar: Appreciated!", 0.04)

                slowprint("~You watch the sun set with Salazar and enjoy some quality roast beef.~", 0.04)

            elif (stop_sal == 2):

                print("\n" * 100)

                slowprint("~You stand in silence and watch Salazar put down his backpack.~", 0.04)
                slowprint("~He opens it to reveal multiple glass pots of firebombs.~", 0.04)
                slowprint("~As you turn your back to the forest fire that had erupted\n"
                "you begin to walk in the direction of the camp.~", 0.04)

                slowprint(first_name + ": Even in a fantasy world... huh?", 0.05)
                sleep(2)

                slowprint("~As you arrive back at the camp, Lumber Jack warmly greets you.~\n", 0.04)

                slowprint("Lumber Jack: Hey, kiddo! I see a nice clearing of trees over\n"
                "from where you came from. You must've been busy , eh? Don't\n"
                "worry, some roast beef will make you feel better!", 0.04)

                slowprint("~You reflexively gag.~", 0.04)

                slowprint("Lumber Jack: Don't like this old man's cooking, eh?\n", 0.04)

                print("1 = Diss him")
                print("2 = Lie\n")

                dis_lie = int(input("Choose: "))

                if (dis_lie == 1):
                    slowprint(first_name + ": Haha... lumberers don't cook. I'll pass, thanks for the offer\n"
                    "though.", 0.04)
                    slowprint("Lumber Jack: Ehhhh, dumb kid. You don't know what your missing out\n"
                    "on! Anyways, suit yourself.", 0.04)

                elif (dis_lie == 2):
                    slowprint(first_name + ": No no, it's nothing like that. I just ate already, I'm too full.", 0.04)
                    slowprint("Lumber Jack: Oh that woul explain the smoke I'm seeing in the\n"
                    "direction you came from!", 0.04)
                    slowprint(first_name + ": Yeah...", 0.04)
                    slowprint("Lumber Jack: Pfft, lazy kid. Don't take such an early lunch break\n"
                    "next time! Some of us actually work our full hours, yknow???",0.04)
                    slowprint(first_name + ": Sorry, boss.", 0.04)

                slowprint("~The day ends.~", 0.04)
        elif (fight_success == 2):
            slowprint("~As the arrows fly free, you two find yourselves not a match for the elves.~", 0.04)
            slowprint("~With the loss of a blood in such freezing temperatures. You both are doomed to\n"
            "die.~", 0.04)
            slowprint("~The result is quite gruesome...~\n", 0.04)

            show_arrow_death = input("Want to see how gruesome? (Yes/No): ")

            if (show_arrow_death == "Yes"):
                arrow_death = Image.open("Scenery\Death By Arrows.jpg")
                arrow_death.show()

            input("Press enter when you are ready to continue.\n")

            slowprint("Salazar: We fought well, I hope we can be brothers again in the next life...", 0.04)
            slowprint(first_name + ": *Coughs blood* Second chances are rare enough, but if there is a third one,"
            "let us meet once again!", 0.04)

            print("\n" *100)

            dead_end()

def frontline_training():
    slowprint("You immediately grasp the techniques of the sword, it turns out\n"
    "you are a genius in the arts.", 0.04)


def cliff_hanger():
    '''Cliff hanger'''

    slowprint("~As you sleep and the day of preparation comes to an end\n"
    "you prepare yourself for the upcoming war.~", 0.04)
    slowprint("~To be continued in... Raganarok: Appleville Arc!~", 0.04)
