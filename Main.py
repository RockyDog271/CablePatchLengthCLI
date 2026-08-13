# Local imports
from Modules.Scripts import initial_startup_script

debug = 0
# [0] = Debug disabled
# [1] = Basic Debug enabled (Unique Errors and Value prints only)
# [2] = Adv Debug enabled (Prints the exceptions as well as the basic Debug output)

syntax = "="
# Common options are "=" ">>" and ":"
# Ex: "Question answer here = "

try:
    initial_startup_script(debug, syntax)
except:
    if debug == 1 : print("Error100")