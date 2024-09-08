from caesar import caesar_enc, caesar_dec
from vigenere import vigenere_encr, vigenere_decrypt
from one_time_pad import one_time_pad_encr, one_time_pad_decr
import csv

""" 
This is the Get mode choice Function. 
This function directs users to the workflow for encrypt or decrypt and takes information in about what cipher is going to
be used.

Input: the mode they would like to use (encrypt or decrypt)
Output: the encrypted or decrypted message
        If there is an issue then the user will be reprompted for correct information and the function will run again

"""
def get_mode_choice(mode_type):
    if mode_type == "E":
        print("Please enter 1 for the caesar cipher, 2 for vigenere, and 3 for one time pad.")
        cipher_type = input()
        encrypted_message = get_choice_encrypt(cipher_type) 
        return encrypted_message
    elif mode_type == "D":
        print("Please enter 1 for the caesar cipher, 2 for vigenere, and 3 for one time pad.")
        cipher_type = input()
        print("Enter the message you would like to decrypt.")
        message_decrypt = input()
        print("Enter the key")
        key_decrypt = input()
        decrypt_message = get_choice_decrypt(cipher_type, message_decrypt, key_decrypt)
        return decrypt_message
    else:
        print("Please write a valid input E or D.")
        mode_type= input()
        get_mode_choice(mode_type)

#TODO ciphertexts need to be saved to a FILE as well
""" 
This is the Get mode choice encrypt function. 
This function directs users to the workflow for the cipher that they want to use and takes in the necessary
input.

Input: the cipher they would like to use 
Output: the encrypted message is returned to get mode choice
    
"""
def get_choice_encrypt(cipher_type):
    file_name = "ciphers.csv"
    if cipher_type == "1":
        print("Enter the message you would like to encrypt.")
        message_input = input()
        print("Enter letter you would like to use for key.")
        letter = input()
        caesar_string = caesar_enc(message_input, letter)
        load_table(file_name, message_input, letter, caesar_string)
        return caesar_string
    elif cipher_type == "2":
        print("Enter the message you would like to encrypt.")
        message_input = input()
        print("Enter the key you want to use")
        vigenere_key = input()
        vigenere_message= vigenere_encr(message_input, vigenere_key)
        load_table(file_name, message_input, vigenere_key,vigenere_message)
        return vigenere_message
    elif cipher_type == "3":
        print("Enter the message you would like to encrypt.")
        message_input = input()
        print("Enter the key you want to use")
        one_pad_key = input()
        one_pad_string = one_time_pad_encr(message_input, one_pad_key) 
        load_table(file_name, message_input, one_pad_key, one_pad_string)
        return one_pad_string
    else:
        print("Please write a valid input, 1, 2 or 3.")
        cipher_type = input()
        get_choice_encrypt()

""" 
This is the Get choice decrypt function. 
This function directs users to the workflow for the cipher that they want to use and takes in the necessary
input.

Input: the cipher, message to decrypt and the key that will be used 
Output: the encrypted message is returned to get mode choice
    
"""
def get_choice_decrypt(cipher_type, message_decrypt, key_decrypt):
    file_name = "ciphers.csv"
    if cipher_type == "1":
        caesar_string = caesar_dec(message_decrypt, key_decrypt)
        load_table(file_name, message_decrypt, key_decrypt, caesar_string)
        return caesar_string
    elif cipher_type == "2":
        vigenere_string = vigenere_decrypt(message_decrypt, key_decrypt)
        load_table(file_name, message_decrypt, key_decrypt, vigenere_string)
        return vigenere_string
    elif cipher_type == "3":
        one_pad_string = one_time_pad_decr(message_decrypt, key_decrypt) 
        load_table(file_name, message_decrypt, key_decrypt, one_pad_string)
        return one_pad_string
    else:
        print("Please write a valid input, 1, 2 or 3.")
        cipher_type = input()
        get_choice_encrypt()

"""
Converts a string to a list
Input: a string
Output: the list of capitalized characters
        If the input has an unacceptable character, it will return None
"""
def convert_to_list(string):
    message = []
    for k in range(len(string)):
        if string[k] == " ":                                             # If the message is a space
            message.append(" ")
        elif ord(string[k]) > 96 and ord(string[k]) < 123:         # If the message is lower case 
            message.append(string[k].upper())
        elif ord(string[k]) > 64 and ord(string[k]) < 91:         # If the message is in upper case
            message.append(string[k])
        else:
            return None
    return message

def load_table(file_name, message, key, result):
    data = [message, key, result]

    # Specify the file path where you want to export the CSV file

    # Write data to CSV file
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    print(f'CSV file exported successfully to {file_name}')
    

if __name__ == "__main__":
    print("Welcome to our encryption and decryption program! Enter E to encryt and D to decrypt.")
    mode_type = input()
    secret_message = get_mode_choice(mode_type)
    print(secret_message)



