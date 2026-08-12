# import os

# Local imports
from Modules.Scripts import InitialStartup as SetupScript
from Modules.Scripts import QuestionScript

# Name of Script and other things
SetupScript()

while True:
    minBendRadius, maxBendRadius = QuestionScript()
    print("hi")