'''

Programmer: Eric, Yathusan, and Omar

Date of Creation: May 27, 2022

Description: Mainline logic for Ragnarok Akansu Village Arc

'''

import akansu_functions_and_classes

def main():
    '''Pre-game notes'''
    akansu_functions_and_classes.pre_game()

    '''Title screen'''
    akansu_functions_and_classes.title_screen()

    '''Character creation'''
    first_name = input("Okay, pick your name:\n")
    print()

    last_name = input("Last name?\n")
    print()

    age = int(input("Age?\n"))
    print()

    while (age < 0):
        print("Sorry, no fetuses or non-existent entities allowed to play this game. Try again.\n")

        age = input("Age?\n")
        print()

    print("\n" * 100)

    '''Name easter egg'''
    akansu_functions_and_classes.name_easter_egg(first_name, last_name)

    '''Isekai time'''
    akansu_functions_and_classes.isekai(last_name)

    '''Begin at the edge of Sakura Forest'''
    arrival_decision = akansu_functions_and_classes.arrival(first_name)

    '''Enter the village'''
    if (arrival_decision == 1):
        village_decision = akansu_functions_and_classes.enter_akansu(first_name, age)

        if (village_decision == 1):
            job_decision = akansu_functions_and_classes.enter_tavern(first_name, last_name)

        if (village_decision == 2):
            job_decision = akansu_functions_and_classes.old_man(first_name, last_name)

    '''Enter the forest'''
    if (arrival_decision == 2):
        akansu_functions_and_classes.enter_forest(first_name, last_name)

        village_decision = akansu_functions_and_classes.enter_akansu(first_name, age)

        if (village_decision == 1):
            job_decision = akansu_functions_and_classes.enter_tavern(first_name, last_name)

        if (village_decision == 2):
            job_decision = akansu_functions_and_classes.old_man(first_name, last_name)

    '''Lumberer'''
    if (job_decision == 1):
        akansu_functions_and_classes.frontline_training()

    if (job_decision == 2):
        akansu_functions_and_classes.lumberer(first_name, last_name)

    '''Frontline training'''

    '''Cliff hanger'''
    akansu_functions_and_classes.cliff_hanger()

main()
input()
