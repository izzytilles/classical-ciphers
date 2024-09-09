"""
This is the Caesar Encryption function.
This function is for encrypting the users message using the Caesar cipher.

Input: The user message they would like to encrypt and the character they would like to use as the key.
Output: The encrypted message.
"""
def caesar_enc(message_input, key_input):
#Initializing message list
    message = []
    #Handling lowercase and incorrect key cases
    if len(key_input) > 1:
        return None
    key_input = key_input.upper()
    #getting ascii for the key
    key = ord(key_input) - ord('A')
    for i in message_input:
        val = ord(i)
        #Changing the space value
        if val == 32:
            val = 91
        #Checking for special characters
        elif val < 65 or val > 90:
            return None
        print(i, " + ", key_input, " % 27 = ", end="")
        #Encrypting the message
        val = ((((val - ord('A')) + key) % 27) + ord('A'))
        #Handlig the spaces
        if val == ord('['):
            letter = ' '
            print(i + " + " + key_input + " = space")
        else:
            letter = chr(val)
        print(letter)
        message.append(letter)
    #Making string
    encr = ''.join(message)
    #print(encr)
    return encr

"""
This is the Caesar Decryption function.
This function is for decrypting the users message using the Caesar cipher.

Input: The user message they would like to decrypt and the character they used as the key.
Output: The decrypted message.
"""
def caesar_dec(message_input, key_input):
    message = []
    #Handling lowercase and incorrect key cases
    if len(key_input) > 1:
        return None
    key_input = key_input.upper()
    #Changing key into ascii
    key = ord(key_input) - ord('A')
    for i in message_input:
        val = ord(i)
        #Handling spaces
        if val == 32:
            val = 91
        #Handling special characters
        elif val < 65 or val > 90:
            return None
        print(i, " - ", key_input, " % 27 = ", end="")
        #Decrypting message
        val = ((val - ord('A') - key + 27) % 27) + ord('A')
        #Handling space cases
        if val == ord('['):
            letter = ' '
            print(i + " - " + key_input + " = space")
        else:
            letter = chr(val)
            print(i + " - " + key_input + " = " + chr(val))
        message.append(letter)
        print(letter)
    #Creating return string
    decr = ''.join(message)
    return decr
