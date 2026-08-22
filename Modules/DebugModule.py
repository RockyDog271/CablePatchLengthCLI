import traceback

def debug_printout(debug, value_name, value_printout):
    if debug in (1, 3):
        print(f"\n\033[31mDEBUG PRINTOUT, the value of {value_name} is {value_printout}\033[32m")
# debug_printout(debug, "VAR NAME HERE", numeric_value)

def debug_exception(debug, exception):
    if debug in (2, 3):
        print(f"\n\033[31mDEBUG PRINTOUT, Exception printout: {exception}\033[32m\n")
        traceback.print_exc()
# debug_exception(debug, exception)

def debug_value_printout(debug, input_data):
    if debug in (1, 3):
        # Extracted the values from inputData
        max_value = input_data["max_value"]
        min_value = input_data["min_value"]
        print(f"\n\033[31mDEBUG PRINTOUT, the MIN value listed is {min_value}\033[32m")
        print(f"\n\033[31mDEBUG PRINTOUT, the MAX value listed is {max_value}\033[32m")
# except Exception as exception
# debug_value_printout(debug, input_data)