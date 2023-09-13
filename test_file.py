from file import square


def test_square_positive_number():
    assert square(4) == 16
    assert square(7) == 49


def test_square_negative_number():
    assert square(-3) == 9
    assert square(-5) == 25


def test_square_zero():
    assert square(0) == 0


if __name__ == "__main__":
    import pytest
    pytest.main()
