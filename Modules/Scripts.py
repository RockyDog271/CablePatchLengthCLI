from MathModules import distance_math_function
from InputModule import input_loop
from FuzzyMatch import fuzzy_loop

def initial_startup_script ():
# A bunch of print statements to start the program in CLI
    print(f"\n\n")
    print(f"     --------------------------------------------     ")
    print(f"     ---------- \033[32mCable Patch Length CLI\033[0m ----------     ")
    print(f"     --------------  \033[34mBy Rocky :3c\033[0m  --------------     ")
    print(f"     --------------------------------------------     ")
    print(f"\n")
# START \033[34m AND \033[32m
# END \033[0m

def data_input_script (debug, syntax):
    # Gets value for the minimum bend radius of the cable (minBendRadius)
    print(f"\nWhat is the minimum bend radius of the cable? (in inches)?")
    print(f"   (The default suggestion is 1.0(in)")
    inputData = {
        "maxValue": 10,   # Max bend radius before error
        "minValue": .75,  # Min bend radius before error
        "input": f"Minimum bend radius {syntax} "
    }
    minBendRadius = input_loop(debug, inputData)

    # Gets value for the maximum bend radius of the cable (maxBendRadius)
    print(f"\nWhat is the max clearance before the cables conflict with an obstacle? (in inches)?")
    print(f"   (If you don't know, just type 30")
    inputData = {
        "maxValue": 30,   # Max clearance before error
        "minValue": 1.5,  # Min clearance before error
        "input": f"Clearance {syntax} "
    }
    maxBendRadius = input_loop(debug, inputData)


    # Gets value for the size of the connectors used (in inches) this is the connectorSize Var
    print(f"\nWhat is the size of the connectors you are using on these patch cables? (in inches pls)")
    print(f"   (Typically connectors with cable relief is 2.0(in) and normal RJ-45 pass-through is 1.0(in)")
    inputData = {
        "maxValue": 5,    # Max connector size before error
        "minValue": .25,  # Min connector size before error
        "input": f"Connector length {syntax} "
    }
    connectorSize = input_loop(debug, inputData)


    # Gets value for preferred amount of cutoff slack VAR = slackCutoff
    print(f"\nHow much slack do you cut off when stripping CAT cable in prep for termination?")
    print(f"   (The default suggestion is 2.0(in) of slack")
    inputData = {
        "maxValue": 5,    # Max strip slack before error
        "minValue": .25,  # Min strip slack before error
        "input": f"Slack cutoff length {syntax} "
    }
    slackCutoff = input_loop(debug, inputData)

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
    if mode == "ez":
        inputData = {
            "maxValue": 240,    # Max length before error
            "minValue": 2.25,   # Min length slack before error
            "input": f"Distance between the (2) points (in inches) {syntax} "
        }
        pointToPointDist = input_loop(debug, inputData)

    elif mode == "adv":
            # Advanced prep msg :3
            print(f"\nThere are a total of x questions to answer, please answer them as accurately as possible, in the unit requested.")
            print(f"------------------------------------------------------------------------------------------------------------------")

            # The distance between the two devices in U
            print(f"how many U's is the gap from your patch panel to the network device? (in U's) (1U = 1.75 inches)")
            print(f"   (Examples are; 0, 0.0, 0.00)")
            inputData = {
                "maxValue": 240,    # Max length before error
                "minValue": 2.25,   # Min length slack before error
                "input": f"Height (in rack U) {syntax} "
            }
            uHeight = input_loop(debug, inputData)

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
                pointToPointDist = (uHeight, patchPortPosition, devicePortPosition, portDistance)
                break
            break

    # Return gathered vars :P
    return minBendRadius, maxBendRadius, connectorSize, slackCutoff, pointToPointDist



