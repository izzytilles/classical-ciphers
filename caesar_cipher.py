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