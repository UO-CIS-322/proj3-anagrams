"""
Bag of letters (structure for anagram creation and solving).
Author: M Young, December 2016.  michal@cs.uoregon.edu, Github: MichalYoung

"""


class LetterBag():
    """
    Bag of letters structure for anagrams

    A letterbag is a bag (in the mathematical sense) of characters
    that might be used to form a word.  It's a bag and not a set
    because 'llax' can be used to make the word 'all' but 'lmax' cannot.

    """
    # Instance variables
    letters = None  # See value created in __init__

    def __init__(self, word):
        """
        Create the letterbag with exactly the letters to create word.
        Args:
           word: a string whose characters should be in the LetterBag
        Returns: nothing  (modifies 'self')
        Effect: this LetterBag is the bag of letters exactly sufficient
            to form word.
        """
        self.letters = dict()
        for letter in word:
            count = self.letters.get(letter, 0)
            self.letters[letter] = count + 1
        return

    def merge(self, other):
        """
        Augment this LetterBag so that it contains other.
        For example, merge of letterbags for 'aab' and 'abb'
        is 'aabb'.
        Args:
            other: another LetterBag to merge into self
        Returns: None
        Effects: this LetterBag is augmented as necessary
        """
        allkeys = list(self.letters.keys()) + list(other.letters.keys())
        for letter in allkeys:
            self.letters[letter] = max(self.letters.get(letter, 0),
                                       other.letters.get(letter, 0))
        return

    def contains(self, other):
        """
        Self contains other.
        Args:
           other: LetterBag or string.
        Returns:
           True iff the LetterBag representation of other is contained
           in (that is, has equal or smaller letter count for each letter)
           the letter count of self.
        Examples:
           LetterBag("abbc").contains(LetterBag("abc")) == True
           LetterBag("abbc").contains("abc") == True
           LetterBag("abbc").contains(LetterBag("abbc")) == True
           LetterBag("abc").contains(LetterBag("abbc")) == False
        """
        if isinstance(other, str):
            other = LetterBag(other)
        for letter in other.letters.keys():
            if other.letters.get(letter) > self.letters.get(letter, 0):
                return False
        return True

    def as_string(self):
        """
        Canonical string representation is sorted sequence of letters.
        (Useful in testing.)
        """
        return "".join(sorted([n * letter
                               for letter, n in self.letters.items()]))

    def __str__(self):
        """
        Printed representation is the canonical string representation.
        """
        return self.as_string()

    def __repr__(self):
        """
        Representation looks like constructor.
        """
        return 'LetterBag("{}")'.format(str(self))
