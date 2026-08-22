from .DebugModule import debug_exception

class ValueTooHigh(Exception):
    pass
class ValueTooLow(Exception):
    pass

def input_loop(debug, input_data):
    while True:
        try:
            # Extracted the values from input_data
            max_value = input_data["max_value"]
            min_value = input_data["min_value"]
            outputText = input_data ["input"]

            # Asks the user for the value
            numeric_value = float(input(f"\033[34m{outputText}\033[0m"))

            # I feel like this is a rare case where the code is self-documenting
            if numeric_value > max_value:
                raise ValueTooHigh
            elif numeric_value < min_value:
                raise ValueTooLow

            numeric_value = round(numeric_value, 2)
            break

        # All of the exception checks
        except ValueError as exception:
            print("\n\033[31mInvalid input. Please enter a valid number.\033[32m")
            print(f"   (Examples are; 0, 0.0, 0.00)")
            debug_exception(debug, exception)
        except ValueTooHigh as exception:
            print("\n\033[31mInvalid input. Input is too high!\033[32m")
            print(f"   (The maximum value allowed is {max_value}, you entered {numeric_value})")
            debug_exception(debug, exception)
        except ValueTooLow as exception:
            print("\n\033[31mInvalid input. Input is too low!\033[32m")
            print(f"   (The minimum value allowed is {min_value}, you entered {numeric_value})")
            debug_exception(debug, exception)
        except Exception as exception:
            debug_exception(debug, exception)
    return numeric_value # note that this will be any VAR for whatever called this function