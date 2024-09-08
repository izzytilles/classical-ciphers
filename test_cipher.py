import pytest

from main import convert_to_list, get_choice_encrypt, get_mode_choice
from one_time_pad import one_time_pad_decr, one_time_pad_encr
from caesar import caesar_enc, caesar_dec
from vigenere import vigenere_encr, vigenere_decrypt

# test to ensure that a key that is too long will not be allowed for one time pad encryption
def test_one_time_pad_encr_long_key():
    encr_message = "HI"
    key = "DOG"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

# test to ensure that a key that is too short will not be allowed for one time pad encryption
def test_one_time_pad_encr_short_key():
    encr_message = "HI"
    key = "D"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

# test to ensure that a key that is too long will not be allowed for one time pad decyrption
def test_one_time_pad_decr_long_key():
    decr_message = "HI"
    key = "DOG"

    result = one_time_pad_decr(decr_message, key)

    assert result == None

# test to ensure that a key that is too short will not be allowed for one time pad decryption
def test_one_time_pad_decr_short_key():
    decr_message = "HI"
    key = "D"

    result = one_time_pad_decr(decr_message, key)

    assert result == None

# test to ensure that an attempt with no key will not be allowed for one time pad encyption
def test_one_time_pad_encr_no_key():
    encr_message = "IZZY"
    key = ""

    result = one_time_pad_encr(encr_message, key)

    assert result == None

# test to ensure that an attempt with no message will not be allowed for one time pad encyption
def test_one_time_pad_encr_no_message():
    encr_message = ""
    key = "HELLO"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

# test to ensure that one time pad encryption works
def test_one_time_pad_encr():
    encr_message = "HELLO"
    key = "MEDIA"

    result = one_time_pad_encr(encr_message, key)

    assert result == ["TIOTO", "MEDIA"] # returns a tuple

# test to ensure that one time pad encyption will not run with lower case input
def test_one_time_pad_encr_lower():
    encr_message = "hello"
    key = "media"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

# test to ensure that one time pad decryption works
def test_one_time_pad_decr():
    decr_message = "TIOTO"
    key = "MEDIA"

    result = one_time_pad_decr(decr_message, key)

    assert result == "HELLO"

# test to ensure that one time pad decryption will not run with lower case input
def test_one_time_pad_decr_lower():
    decr_message = "tioto"
    key = "media"

    result = one_time_pad_decr(convert_to_list(decr_message), key)

    assert result == None

# test to ensure that caesar encryption works
def test_caesar_encr():
    encr_message = "AWAY WE GO"
    key = "X"

    result = caesar_enc(encr_message, key)

    assert result == "XSXUWSAWCK"

# test to ensure that caesar encryption will not work with lowercase input 
def test_caesar_encr_lower():
    encr_message = "away we go"
    key = "x"

    result = caesar_enc(encr_message, key)

    assert result == None

# test to ensure that caesar decryption works
def test_caesar_decr():
    encr_message = "XSXUWSAWCK"
    key = "X"

    result = caesar_dec(encr_message, key)

    assert result == "AWAY WE GO"

# test to ensure that caesar decryption does not work with lowercase input
def test_caesar_dec_lower():
    encr_message = "xsxuwsawck"
    key = "a"

    result = caesar_dec(encr_message, key)

    assert result == None

# test to ensure that caesar encryption doesn't work with a key that's longer that one character
def test_caesar_encr_long_key():
    encr_message = "HELLO"
    key = "AB"

    result = caesar_enc(encr_message, key)

    assert result == None

# test to ensure that caesar decryption doesn't work with a key that's longer that one character
def test_caesar_decr_long_key():
    decr_message = "HELLO"
    key = "AB"

    result = caesar_dec(decr_message, key)

    assert result == None

# test to ensure that vigenere encryption works
def test_vigenere_encr():
    encr_message = "HELLO"
    key = "CAT"

    result = vigenere_encr(encr_message, key)

    assert result == "JEDNO" 

# test to ensure that vigenere encryption doesn't work with lowercase input
def test_vigenere_encr_lower():
    encr_message = "hello"
    key = "cat"

    result = vigenere_encr(encr_message, key)

    assert result == None

# test to ensure that vigenere decryption works
def test_vigenere_decr():
    decr_message = "JEDNO"
    key = "CAT"

    result = vigenere_decrypt(decr_message, key)

    assert result == "HELLO"

# test to ensure that vigenere encryption doesn't work if the key is longer than the word to be encrypted
def test_vigenere_encr_long_key():
    encr_message = "cat"
    key = "hello"

    result = vigenere_encr(encr_message, key)

    assert result == None 

# test to ensure that vigenere decryption doesn't work if the key is longer than the word to be decrypted
def test_vigenere_decr_long_key():
    decr_message = "cat"
    key = "hello"

    result = vigenere_decrypt(decr_message, key)

    assert result == None
