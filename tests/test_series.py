import pytest

from math_series.series import fibonacci, lucas, sum_series

# Fibonacci


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_negative():
    actual = fibonacci(-1)
    expected = "Invalid Input"
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

# Lucas


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_negative():
    actual = lucas(-2)
    expected = "Invalid Input"
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_ten():
    actual = lucas(10)
    expected = 123
    assert actual == expected

# sum_series


def test_sum_series_zero_no_optionals():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_zero_with_optionals():
    actual = sum_series(0, 7, 3)
    expected = 7
    assert actual == expected


def test_sum_series_five_no_optionals():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_sum_series_five_optionals():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected


def test_sum_series_negative():
    actual = sum_series(-3)
    expected = "Invalid Input"
    assert actual == expected


def test_sum_series_negative_optionals():
    actual = sum_series(-3, 5, 10)
    expected = "Invalid Input"
    assert actual == expected


def test_sum_series_five_with_negative_optionals():
    actual = sum_series(5, -5, -3)
    expected = -30
    assert actual == expected
