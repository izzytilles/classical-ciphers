
def caesar_enc(message_input, key_input):
#Changing inputs to ascii values
    message = []
    key = ord(key_input) - ord('A')
    #Encrypting the message
    for i in message_input:
        val = ord(i)
        #Changing the space value
        if val == 32:
            val = 91
            #Ecrypting the space value
            val = ((((val - ord('A')) + key) % 26) + ord('A')) - 1
            if val == 64:
                val = 91
        else:
            #Ecrypting letters
            val = ((((val - ord('A')) + key) % 26) + ord('A'))
        #Converting 91 to be space
        if val == 91:
            letter = ' '
        else:
            letter = chr(val)
        message.append(letter)
    #Making string
    encr = ''.join(message)
    #print(encr)
    return encr
#Deciphering caesar runs but isnt quite correct yet
def caesar_dec(message_input, key_input):
    message = []
    key = ord(key_input) - ord('A')
    for i in message_input:
        val = ord(i)
        if val == 32:
            val = 91
            val = ((((val - ord('A')) - key) + 26) + ord('A')) - 1
            if val == 64:
                val == 91
        else:
                val = ((((val - ord('A')) - key) + 26) + ord('A'))

        if val == 91:
            letter = ' '
        else:
            letter = chr(val)
        message.append(letter)
    decr = ''.join(message)
    print(decr)
    return decr

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
    if cipher_type == "1":
        print("Enter the message you would like to encrypt.")
        message_input = input()
        print("Enter letter you would like to use for key.")
        letter = input()
        caesar_string = caesar_enc(message_input, letter)
        return caesar_string
    elif cipher_type == "2":
        print("Enter the message you would like to encrypt.")
        message_input = input()
        print("Enter the key you want to use")
        vigenere_key = input()
        vigenere_message= vigenere_encr(message_input, vigenere_key)
        return vigenere_message
    elif cipher_type == "3":
        print("Enter the message you would like to encrypt.")
        message_input = input()
        print("Enter the key you want to use")
        one_pad_key = input()
        one_pad_string = one_time_pad_encr(message_input, one_pad_key) 
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
    if cipher_type == "1":
        caesar_string = caesar_dec(message_decrypt, key_decrypt)
        return caesar_string
    elif cipher_type == "2":
        vigenere_string = vigenere_decrypt(message_decrypt, key_decrypt)
        return vigenere_string
        return "two works" + cipher_type
    elif cipher_type == "3":
        one_pad_string = one_time_pad_encr(message_decrypt, key_decrypt) 
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
def convertToList(string):
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

""" 
This is the space handler function. 
This function handles the alphabet that is provided and takes care of spaces.

Input: a char
Output: the asci value of the char input
    
"""
def space_handler(char):
    if (char == ' '):
        return 26    
    else:
        return ord(char) - ord('A')

""" 
This is the vigenere encrypt function. 
This function takes in a message and a key and encrypts the message.

Input: message and key
Output: the encrypted message 
    
"""
def vigenere_encr(message, key):
    cipher_text = []
    length = len(message)
    key_length = len(key)
    message = convertToList(message)
    key = convertToList(key)
    n = 0

    for i in range(length):
        if n >= key_length:
            n = 0
        char = message[i]
        message_value = space_handler(char)
        key_value = space_handler(key[n]) 
        encrypyt_char = ((message_value + key_value) % 27) + 65
        cipher_text.append(chr(encrypyt_char))
        n+=1
    return cipher_text

""" 
This is the reverse space function. 
This function takes in character and handles the ascii value that is generated by spaces.

Input: character
Output: the number ascii value
    
"""
def reverse_space(char):
    if (char == '['):
        return 91    
    else:
        return ord(char) - ord('A')

""" 
This is the vigenere decrypt function. 
This function takes in a message and a key and decrypts the message.

Input: message and key
Output: the decrypted message in a list form 
    
"""
def vigenere_decrypt(message, key):
    plain_text = []
    message = convertToList(message)
    key = convertToList(key)
    length = len(message)
    key_length = len(key)
    n = 0

    for i in range(length):
        if n >= key_length:
            n = 0
        char = message[i]
        message_val = reverse_space(char) #need to figure out how to deal with spaces
        key_value = reverse_space(key[n])
        decrypyt_char = ((message_val - key_value) % 27) + 65
        plain_text.append(chr(decrypyt_char))
        n+=1
    return plain_text

""" 
This is the One Time Pad Encryption Function. 
One Time Pad uses a key that is the same exact length as the message.

Input: the message and key containing only letters and spaces (will fail gracefully is given anything else)
Output: the encrypted message and the key (with some words labeling each)
        If there is an issue, it will output None

"""
def one_time_pad_encr(message_input, key_input):
    
    # Frist we make sure that the lengths of the message and key match
    length = len(message_input)     # We will use this later so it gets its own variable
    if length != len(key_input):
        return None
    
    # We want to make sure the message and key are in capital letters and do not contain special characters
    message = convertToList(message_input)            # This is the version of the message in capital letters
    if message == None:
        return None
    key = convertToList(key_input)                # This is the version of the key in capital letters
    if key == None:
        return None

    encr = []                               # This is the encrypted message that we will output

    # This for loop adds the key letter to the associated letter in the message to encrypt it, and then appends the encrypted letter to the encrypted message 
    for i in range(length):                 
        
        # If the "letter" of the message is a space
        if message[i] == " ":
            letterEncr = (26 + ord(key[i]) - 65) % 27 + 65      # 26 is our decided value for a space, ord() changes the value to be the ASCII number value, we subtract 65 to get the key down to our 0-26 range, we mod by 27 to make sure that the total remains below 27, we add 65 to get it back to the correct ASCII value
            if letterEncr == 91:         # If the letter is supposed to be a space it will be 91 right now, we must correct that
                encr.append(chr(32))    # the character chr() for 32 is a space
            else:                       
                encr.append(chr(letterEncr))    # letterEncr is technically a number that represents a letter, it is not a character until you use chr()
        
        # If the "letter" of the message is actually a letter
        else:
            letterEncr = (( ord(message[i]) - 65 + ord(key[i]) - 65) ) % 27 + 65      # This will subtract the base value A from each letter, add the value of the key in its 0-16 form, and mod 27 to make sure values are between 0 and 26, add 65 to get it back to the ASCII table leter
            if letterEncr == 91:             # If the letter is supposed to be a space it will be 91 right now, we must correct that
                encr.append(chr(32))
            else:
                encr.append(chr(letterEncr))

    # This prettifies the lists back into a string so it is easy to read and can be copied and pasted for decryption
    final_encrypt = "".join(encr)
    final_key = "".join(key)

    return  [final_encrypt, final_key]


""" 
This is the One Time Pad Decryption Function. 
One Time Pad uses a key that is the same exact length as the message.

Input: the encrypted message and key containing only letters and spaces (will fail gracefully is given anything else)
Output: the decrypted message
        If there is an issue it will return None

"""
def one_time_pad_decr(encr_mess, key_in):
    # Change the input encryption message into a list of characters
    encr = convertToList(encr_mess)
    if encr == None:
        return None
    
    # Change the input key into a list of characters. Will capitalize the lower case letters.
    key = convertToList(key_in)
    if key == None:
        return None
    
    # initialize our descryption list
    decr = []
    
    # make sure that the length of the message and the key match
    length = len(encr_mess)
    if length != len(key_in):
        return None

    # This for loop decrypts the message
    for i in range(length):                 
        
        # If the "letter" of the encrypted message is a space
        if encr[i] == " ":
            letterDecr = (26 - ord(key[i]) + 65) % 27 + 65      # The space value starts at 26, we subtract the value of the key which is the ord()-65 (double negative makes a positive so we add 65), mod 27 to bring it back to our range of 0-26, then add 65 to bring it back to ASCII
            if letterDecr == 91:         # If the letter is supposed to be a space it will be 91 right now, we must correct that
                decr.append(chr(32))
            else:
                decr.append(chr(letterDecr))        # note: letterDecr is actually the number value of the letter
        
        # If the "letter" of the encrypted message is actually a letter
        elif ord(encr[i]) > 64 and ord(encr[i]) < 91:
            letterDecr = (( ord(encr[i]) - 65 - ord(key[i]) + 65) ) % 27 + 65      # This will subtract the base value A from each letter, subtract the value of the simplified letters together, and mod 27 to get values between 0 and 26, add 65 to get it back to the ASCII table leter
            if letterDecr == 91:             # If the letter is supposed to be a space it will be 91 right now, we must correct that
                decr.append(chr(32))
            else:
                decr.append(chr(letterDecr))
    
    return "".join(decr)    # This is the pretty string version of the decr list 



#TODO needs to be put back in to run program framework

print("Welcome to our encryption and decryption program! Enter E to encryt and D to decrypt.")
mode_type = input()
secret_message = get_mode_choice(mode_type)
print(secret_message)


"""
# My personal testing. Feel free to delete or change. 
message = input("Write message: ")
key = input("Write key of the same length as the message: ")
print(one_time_pad_encr(message, key))

decryption = input("Encrypted Message: ")
key = input("Key: ")
print("The message is: " + one_time_pad_decr(decryption, key))\
"""

