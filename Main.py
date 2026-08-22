# Local imports
from Modules.Scripts import initial_startup_script
from Modules.Scripts import data_input_script
from Modules.MathModules import cable_length_calc
from Modules.DebugModule import debug_exception
from Modules.DebugModule import debug_printout
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
    min_bend_radius, max_bend_radius, connector_size, slack_cutoff, point_to_point_dist = data_input_script(debug, syntax)
    CBLLN = cable_length_calc (min_bend_radius, max_bend_radius, connector_size, slack_cutoff, point_to_point_dist)
    print(f"------------------------------------------")
    print(f"\n   CableLength to cut is {CBLLN} inches!^^\n")
    print(f"------------------------------------------")
except Exception as exception:
    debug_exception(debug, exception)