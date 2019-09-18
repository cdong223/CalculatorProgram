def check_total_cholesterol(total_cholesterol):
    if total_cholesterol < 200:
        return "normal"
    elif 200<=total_cholesterol<239:
        return "borderline high"
    else:
        return "high"

def total_cholesterol_interface():
    print("Total cholesterol check")
    chol_input = input("Enter your total cholesterol result (total=x): ")
    chol_data = chol_input.split("=")
    if chol_data[0] == "total":
        result = check_HDL(int(chol_data[1]))
        print("The result is {}".format(result))
    else:
        print("bad input")


def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline low"
    else:
        return "low"

def check_LDL(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result <= 159:
        return "Borderline high"
    elif 160 <= LDL_result <= 189:
        return "High"
    else:
        return "Very high"

def cholesterol_interface():
    print("HDL/LDL check")
    chol_input = input("Enter your cholesterol test result: ")
    chol_data = chol_input.split("=")
    if chol_data[0] in ["HDL","LDL"]:
        if chol_data[0] == "HDL":
            result = check_HDL(int(chol_data[1]))
            print("The result is {}".format(result))
        elif chol_data[0] == "LDL":
            result = check_LDL(int(chol_data[1]))
            print("The result is {}".format(result))
    else:
        print("bad input")

def interface():
        print("My calculator program")
        keep_running = True
        while keep_running:
            print("Option: ")
            print("1 - HDL/LDL Check")
            print("2 - Total Cholesterol Check")
            print("9 - Quit")
            choice = input("Enter your choice: ")
            if choice == '9':
                keep_running = False
            elif choice == '1':
                cholesterol_interface()
            elif choice == '2':
                total_cholesterol_interface()
            else:
                print("bad input")
        return

if __name__ == "__main__":
        interface()
