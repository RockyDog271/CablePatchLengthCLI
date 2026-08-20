from .DebugModule import * 

class ValueTooHigh(Exception):
    pass
class ValueTooLow(Exception):
    pass

def input_loop(debug, inputData):
    while True:
        try:
            # Extracted the values from inputData
            maxValue = inputData["maxValue"]
            minValue = inputData["minValue"]
            outputText = inputData ["input"]

            # Asks the user for the value
            numericValue = float(input(f"\033[34m{outputText}\033[0m"))

            # I feel like this is a rare case where the code is self-documenting
            if numericValue > maxValue:
                raise ValueTooHigh
            elif numericValue < minValue:
                raise ValueTooLow
            else: # This isn't needed, I may remove in the future but I might try something first
                numericValue = round(numericValue, 2)
                break

        # All of the exception checks
        except ValueError as exception:
            print("\n\033[31mInvalid input. Please enter a valid number.\033[32m")
            print(f"   (Examples are; 0, 0.0, 0.00)")
            debug_exception(debug, exception)
        except ValueTooHigh as exception:
            print("\n\033[31mInvalid input. Input is too high!\033[32m")
            print(f"   (The maximum value allowed is {maxValue}, you entered {numericValue})")
            debug_exception(debug, exception)
        except ValueTooLow as exception:
            print("\n\033[31mInvalid input. Input is too low!\033[32m")
            print(f"   (The minimum value allowed is {minValue}, you entered {numericValue})")
            debug_exception(debug, exception)
        except Exception as exception:
            debug_exception(debug, exception)
    return numericValue # note that this will be any VAR for whatever called this function