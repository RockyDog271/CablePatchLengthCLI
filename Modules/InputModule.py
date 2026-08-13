def input_loop(debug):
    
    while True:
        try:
           minBendRadius = round(minBendRadius, 2)
           if Debug: print(f"Debug message: {minBendRadius}")
           break 
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            print(f"   (Examples are; 0, 0.0, 0.00)")

# START \033[34m AND \033[32m
# END \033[0m