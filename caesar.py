"""
This is the Caesar Encryption function.
This function is for encrypting the users message using the Caesar cipher.

Input: The user message they would like to encrypt and the character they would like to use as the key.
Output: The encrypted message.
"""
def caesar_enc(message_input, key_input):
#Changing inputs to ascii values
    message = []
    #Handling lower case
    key_input = key_input.upper()
    key = ord(key_input) - ord('A')
    #Encrypting the message
    for i in message_input:
        val = ord(i)
        #Changing the space value
        if val == 32:
            val = 91

        val = ((((val - ord('A')) + key) % 27) + ord('A'))
        if val == ord('['):
            letter = ' '
        else:
            letter = chr(val)
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
    #Handling lower case
    key_input = key_input.upper()
    key = ord(key_input) - ord('A')
    #decrypting
    for i in message_input:
        val = ord(i)
        if val == 32:
            val = 91
        val = ((val - ord('A') - key + 27) % 27) + ord('A')
        if val == ord('['):
            letter = ' '
        else:
            letter = chr(val)
        message.append(letter)
    #Creating return string
    decr = ''.join(message)
    return decr
