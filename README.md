# CablePatchLengthCLI  
A Python command-line tool designed to calculate the recommended cut length for Ethernet patch cables based on the distance between the connected devices, connector size, bend radius, and preferred termination slack.  

## Features  
> Calculate cable length using a simple measurement ("EZ" mode)  
> Calculate port-to-port distance using rack and port measurements ("ADV" mode)  
> Fuzzy matching for text-based options  
> Input validation with minimum and maximum values  
> Modular Python structure  
> Rounded calculations to two decimal places  
> Basic - Advance debug printout and traceback options  
> Unit tests for development assistance  

The program calculates the recommended cable length using several measurements:  
> Minimum cable bend radius  
> Maximum clearance around obstacles  
> Connector length  
> Termination slack  
> Port-to-port distance  
  
## Relevant Information
This is a practice project, used to help develop my overall python skills.  
This does not mean that it is untested, I use this program for all of my patch cable calculations,  
I came up with the idea for this practice project when I was making an excel equation to automate this, and figured it would be good code practice.  
- Note by: Logan Simila, 08/21/2026  
  
## Currently Known Bugs  
BUG: "maxbendradius" variable has too much effect on the cable length when <6"  
-> Discovered by Logan when making some open-air patch cables  
  
CLARITY: The prompt asking for clearance goes to the VAR "maxBendRadius" when it should be something like "clearance" or smthn  
  
CLARITY: patchPortPosition and devicePortPosition are hard coded to ontop of eachother, this can be remedied by changing to topMounted and lowerMounted or smthn  