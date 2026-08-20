def debug_loop(debug, valuePrintout, valueText, exception, traceback):
    def debug_loop_basic(valuePrintout, valueText):
        print(f"\n\033[31mDEBUG PRINTOUT, the value of {valueText} is {valuePrintout}\033[32m")
        print(f"Traceback: ERROR{traceback}\n")
        # valuePrintout should be the variable, and valueText should be the variable name ("var_name")

    def debug_loop_adv(exception):
        print(f"\n\033[31mDEBUG PRINTOUT, Exception printout: {exception}\033[32m\n")
        print(f"Traceback: ERROR{traceback}\n")
        # when an exception occurs, the valuePrintout should be (exception as var), so the exception gets printed

    if debug == 0:
        pass # It seems like this should be here just in case but I am unsure why
    if debug == 1:
        debug_loop_basic(valuePrintout, valueText, traceback)
    if debug == 2:
        debug_loop_adv(exception, traceback)
    if debug == 3:
        debug_loop_basic(valuePrintout, valueText, traceback)
        debug_loop_adv(exception, traceback)

# if debug basic then;
# if debug > 0: debug_loop(debug, ) 

# if debug adv, or adv + basic then;
# 
# if debug > 0: debug_loop() 