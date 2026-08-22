from difflib import get_close_matches # Needed for the fuzzy matching of the mode input
# from .DebugModule import debug_value_printout
# from .DebugModule import debug_exception
# from .DebugModule import debug_printout

def fuzzy_loop(debug, fuzzy_data, option_list):
    fuzz_amount = fuzzy_data["cutoffValue"]
    output_text = fuzzy_data["input"]

    while True:
        # Asks the user for the value
        char_value = input(f"\033[34m{output_text}\033[0m") # also maybe name the VAR fuzzy_value ?
        char_value = char_value.lower()
        matches = get_close_matches(char_value, option_list, n = 1, cutoff = fuzz_amount) 

        if matches:
            char_value = matches[0]
            break
        else:
            print("\n\033[31mInvalid input. Please enter a valid input.\033[32m")
            print(f"   (Examples are; {', '.join(option_list)}, {', '.join(option.upper() for option in option_list)})")  # Thank you to my friend for helping me, I was stuck on this for a good minute lol
    return char_value
