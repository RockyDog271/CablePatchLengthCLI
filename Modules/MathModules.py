from .DebugModule import * 
import math

def distance_math_function(u_height, patch_port_position, device_port_position, port_distance, debug):
    one_u = 1.75         # This value is the U height of a rack
    one_port = 0.50      # This value is the rough width of a port (measure from 3 patch panels and AVG'd)
    top_port = -0.75     # This value is what is subtracted from "one_u" to get the middle point of the top port (measured from a Cisco2960)
    middle_port = -0.85  # This value is what is subtracted from "one_u" to get the middle point of the middle port (measured from a CiscoASA)
    lower_port = 1.25    # This value is what is subtracted from "one_u" to get the middle point of the bottom port (measured from a Cisco2960)

    # This gets the main distance done and out of the way
    horizontal_distance = u_height * one_u   # Distance from U to U (rough est)
    debug_printout(debug, "horizontal_distance", horizontal_distance)

    # THis gets vertical done and out of the way so I don't have to deal with it more
    vertical_distance = port_distance * one_port
    debug_printout(debug, "vertical_distance", vertical_distance)

    # This is used because I did complex stuff and things that could have been cleaner earlier but it is too late :c
    adjustments = {
        "bottom": lower_port,
        "middle": middle_port,
        "top": top_port
    }
    horizontal_distance -= adjustments[patch_port_position]                               # This takes the HozDist and subtracts based on the dictionary reference
    horizontal_distance -= adjustments[device_port_position]                              # This takes the HozDist and subtracts based on the dictionary reference
    point_to_point_dist = math.sqrt(vertical_distance**2 + horizontal_distance**2)        # This finds the distance between the 2 points (in inches ofc :3)
    point_to_point_dist = round(point_to_point_dist, 2)                                   # Just painting a happy little rounded number :D                              
    return point_to_point_dist

def cable_length_calc (min_bend_radius, max_bend_radius, connector_size, slack_cutoff, point_to_point_dist):
    if min_bend_radius < 1.5:
        max_bend_radius = max_bend_radius + 1.5
    cable_length = connector_size * 2                   # Takes the connector size and *2 (for each side)
    cable_length = cable_length - (0.25 * 2)            # Subtracts the .25 that the cable doesn't pull through the connector (for each side)
    cable_length = cable_length + point_to_point_dist   # Adds the main length factor
    cable_length = cable_length + (max_bend_radius//3)  # This works good for me when it comes to adding bend
    cable_length = cable_length + (slack_cutoff * 2)    # adding the slack cutoff for both ends of the cable
    cable_length = round(cable_length, 2)    
    return cable_length