import pytest

from Group1_CPSC353_CipherCode import one_time_pad_decr, one_time_pad_encr, convertToList, get_choice_encrypt, get_mode_choice, vigenere_encr, caesar_enc

def test_one_time_pad_decr_wrong_key():
    encr_message = "HI"
    key = "DOG"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

def test_one_time_pad_decr_no_key():
    encr_message = "IZZY"
    key = ""

    result = one_time_pad_encr(encr_message, key)

    assert result == None

def test_one_time_pad_decr_no_message():
    encr_message = ""
    key = "HELLO"

    result = one_time_pad_encr(encr_message, key)

    assert result == None

def test_one_time_pad_encr():
    encr_message = "HELLO"
    key = "MEDIA"

    result = one_time_pad_encr(encr_message, key)

    assert result == ["TIOTO", "MEDIA"] # returns a tuple

def test_one_time_pad_decr():
    decr_message = "TIOTO"
    key = "MEDIA"

    result = one_time_pad_decr(decr_message, key)

    assert result == "HELLO"

def test_caesar_enc():
    encr_message = "THIS IS SECRET"
    key = "X"

    result = caesar_enc(encr_message, key)

    assert result == "QEFPWFPWPBZOBQ"

# def test_space_handler():

def test_vignere_encr():
    encr_message = "HELLO"
    key = "CAT"

    result = vigenere_encr(encr_message, key)

    assert result == "HSDEK" # dummy 5-letter value until we actually encrypt HELLO using CAT

#def