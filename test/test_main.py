"""
Test for the Web UI backend functions. The frontend 
doesn't need much testing.
"""

from codes import random_code, random_choices, get_code_from_msg, codes


def test_random_choices():
    """
    Test the random choice generation to ensure duplicates don't exist and
    that the desired response is included. It runs 10,000 times to be VERY
    sure it works :)
    """
    size: int = 4
    for _ in range(10000):
        code: tuple[int, str] = random_code()
        choices = random_choices(code[0], size)
        assert code[1] in choices
        assert len(set(choices)) == size + 1


def test_get_code_from_msg():
    """
    Test the code from message function. This is used to convert a correct
    answer into a code for use with the cat api!
    """
    for code, msg in codes.items():
        assert code == get_code_from_msg(msg)
