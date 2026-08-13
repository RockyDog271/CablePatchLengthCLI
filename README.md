# CablePatchLengthCLI
A Python command-line tool designed to calculate the recommended cut length for Ethernet patch cables based on the distance between the connected devices, connector size, bend radius, and preferred termination slack.

## Features
> Calculate cable length using a simple measurement ("EZ" mode)
> Calculate port-to-port distance using rack and port measurements ("ADV" mode)
> Fuzzy matching for text-based options
> Input validation with minimum and maximum values
> Modular Python structure
> Rounded calculations to two decimal places

The program calculates the recommended cable length using several measurements:
> Minimum cable bend radius
> Maximum clearance around obstacles
> Connector length
> Termination slack
> Port-to-port distance

## V0.3 Planned Features
Advanced and Basic DEBUG options in Main
At least one if not more unit tests
Bugfix of the "maxbendradius" having too much effect on the cable length when more then 6"

## V0.4 Planned Features
menu options at the start of the program
I forgot that classes exist so changing the dictionary's being used to classes instead