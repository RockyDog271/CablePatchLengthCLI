from .DebugModule import * 
import math

def distance_math_function(uHeight, patchPortPosition, devicePortPosition, portDistance, debug):
    oneU = 1.75         # This value is the U height of a rack
    onePort = 0.50      # This value is the rough width of a port (measure from 3 patch panels and AVG'd)
    topPort = -0.75     # This value is what is subtracted from "oneU" to get the middle point of the top port (measured from a Cisco2960)
    middlePort = -0.85  # This value is what is subtracted from "oneU" to get the middle point of the middle port (measured from a CiscoASA)
    lowerPort = 1.25    # This value is what is subtracted from "oneU" to get the middle point of the bottom port (measured from a Cisco2960)

    # This gets the main distance done and out of the way
    horizontalDistance = uHeight * oneU   # Distance from U to U (rough est)
    debug_printout(debug, "horizontalDistance", horizontalDistance)

    # THis gets vertical done and out of the way so I don't have to deal with it more
    verticalDistance = portDistance * onePort
    debug_printout(debug, "verticalDistance", verticalDistance)

    # This is used because I did complex stuff and things that could have been cleaner earlier but it is too late :c
    adjustments = {
        "bottom": lowerPort,
        "middle": middlePort,
        "top": topPort
    }
    horizontalDistance -= adjustments[patchPortPosition]                            # This takes the HozDist and subtracts based on the dictionary reference
    horizontalDistance -= adjustments[devicePortPosition]                           # This takes the HozDist and subtracts based on the dictionary reference
    pointToPointDist = math.sqrt(verticalDistance**2 + horizontalDistance**2)       # This finds the distance between the 2 points (in inches ofc :3)
    pointToPointDist = round(pointToPointDist, 2)                                   # Just painting a happy little rounded number :D                              
    return pointToPointDist

def cable_length_calc (minBendRadius, maxBendRadius, connectorSize, slackCutoff, pointToPointDist):
    if minBendRadius < 1.5:
        maxBendRadius = maxBendRadius + 1.5
    cableLength = connectorSize * 2                # Takes the connector size and *2 (for each side)
    cableLength = cableLength - (0.25 * 2)         # Subtracts the .25 that the cable doesn't pull through the connector (for each side)
    cableLength = cableLength + pointToPointDist   # Adds the main length factor
    cableLength = cableLength + (maxBendRadius//3) # This works good for me when it comes to adding bend
    cableLength = cableLength + (slackCutoff * 2)  # adding the slack cutoff for both ends of the cable
    cableLength = round(cableLength, 2)    
    return cableLength