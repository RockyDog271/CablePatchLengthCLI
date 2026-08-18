# Local imports
from Modules.Scripts import initial_startup_script
from Modules.Scripts import data_input_script
from Modules.MathModules import cable_length_calc

debug = 0
# [0] = Debug disabled
# [1] = Basic Debug enabled (Unique Errors and Value prints only)
# [2] = Adv Debug enabled (Prints the exceptions as well as the basic Debug output)

syntax = "="
# Common options are "=" ">>" and ":"
# Ex: "Question answer here = "

try:
    initial_startup_script(debug)
    minBendRadius, maxBendRadius, connectorSize, slackCutoff, pointToPointDist = data_input_script(debug, syntax)
    CBLLN = cable_length_calc (minBendRadius, maxBendRadius, connectorSize, slackCutoff, pointToPointDist)
    print(f"------------------------------------------")
    print(f"\n   CableLength to cut is {CBLLN} inches!^^\n")
    print(f"------------------------------------------")
except Exception as e:
    print(f"DEBUG EXCEPTION: {type(e).__name__}: {e}")
    if debug == 1 : print("Error100")