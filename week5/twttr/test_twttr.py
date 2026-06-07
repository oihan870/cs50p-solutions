from week5.test_twttr.twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("What's up?") == "Wht's p?"
