"""
Randomly choose and arrange elements
from lists of strings and strings of
characters.
Author: M Young, December 2016. michal@cs.uoregon.edu, github: MichalYoung
"""

import random
from letterbag import LetterBag


def jumbled(word_list, n):
    """
    Create an anagram of n strings randomly chosen
    from word_list.  The jumble is enough to create
    any one of the selected words, but duplicates between
    words are merged (see letterbag).
    Args:
       word_list:  non-empty list of strings
       n: 1 <= n <= len(word_list), number of words
          to jumble together.
    Returns:
       A jumbled string with the property that any of the
       selected strings from word_list can be formed.  The
       result should be the smallest jumble with this property
       (i.e., duplicates between words have been removed).
    """
    selected = random.sample(word_list, n)
    bag = LetterBag("")
    for word in selected:
        bag.merge(LetterBag(word))
    letters = list(bag.as_string())
    print("Letters: {}".format(letters))
    random.shuffle(letters)
    result = "".join(letters)
    return result
