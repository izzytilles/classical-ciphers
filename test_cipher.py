import pytest

from Group1_CPSC353_CipherCode import oneTimePadDecr, oneTimePadEncr

def test_one_time_pad_decr():
    encr_message = "HELLO"
    key = "MEDIA"

    oneTimePadEncr(encr_message, key)
