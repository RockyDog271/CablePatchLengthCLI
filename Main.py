# Local imports
from Modules.Scripts import initial_startup_script
from Modules.Scripts import data_input_script
from Modules.MathModules import cable_length_calc
from Modules.DebugModule import * # This includes "debug_printout", "debug_exception", & "debug_value_exception"
# debug_printout(debug, "VAR NAME HERE", numericValue)
# ----------------------------------------
# debug_value_printout(debug, inputData)
# ----------------------------------------
# except Exception as exception
# debug_exception(debug, exception)

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
except Exception as exception:
    debug_exception(debug, exception)