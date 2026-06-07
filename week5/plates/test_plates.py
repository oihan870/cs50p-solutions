from plates import is_valid


def test_valid_plate():
    assert is_valid("CS50") == True


def test_too_short():
    assert is_valid("C") == False


def test_too_long():
    assert is_valid("CS50000") == False


def test_numbers_middle():
    assert is_valid("CS50P") == False


def test_zero_first_number():
    assert is_valid("CS05") == False


def test_punctuation():
    assert is_valid("PI3.14") == False


def test_starts_with_numbers():
    assert is_valid("50CS") == False

def test_beginning_not_letters():
    assert is_valid("50") == False
    assert is_valid("1ABC") == False

def test_beginning_one_letter_one_number():
    assert is_valid("A1CDE") == False
