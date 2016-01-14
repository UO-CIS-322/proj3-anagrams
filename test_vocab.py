"""
Nose tests for vocab.py
"""

from vocab import Vocab

def test_empty_vocab():
    """
    Nothing is present in an empty word list
    """
    vocab = Vocab( [ ] )
    assert vocab.as_list() == [ ]
    assert not vocab.has("sheep")

def test_single_vocab():
    vocab = Vocab([ "moe" ])
    assert vocab.as_list() == [ "moe" ]
    assert vocab.has("moe")
    assert not vocab.has("meeny")

def test_small_vocab():
    l = ["eeny", "moe", "miney", "meeny"];
    vocab = Vocab(l)
    assert vocab.has("moe")
    assert vocab.has("eeny")
    assert vocab.has("miney")
    assert vocab.has("meeny")
    assert not vocab.has("many")
    assert sorted(vocab.as_list()) == sorted(l)

def test_from_simulated_file():
    from io import StringIO
    l = StringIO(initial_value="""
        #comment
        # another comment line
        sheep
        rats
        #comment
        squirrels
        """)
    vocab = Vocab(l)
    assert sorted(vocab.as_list()) == ["rats", "sheep", "squirrels"]
    assert vocab.has("sheep")
    assert vocab.has("rats")
    assert vocab.has("squirrels")
    assert not vocab.has("#comment")
