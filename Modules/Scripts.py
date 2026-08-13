from difflib import get_close_matches # Needed for the fuzzy matching of the mode input
import math # Needed for the complex math thingies

def Math(oneU, onePort, topPort, middlePort, lowerPort, uHeight, patchPortPosition, devicePortPosition, portDistance):
    # This gets the main distance done and out of the way
    horizontalDistance = uHeight * oneU   # Distance from U to U (rough est)

    # THis gets vertical done and out of the way so I don't have to deal with it more
    verticalDistance = portDistance * onePort

    # This is used because I did complex stuff and things that could have been cleaner earlier but it is too late :c
    adjustments = {
        "bottom": lowerPort,
        "middle": middlePort,
        "top": topPort
    }
    horizontalDistance -= adjustments[patchPortPosition]                            # This takes the HozDist and subtracts based on the dictionary reference
    horizontalDistance -= adjustments[devicePortPosition]                           # This takes the HozDist and subtracts based on the dictionary reference
    pointToPointDist = math.sqrt(verticalDistance**2 + horizontalDistance**2)       # This finds the distance between the 2 points (in inches ofc :3)
    pointToPointDist = round(pointToPointDist, 2)                                   # Just painting a happy little rounded number :D                              
    return pointToPointDist

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
    Debug = False # For debugging purposes, if you want to see the values of the variables

    # Print and Answers for the basic necessities of the program

    # Gets value for the minimum bend radius of the cable (minBendRadius)
    print(f"\nWhat is the minimum bend radius of the cable? (in inches)?")
    print(f"   (The default suggestion is 1.0(in)")
    while True:
        try:
           minBendRadius = float(input(f"\nMinimum bend radius {Syntax} "))
           minBendRadius = round(minBendRadius, 2)
           if Debug: print(f"Debug message: {minBendRadius}")
           break 
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            print(f"   (Examples are; 0, 0.0, 0.00)")

    # Gets value for the maximum bend radius of the cable (maxBendRadius)
    print(f"\nWhat is the max clearance before the cables conflict with an obstacle? (in inches)?")
    print(f"   (If you don't know, just type 0")
    while True:
        try:
            maxBendRadius = float(input(f"\nClearance {Syntax} "))
            if maxBendRadius == 0:
               maxBendRadius = 30
            if maxBendRadius >= 3:
                maxBendRadius = 2.5
            maxBendRadius = round(maxBendRadius, 2)
            if Debug: print(f"Debug message: {maxBendRadius}")
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            print(f"   (Examples are; 0, 0.0, 0.00)")

    # Gets value for the size of the connectors used (in inches) this is the connectorSize Var
    print(f"\nWhat is the size of the connectors you are using on these patch cables? (in inches pls)")
    print(f"   (Typically connectors with cable relief is 2.0(in) and normal RJ-45 pass-through is 1.0(in)")
    while True:
        try:
           connectorSize = float(input(f"\nPlease enter your connector size {Syntax} "))
           connectorSize = round(connectorSize, 2)
           if Debug: print(f"Debug message: {connectorSize}")
           break 
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            print(f"   (Examples are; 0, 0.0, 0.00)")

    # Gets value for preferred amount of cutoff slack VAR = slackCutoff
    print(f"\nHow much slack do you cut off when stripping CAT cable in prep for termination?")
    print(f"   (The default suggestion is 2.0(in) of slack")
    while True:
        try:
           slackCutoff = float(input(f"\nPlease enter your preferred slack when terminating CAT cable {Syntax} "))
           slackCutoff = round(slackCutoff, 2)
           if Debug: print(f"Debug message: {slackCutoff}")
           break 
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            print(f"   (Examples are; 0, 0.0, 0.00)")


    # Gets value for the distance between the 2 endpoints (pointToPointDist)
    # Asks for which mode the user wants to use, EZ or ADV
    print(f"\nWhat is the distance between the 2 ports?")
    print(f'There are 2 ways to measure this distance\nIf you know the distance in inches, enter "EZ"\nIf you do not know the distance, enter "ADV"')

    # Takes the mode input and checks for validity, then moves on (see next section)
    while True:
        mode = input(f"\nMode (EZ/ADV) {Syntax} ")                               # Gets the user input
        mode = mode.lower()                                                      # Takes the input and makes it lowercase
        matches = get_close_matches(mode, ["ez", "adv"], n = 1, cutoff = 0.45)   # Uses the thing I imported to use fuzzy check for if the input is close to the valid options,
        if matches:
            mode = matches[0]                                                    # If the input is close enough to a valid option, it will set the mode to that option
            if Debug: print(f"Debug message: {mode}")                            # Prints the mode for debugging purposes  (I put this msg cuz it looked wrong without it)
            break
        else:
            print("\nInvalid input. Please enter a valid mode.")
            print(f'   (Examples are; "EZ, ez", "ADV, adv")')

    # This has the two menu options, depending on what the user chose, EZ is first.
    while True:
        if mode == "ez":
            try:
                pointToPointDist = float(input(f"\nPlease enter the distance between the 2 ports (in inches) {Syntax} "))
                pointToPointDist = round(pointToPointDist, 2)
                if Debug: print(f"Debug message: {pointToPointDist}")
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
                print(f"   (Examples are; 0, 0.0, 0.00)") # OwO
        elif mode == "adv":
            oneU = 1.75         # This value is the U height of a rack
            onePort = 0.50      # This value is the rough width of a port
            topPort = -0.75     # This value is what is subtracted from "oneU" to get the middle point of the top port
            middlePort = -0.85  # This value is what is subtracted from "oneU" to get the middle point of the middle port
            lowerPort = 1.25    # This value is what is subtracted from "oneU" to get the middle point of the bottom port

            # The distance in U
            print(f"\nThere are a total of x questions to answer, please answer them as accurately as possible, in the unit requested.")
            print(f"------------------------------------------------------------------------------------------------------------------")
            print(f"how many U's is the gap from your patch panel to the network device? (in U's) (1U = 1.75 inches)")
            print(f"   (Examples are; 0, 0.0, 0.00)")
            while True:
                try:
                    uHeight = float(input(f"\nPlease enter the height in U's {Syntax} "))
                    break
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")
                    print(f"   (Examples are; 0, 0.0, 0.00)")

            # The position of the port on the patch panel
            print(f"\nIs the port on your patch panel centered, or is it on the top or bottom of the U? (top/middle/bottom)")
            while True:
                patchPortPosition = input(f"\nPlease enter the position of the port (top/middle/bottom) {Syntax} ")
                patchPortPosition = patchPortPosition.lower()
                matches = get_close_matches(patchPortPosition, ["top", "middle", "bottom"], n = 1, cutoff = 0.45)
                if matches:
                    patchPortPosition = matches[0]
                    if Debug: print(f"Debug message: {patchPortPosition}")
                    break
                else:
                    print("\nInvalid input. Please enter a valid position.")
                    print(f'   (Examples are; "top, Top", "middle, Middle", "bottom, Bottom")')

            # The position of the port on the network device
            print(f"\nIs the port on your network device centered, or is it on the top or bottom of the U? (top/middle/bottom)")
            while True:
                devicePortPosition = input(f"\nPlease enter the position of the port (top/middle/bottom) {Syntax} ")
                devicePortPosition = devicePortPosition.lower()
                matches = get_close_matches(devicePortPosition, ["top", "middle", "bottom"], n = 1, cutoff = 0.45)
                if matches:
                    devicePortPosition = matches[0]
                    if Debug: print(f"Debug message: {devicePortPosition}")
                    break
                else:
                    print("\nInvalid input. Please enter a valid position.")
                    print(f'   (Examples are; "top, Top", "middle, Middle", "bottom, Bottom")')

            # Get the left // right distance between the ports
            print(f"\nWhat is the distance between the ports, left to right? please count the distance by counting how many ports apart the switches,\nwether it is left or right doesn't matter")
            while True:
                try:
                    portDistance = int(input(f"\nPlease enter the distance between the ports (in port count) {Syntax} "))
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")
                    print(f"   (Examples are; 0, 1, 2, 3, 4, 5, etc.)")
                pointToPointDist = Math(oneU, onePort, topPort, middlePort, lowerPort, uHeight, patchPortPosition, devicePortPosition, portDistance)
                break
            break

    # Return gathered vars :P
    return minBendRadius, maxBendRadius, connectorSize, slackCutoff, pointToPointDist


def CableLengthCalc (minBendRadius, maxBendRadius, connectorSize, slackCutoff, pointToPointDist):
    if minBendRadius < 1.5:
        maxBendRadius = maxBendRadius + 1.5
    cableLength = connectorSize * 2                # Takes the connector size and *2 (for each side)
    cableLength = cableLength - (0.25 * 2)         # Subtracts the .25 that the cable doesn't pull through the connector (for each side)
    cableLength = cableLength + pointToPointDist   # Adds the main length factor
    cableLength = cableLength + (maxBendRadius//3) # This works good for me when it comes to adding bend
    cableLength = cableLength + (slackCutoff * 2)  # adding the slack cutoff for both ends of the cable
    cableLength = "{:.2f}".format(cableLength)
    return cableLength

 

# connector + connector -.25 -.25 (since connector doesnt have cable go all the way through) + cutpoint (length of slack) + distancepoint to point, and then + (bend // 3)

