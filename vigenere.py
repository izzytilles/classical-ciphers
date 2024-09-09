
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
    n = 0

    # fail gracefully if the key is longer than the message
    if len(key) > len(message):
        return None
    for k in range(key_length):
        if (ord(key[k]) < 65 and ord(key[k]) != 32) or ord(key[k])> 90:
            return None

    for i in range(length):
        # fail gracefully if the message contains anything other than a capitalized letter or space
        if (ord(message[i]) < 65 and ord(message[i]) != 32) or ord(message[i]) > 90:
            return None
        
        if n >= key_length: #checks to make sure if the key is in bounds since message > key
            n = 0
        char = message[i]
        message_value = space_handler(char)
        key_value = space_handler(key[n]) 
        encrypyt_char = ((message_value + key_value) % 27) + 65 #encryption
        if encrypyt_char == ord('['):
            cipher_text.append(' ') #if its 91 then append a space (acts as 0-27)
            print(message[i]+ " + " + key[n] + " = space")
        else:
            cipher_text.append(chr(encrypyt_char)) # if anything else that's valid append char
            print(message[i] + " + " + key[n] + " = " + chr(encrypyt_char))
        n+=1
    final_encr = "".join(cipher_text) # convert to string and return to main
    return final_encr

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
    length = len(message)
    key_length = len(key)
    n = 0

    if key_length > length:
        return None
    for i in range(length):
        if n >= key_length:
            n = 0
        char = message[i]
        message_val = reverse_space(char) #checks if it is a ] or not and adjusts if it is
        key_value = reverse_space(key[n]) 
        decrypyt_char = ((message_val - key_value) % 27) + 65 #decryption calculations
        if decrypyt_char == ord('['):
            plain_text.append(' ')
            print(message[i]+ " - " + key[n] + " = space")
        else:
            plain_text.append(chr(decrypyt_char))
            print(message[i] + " - " + key[n] + " = " + chr(decrypyt_char))
        n+=1
    final_decr = "".join(plain_text) #converts decryption to string and returns
    return final_decr
