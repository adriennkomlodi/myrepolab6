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


def pass_decoder(encoded_pass):
    pass


if __name__ == "__main__":
    encoded_pass_entry = ""
    while program_continues:
        # print menu
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        # encode option
        if option == 1:
            pass_entry = input("Please enter your password to encode: ")
            encoded_pass_entry = pass_encoder(pass_entry)
            print("Your password has been encoded and stored!")
        # decode option
        elif option == 2:
            print(f"The encoded password is {encoded_pass_entry}, and the original password is {pass_decoder(encoded_pass_entry)}")
            pass
        elif option == 3:
            program_continues = False
