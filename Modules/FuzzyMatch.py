from difflib import get_close_matches # Needed for the fuzzy matching of the mode input

def fuzzy_loop():
    pass


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




  # Gets value for the distance between the 2 endpoints (pointToPointDist)
    # Asks for which mode the user wants to use, EZ or ADV
    print(f"\nWhat is the distance between the 2 ports?")
    print(f'There are 2 ways to measure this distance\nIf you know the distance in inches, enter "EZ"\nIf you do not know the distance, enter "ADV"')
    optionListOne = ["ez", "adv"]
    fuzzyData = {
        "cutoffValue": 0.45,    # Max strip slack before error
        "input": f"Mode (EZ/ADV) {syntax} "     
    }
    mode = input_loop(debug, fuzzyData, optionListOne)
    # optionList (ez, adv, etc)