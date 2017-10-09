"""
Nose tests for jumble.py

We cannot test for randomness here (no effective oracle),
but we can test that the elements in the returned string
are correct.
"""

from jumble import jumbled

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def same(s, t):
    """
    Same characters (possibly in different order)
    in two strings s and t.
    """
    return sorted(s) == sorted(t)


def test_jumbled_single():
    assert same(jumbled(["abbcd"], 1), "abbcd")


def test_jumbled_pair():
    assert same(jumbled(["abbc", "abcc"], 2), "abbcc")


def test_jumbled_more():
    assert same(jumbled(["aabc", "abac", "bcaa"], 2), "aabc")
