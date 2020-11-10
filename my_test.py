from my_code import add_n


def test_inc():
    assert 3 == add_n(2)
    assert 15 == add_n(5)
    assert 21 == add_n(6)
