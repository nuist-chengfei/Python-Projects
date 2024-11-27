import random
import string

# Generates the password
def gen_pass(length, numbers=True, special_char=True):
    alphabets = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    if numbers:
        alphabets += digits
    if special_char:
        alphabets += special
    
    pwd = ""
    criteria = False
    has_num = False
    has_special = False
    
    while not criteria or len(pwd) < length:
        new_char = random.choice(alphabets)
        pwd += new_char
        
        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_special = True
        
        criteria = True
        if numbers:
            criteria = has_num
        if special_char:
            criteria = criteria and has_special
    
    return pwd

# Here, bau means Business As Usual. Just a shortcut for me Because I am lazy...
# Checking is the inputs are correct and If I'm generating the password or not.
def validating(length_input):
    try:
        if ' ' in length_input:
            length, additional = length_input.split(' ')
            length = int(length)
            if additional == "bau":
                return length, True, True, True
        else:
            length = int(length_input)
        return length, False, True, True
    except ValueError:
        print("Follow the instructions and give correct input.")
        return None

# validate yes/no inputs
def validating_y_n(prompt):
    user_input = input(prompt).lower()
    if user_input in ['y', 'n']:
        return user_input == 'y'
    else:
        print("Follow the instructions and give correct input.")
        return validating_y_n(prompt)

# Main Function Calling
length_input = input("Enter the length: ")
length_result = validating(length_input)

if length_result:
    length, bypass_other_inputs, has_num, has_special = length_result
    if not bypass_other_inputs:
        has_num = validating_y_n("Do you want to have numbers? (y/n)\n-> ")
        has_special = validating_y_n("Do you want to have special characters? (y/n)\n-> ")
    
    pwd = gen_pass(length, has_num, has_special)
    print("The generated password is:", pwd)
