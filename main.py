# Adrienn Komlodi
program_continues = True

def pass_encoder(password):
    encoded_pass = ""
    pass_list = list(password)
    for char in pass_list:
        new_pass_digit = int(char) + 3
        new_pass_digit = str(new_pass_digit)
        encoded_pass += new_pass_digit
    return encoded_pass


if __name__ == "__main__":
    while program_continues:
        # print menu
        print("Menu\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        if option == 0:
            program_continues = False
        # encode option
        elif option == 1:
            pass_entry = input("Please enter your password to encode: ")
            encoded_pass_entry = pass_encoder(pass_entry)
            print(encoded_pass_entry)
            print("Your password has been encoded and stored!")
        # decode option
        