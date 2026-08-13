# CablePatchLengthCLI

Objectives

> Add debug options to main and pass them to modules
> add adv and simple debuf modes, one to print exceptions and one just for mine

> add a unit test or 2


> replace "math" with something more descriptive

> fix bug in portExcept

> remove whileTRUE around ez/adv mode selector

> add menu options at start

> fix unprofessial part at end of main

> create reusable input function

> create reusable fuzzy match function

> dont change number to strung, keep it a float (end def)

> add input validation (input too low, input too high)


            if maxBendRadius == 0:
               maxBendRadius = 30
            if maxBendRadius >= 3:
                maxBendRadius = 2.5
            maxBendRadius = round(maxBendRadius, 2)


I forgot that data classes exist