from .MathModules import distance_math_function
from .InputModule import input_loop
from .FuzzyMatch import fuzzy_loop
from .DebugModule import debug_value_printout
from .DebugModule import debug_exception
from .DebugModule import debug_printout

def initial_startup_script (debug):
# A bunch of print statements to start the program in CLI
    print(f"\n\n")
    print(f"       --------------------------------------------     ")
    print(f"     ------------ \033[32mCable Patch Length CLI\033[0m --------------     ")
    print(f"   ------------------  \033[34mBy Rocky :3c\033[0m  ----------------     ")
    print(f"       --------------------------------------------     ")
    print(f"\n")
# START \033[34m AND \033[32m
# END \033[0m

def data_input_script (debug, syntax):
    # Gets value for the minimum bend radius of the cable (min_bend_radius)
    print(f"\nWhat is the minimum bend radius of the cable? (in inches)?")
    print(f"   (The default suggestion is 1.0(in) )")
    input_data = {
        "max_value": 10,   # Max bend radius before error
        "min_value": .75,  # Min bend radius before error
        "input": f"Minimum bend radius {syntax} "
    }
    debug_value_printout(debug, input_data)
    min_bend_radius = input_loop(debug, input_data)
    debug_printout(debug, "min_bend_radius", min_bend_radius)

    # Gets value for the maximum bend radius of the cable (max_bend_radius)
    # print(f"\nWhat is the max clearance before the cables conflict with an obstacle? (in inches)?")
    # print(f"   (If you don't know, just type thirty (30) )")
    # input_data = {
    #     "max_value": 30,   # Max clearance before error
    #     "min_value": 1.5,  # Min clearance before error
    #     "input": f"Clearance {syntax} "
    # }
    # debug_value_printout(debug, input_data)
    # max_bend_radius = input_loop(debug, input_data)
    # if max_bend_radius == 30:
    #     max_bend_radius == 3
    # debug_printout(debug, "max_bend_radius", max_bend_radius)
    max_bend_radius = 0.00

    # Gets value for the size of the connectors used (in inches) this is the connector_size Var
    print(f"\nWhat is the size of the connectors you are using on these patch cables? (in inches pls)")
    print(f"   (Typically connectors with cable relief is 2.0(in) and normal RJ-45 pass-through is 1.0(in) )")
    input_data = {
        "max_value": 5,    # Max connector size before error
        "min_value": .25,  # Min connector size before error
        "input": f"Connector length {syntax} "
    }
    debug_value_printout(debug, input_data)
    connector_size = input_loop(debug, input_data)
    debug_printout(debug, "connector_size", connector_size)

    # Gets value for preferred amount of cutoff slack VAR = slack_cutoff
    print(f"\nHow much slack do you cut off when stripping CAT cable in prep for termination?")
    print(f"   (The default suggestion is 2.0(in) of slack)")
    input_data = {
        "max_value": 5,    # Max strip slack before error
        "min_value": .25,  # Min strip slack before error
        "input": f"Slack cutoff length {syntax} "
    }
    debug_value_printout(debug, input_data)
    slack_cutoff = input_loop(debug, input_data)
    debug_printout(debug, "slack_cutoff", slack_cutoff)

    # Gets value for the distance between the 2 endpoints (point_to_point_dist)
    # Asks for which mode the user wants to use, EZ or ADV
    print(f"\nWhat is the distance between the 2 ports?")
    print(f'There are two (2) ways to measure this distance\nIf you know the distance in inches, enter "EZ"\nIf you do not know the distance, enter "ADV"')
    option_list = ["ez", "adv"]
    fuzzy_data = {
        "cutoff_value": 0.45,
        "input": f"Mode (EZ/ADV) {syntax} "     
    }
    mode = fuzzy_loop(debug, fuzzy_data, option_list)
    debug_printout(debug, "mode", mode)
    # option_list (ez, adv, etc)

    # This has the two menu options, depending on what the user chose, EZ is first.
    if mode == "ez":
        input_data = {
            "max_value": 240,    # Max length before error
            "min_value": 2.25,   # Min length slack before error
            "input": f"Distance between the (2) points (in inches) {syntax} "
        }
        point_to_point_dist = input_loop(debug, input_data)
        debug_printout(debug, "point_to_point_dist", point_to_point_dist)

    elif mode == "adv":
        # Advanced prep msg :3
        print(f"\nThere are a total of four (4) questions to answer, please answer them as accurately as possible, in the unit requested.")
        print(f"------------------------------------------------------------------------------------------------------------------")

        # The distance between the two devices in U
        print(f"how many U's is the gap from your patch panel to the network device? (in U's) (1U = 1.75 inches)")
        print(f"   (This includes the U of the patch, if the devices are stacked on each-other that is 2U)")
        input_data = {
                "max_value": 64,    # Max length before error
                "min_value": 2,     # Min length slack before error
                "input": f"Height (in rack U) {syntax} "
            }
        u_height = input_loop(debug, input_data)
        debug_printout(debug, "u_height", u_height)

        # The position of the port on the patch panel
        print(f"\nIs the port on your patch panel centered, or is it on the top or bottom of the panel? (top/middle/bottom)")
        option_list = ["bottom", "middle", "top"]
        fuzzy_data = {
            "cutoff_value": 0.45,
            "input": f"Port position (top/middle/bottom) {syntax} "   
        }
        patch_port_position = fuzzy_loop(debug, fuzzy_data, option_list)
        debug_printout(debug, "patch_port_position", patch_port_position)

        # The position of the port on the network device
        print(f"\nIs the port on your network device centered, or is it on the top or bottom of the network device? (top/middle/bottom)")
        option_list = ["bottom", "middle", "top"]
        fuzzy_data = {
            "cutoff_value": 0.45,
            "input": f"Port position (top/middle/bottom) {syntax} "
        }
        device_port_position = fuzzy_loop(debug, fuzzy_data, option_list)
        debug_printout(debug, "device_port_position", device_port_position)

        # Get the left // right distance between the ports
        print(f"\nWhat is the distance between the ports, left to right? please count the distance by counting how many ports apart the switches,\nwether it is left or right doesn't matter")
        input_data = {
                "max_value": 32,    # Max gap before error
                "min_value": 0  ,   # Min gap before error
                "input": f"The gap between the network device and patch panel {syntax} "
            }
        debug_value_printout(debug, input_data)
        port_distance = input_loop(debug, input_data)
        debug_printout(debug, "port_distance", port_distance)
        # grab the final calculation for the adv mode
        point_to_point_dist = distance_math_function(u_height, patch_port_position, device_port_position, port_distance, debug) # Please note that the scaling now exists INSIDE the function

    # Return gathered vars :P
    return min_bend_radius, max_bend_radius, connector_size, slack_cutoff, point_to_point_dist