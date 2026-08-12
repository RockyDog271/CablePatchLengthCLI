from ast import While
from multiprocessing.util import debug


def InitialStartup ():
# A bunch of print statements to start the program in CLI
    print(f"\n\n")
    print(f"         ------------------------------------         ")
    print(f"         ------ \033[32mCable Patch Length CLI\033[0m ------         ")
    print(f"         ----------  \033[34mBy Rocky :3c\033[0m  ----------         ")
    print(f"         ------------------------------------         ")
    print(f"\n")
# START \033[34m AND \033[32m
# END \033[0m

def QuestionScript ():
    Syntax = "=" # For what the typing prompt starts with :)
    Debug = True # For debugging purposes, if you want to see the values of the variables

    # Print and Answers for the basic necessities of the program

    # Gets value for the minimum bend radius of the cable (minBendRadius)
    print(f"\nWhat is the minimum bend radius of the cable? (in inches)?")
    print(f"   (The default suggestion is 1.0)")
    while True:
        try:
           minBendRadius = float(input(f"\nMinimum bend radius {Syntax} "))
           minBendRadius = "{:.2f}".format(minBendRadius)
           if Debug: print(f"Debug message: {minBendRadius}")
           break 
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            print(f"   (Examples are; 0, 0.0, 0.00)")

    # Gets value for the minimum bend radius of the cable (minBendRadius)
    print(f"\nWhat is the max clearance before the cables conflict with an obstacle? (in inches)?")
    print(f"   (If you don't know, just type 0)")
    while True:
        try:
            maxBendRadius = float(input(f"\nClearance {Syntax} "))
            if maxBendRadius == 0:
               maxBendRadius = 30
            if maxBendRadius >= 3:
                maxBendRadius = 2.5
            maxBendRadius = "{:.2f}".format(maxBendRadius)
            if Debug: print(f"Debug message: {maxBendRadius}")
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            print(f"   (Examples are; 0, 0.0, 0.00)")

    # Return gathered vars :P
    return minBendRadius, maxBendRadius 