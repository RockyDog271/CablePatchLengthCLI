from difflib import get_close_matches # Needed for the fuzzy matching of the mode input

def fuzzy_loop(debug, fuzzyData, optionList):
    fuzzAmount = fuzzyData["cutoffValue"]
    outputText = fuzzyData["input"]

    while True:
        # Asks the user for the value
        charValue = float(input(f"\033[34m{outputText}\033[0m")) # also maybe name the VAR fuzzyValue ?
        charValue = charValue.lower()
        matches = get_close_matches(charValue, [optionList], n = 1, cutoff = fuzzAmount) 

        if matches:
            charValue = matches[0]
            break
        else:
            print("\n\033[31mInvalid input. Please enter a valid input.\033[32m")
            print(f"   (Examples are; {', '.join(optionList)}, {', '.join(option.upper() for option in optionList)})")  # Thank you to my friend for helping me, I was stuck on this for a good minute lol
    return charValue
