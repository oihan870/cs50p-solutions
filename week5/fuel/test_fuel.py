import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("3/2")

    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
