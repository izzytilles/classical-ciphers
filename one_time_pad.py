# from main import convert_to_list # TODO remove when convert to list becomes an external thing

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

""" 
This is the One Time Pad Encryption Function. 
One Time Pad uses a key that is the same exact length as the message.

Input: the message and key containing only letters and spaces (will fail gracefully is given anything else)
Output: the encrypted message and the key (with some words labeling each)
        If there is an issue, it will output None

"""
def one_time_pad_encr(message, key):
    
    # Frist we make sure that the lengths of the message and key match
    #length = len(message_input)     # We will use this later so it gets its own variable
    #if length != len(key_input):
    #    return None
    
    # We want to make sure the message and key are in capital letters and do not contain special characters
    #message = convert_to_list(message_input)            # This is the version of the message in capital letters
    #if message == None:
    #    return None
    #key = convert_to_list(key_input)                # This is the version of the key in capital letters
    #if key == None:
    #    return None

    encr = []                               # This is the encrypted message that we will output

    # This for loop adds the key letter to the associated letter in the message to encrypt it, and then appends the encrypted letter to the encrypted message 
    for i in range(len(message)):                 
        
        # If the "letter" of the message is a space
        if message[i] == " ":
            letter_encr = (26 + ord(key[i]) - 65) % 27 + 65      # 26 is our decided value for a space, ord() changes the value to be the ASCII number value, we subtract 65 to get the key down to our 0-26 range, we mod by 27 to make sure that the total remains below 27, we add 65 to get it back to the correct ASCII value
            if letter_encr == 91:         # If the letter is supposed to be a space it will be 91 right now, we must correct that
                encr.append(chr(32))    # the character chr() for 32 is a space
            else:                       
                encr.append(chr(letter_encr))    # letterEncr is technically a number that represents a letter, it is not a character until you use chr()
        
        # If the "letter" of the message is actually a letter
        else:
            letter_encr = (( ord(message[i]) - 65 + ord(key[i]) - 65) ) % 27 + 65      # This will subtract the base value A from each letter, add the value of the key in its 0-16 form, and mod 27 to make sure values are between 0 and 26, add 65 to get it back to the ASCII table leter
            if letter_encr == 91:             # If the letter is supposed to be a space it will be 91 right now, we must correct that
                encr.append(chr(32))
            else:
                encr.append(chr(letter_encr))

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
def one_time_pad_decr(encr, key):
    # Change the input encryption message into a list of characters
    #encr = convert_to_list(encr_mess)
    #if encr == None:
    #    return None
    
    # Change the input key into a list of characters. Will capitalize the lower case letters.
    #key = convert_to_list(key_in)
    #if key == None:
    #    return None
    
    # initialize our descryption list
    decr = []
    
    # make sure that the length of the message and the key match
    length = len(encr)
    if length != len(key):
        return None

    # This for loop decrypts the message
    for i in range(len(encr)):                 
        
        # If the "letter" of the encrypted message is a space
        if encr[i] == " ":
            letter_decr = (26 - ord(key[i]) + 65) % 27 + 65      # The space value starts at 26, we subtract the value of the key which is the ord()-65 (double negative makes a positive so we add 65), mod 27 to bring it back to our range of 0-26, then add 65 to bring it back to ASCII
            if letter_decr == 91:         # If the letter is supposed to be a space it will be 91 right now, we must correct that
                decr.append(chr(32))
            else:
                decr.append(chr(letter_decr))        # note: letterDecr is actually the number value of the letter
        
        # If the "letter" of the encrypted message is actually a letter
        elif ord(encr[i]) > 64 and ord(encr[i]) < 91:
            letter_decr = (( ord(encr[i]) - 65 - ord(key[i]) + 65) ) % 27 + 65      # This will subtract the base value A from each letter, subtract the value of the simplified letters together, and mod 27 to get values between 0 and 26, add 65 to get it back to the ASCII table leter
            if letter_decr == 91:             # If the letter is supposed to be a space it will be 91 right now, we must correct that
                decr.append(chr(32))
            else:
                decr.append(chr(letter_decr))
    
    return "".join(decr)    # This is the pretty string version of the decr list 