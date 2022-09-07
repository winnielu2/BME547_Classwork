def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Total Cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_driver()

def input_HDL():
    inp = input("Enter HDL value:")
    return int(inp)

def input_LDL():
    inp = input("Enter LDL value: ")
    return int(inp)

def input_total():
    inp = input("Enter total cholesterol value: ")
    return int(inp)

def check_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif HDL < 40:
        return "Low"
    else:
        return "Borderline Low"

def check_LDL(LDL):
    if LDL < 130:
        return "Normal"
    elif 130 <= LDL <= 159:
        return "Borderline High"
    elif 160 <= LDL <= 189:
        return "High"
    else:
        return "Very High" 

def check_total(total):
    if total < 200:
        return "Normal"
    elif 200 <= total <=239:
        return "Borderline High"
    else:
        return "High"

def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)

def LDL_driver():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)

def total_driver():
    total_value = input_total()
    answer = check_total(total_value)
    output_total_result(total_value, answer)

def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value of {} is {}".format(hdl_value, charac))

def output_LDL_result(ldl_value, charac):
    print("The results for an LDL value of {} is {}".format(ldl_value, charac))

def output_total_result(total_value, charac):
    print("The results for a total cholesterol value of {} is {}".format(total_value, charac))

interface()