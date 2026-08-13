# import os

# Local imports
from Modules.Scripts import InitialStartup as SetupScript
from Modules.Scripts import QuestionScript
from Modules.Scripts import CableLengthCalc

# Name of Script and other things
try:
    SetupScript()
except:
    print("Error231: Something went wrong!")

while True:
    try:
        minBendRadius, maxBendRadius, connectorSize, slackCutoff, pointToPointDist = QuestionScript()
    except:
        print("Error232: Something went wrong!")
    try:
        cableSize = CableLengthCalc(minBendRadius, maxBendRadius, connectorSize, slackCutoff, pointToPointDist)
    except:
        print("Error233: Something went wrong!")

    print(f"\nFor your patch cables, you should cut {cableSize} inches of cable!^^")

    # I have to go to work in like 10m so I have to finish this fast 
    RRS = input(f"\nWould you like to calc another cable? (Y/N)")
    if RRS == "Y":
        pass
    if RRS == "N":
        break
    else:
        break