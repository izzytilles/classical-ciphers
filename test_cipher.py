import pytest

from main import convert_to_list, get_choice_encrypt, get_mode_choice
from one_time_pad import one_time_pad_decr, one_time_pad_encr
from caesar import caesar_enc, caesar_dec
from vigenere import vigenere_encr, vigenere_decrypt

# test one time pad

def test_one_time_pad_encr_long_key():
    encr_message = "HI"
    key = "DOG"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

def test_one_time_pad_encr_short_key():
    encr_message = "HI"
    key = "D"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

def test_one_time_pad_decr_long_key():
    decr_message = "HI"
    key = "DOG"

    result = one_time_pad_decr(decr_message, key)

    assert result == None

def test_one_time_pad_decr_short_key():
    decr_message = "HI"
    key = "D"

    result = one_time_pad_decr(decr_message, key)

    assert result == None

def test_one_time_pad_encr_no_key():
    encr_message = "IZZY"
    key = ""

    result = one_time_pad_encr(encr_message, key)

    assert result == None

def test_one_time_pad_encr_no_message():
    encr_message = ""
    key = "HELLO"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

def test_one_time_pad_encr():
    encr_message = "HELLO"
    key = "MEDIA"

    result = one_time_pad_encr(encr_message, key)

    assert result == ["TIOTO", "MEDIA"] # returns a tuple

def test_one_time_pad_encr_lower():
    encr_message = "hello"
    key = "media"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

def test_one_time_pad_decr():
    decr_message = "TIOTO"
    key = "MEDIA"

    result = one_time_pad_decr(decr_message, key)

    assert result == "HELLO"

def test_one_time_pad_decr_lower():
    decr_message = "tioto"
    key = "media"

    result = one_time_pad_decr(decr_message, key)

    assert result == None

# test caesar

def test_caesar_encr():
    encr_message = "A"
    key = "X"

    result = caesar_enc(encr_message, key)

    assert result == "X"

def test_caesar_encr_lower():
    encr_message = "a"
    key = "x"

    result = caesar_enc(encr_message, key)

    assert result == "X"

def test_caesar_decr():
    encr_message = "X"
    key = "A"

    result = caesar_enc(encr_message, key)

    assert result == "X"

def test_caesar_encr_lower():
    encr_message = "x"
    key = "a"

    result = caesar_enc(encr_message, key)

    assert result == None

def test_caesar_encr_long_key():
    encr_message = "X"
    key = "AB"

    result = caesar_enc(encr_message, key)

    assert result == None

def test_caesar_decr_long_key():
    decr_message = "X"
    key = "AB"

    result = caesar_dec(decr_message, key)

    assert result == None

# def test_space_handler():


# test vigenere

def test_vigenere_encr():
    encr_message = "HELLO"
    key = "CAT"

    result = vigenere_encr(encr_message, key)

    assert result == "JEDNO" 

def test_vigenere_encr_lower():
    encr_message = "hello"
    key = "cat"

    result = vigenere_encr(encr_message, key)

    assert result == None 

def test_vigenere_decr():
    decr_message = "JEDNO"
    key = "CAT"

    result = vigenere_decrypt(decr_message, key)

    assert result == "HELLO"

def test_vigenere_decr_lower():
    decr_message = "jedno"
    key = "cat"

    result = vigenere_decrypt(decr_message, key)

    assert result == "HELLO"

def test_vigenere_encr_long_key():
    encr_message = "cat"
    key = "hello"

    result = vigenere_encr(encr_message, key)

    assert result == None 

def test_vigenere_decr_long_key():
    decr_message = "cat"
    key = "hello"

    result = vigenere_decrypt(decr_message, key)

    assert result == None
