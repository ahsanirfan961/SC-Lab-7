import pytest
from string_permutations import generate_permutations  # replace with the actual module name

def test_empty_string():
    """
    Test that an empty string returns an empty list.
    """
    assert generate_permutations("") == []

def test_single_character():
    """
    Test that a single character string returns a list with the string itself.
    """
    assert generate_permutations("a") == ["a"]

def test_two_characters():
    """
    Test that a two-character string returns two permutations.
    """
    result = generate_permutations("ab")
    assert sorted(result) == sorted(["ab", "ba"])

def test_three_characters():
    """
    Test that a three-character string returns six permutations.
    """
    result = generate_permutations("abc")
    assert sorted(result) == sorted(["abc", "acb", "bac", "bca", "cab", "cba"])

def test_large_input():
    """
    Test a slightly larger string to ensure the function does not crash.
    """
    result = generate_permutations("abcd")
    assert len(result) == 24  # 4! = 24

def test_non_alphabetic_characters():
    """
    Test that the function works with non-alphabetic characters.
    """
    result = generate_permutations("1a!")
    assert sorted(result) == sorted(["1a!", "1!a", "a1!", "a!1", "!1a", "!a1"])

@pytest.mark.parametrize("input_str, expected_length", [
    ("abc", 6),  # 3! permutations
    ("abcd", 24),  # 4! permutations
    ("abcde", 120)  # 5! permutations
])
def test_permutations_length(input_str, expected_length):
    """
    Parametrized test to check if the number of permutations matches n!.
    """
    result = generate_permutations(input_str)
    assert len(result) == expected_length

