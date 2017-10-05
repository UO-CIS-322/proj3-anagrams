"""
A list of vocabulary words (designed for an ELL class).
"""


class Vocab():
    """
    A list of vocabularly words.
    Can be instantiated with a file or list of strings.
    """

    def __init__(self, wordlist):
        """
        Initialize with the provided word list.
        Args:
           wordlist: a file, path to a file, or a list of strings.
           Words must appear one to a line. Empty lines and lines
           beginning with # are treated as comments.
        Returns: nothing
        Effect: the new Vocab objects contains the strings from wordlist
        Raises:  IOError if if wordlist is a bad path
        """
        self.words = []
        if isinstance(wordlist, str):
            ls = open(wordlist, 'r')
        else:
            ls = wordlist

        for word in ls:
            word = word.strip()
            if len(word) == 0 or word.startswith("#"):
                continue
            self.words.append(word)
        self.words.sort()

    def as_list(self):
        """As list of words"""
        return self.words

    def has(self, word):
        """
        Is word present in vocabulary list?
        Args:
           word: a string
        Reurns: true if word occurs in the vocabularly list
        """
        low = 0
        high = len(self.words) - 1
        while low <= high:
            mid = (low + high) // 2
            probe = self.words[mid]
            if word > probe:
                low = mid + 1
            elif word < probe:
                high = mid - 1
            else:
                return True
        return False
