import traceback

def debug_printout(debug, valueName, valuePrintout):
    if debug in (1, 3):
        print(f"\n\033[31mDEBUG PRINTOUT, the value of {valueName} is {valuePrintout}\033[32m")
# debug_printout(debug, "VAR NAME HERE", numericValue)

def debug_exception(debug, exception):
    if debug in (2, 3):
        print(f"\n\033[31mDEBUG PRINTOUT, Exception printout: {exception}\033[32m\n")
        traceback.print_exc()
# debug_exception(debug, exception)

def debug_value_printout(debug, inputData):
    if debug in (1, 3):
        # Extracted the values from inputData
        maxValue = inputData["maxValue"]
        minValue = inputData["minValue"]
        print(f"\n\033[31mDEBUG PRINTOUT, the MIN value listed is {minValue}\033[32m")
        print(f"\n\033[31mDEBUG PRINTOUT, the MAX value listed is {maxValue}\033[32m")
# except Exception as exception
# debug_value_printout(debug, inputData)