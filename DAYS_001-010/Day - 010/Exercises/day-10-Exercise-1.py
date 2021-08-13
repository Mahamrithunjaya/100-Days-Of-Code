# Function with Outputs

def name_format(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You Didn't entered a Valid Input. "
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"Result: {formatted_f_name} {formatted_l_name}"


output = name_format(input("What is your first name? "), input("What is your last name? "))
print(output)
