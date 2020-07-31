#taken from https://stephantul.github.io/trees/2019/07/10/treerec/
import numpy as np

def recursive_compose(tree, embeddings, emb_size):
    """
    Recursively compose a tree.

    If a word is OOV (not in embeddings), we replace it with a zero vector.

    Parameters
    ----------
    tree : list (of list)* of strings
        A tree represented as lists. The terminals are assumed to be strings.
        Example: (("dog", "cat"), "walked")
    embeddings : dict
        A dictionary mapping from words to their word vectors.
    emb_size : int
        The embedding size.

    EXAMPLE
    # Random embeddings
    emb_mtr = np.random.rand(2, 10)
    # Transform them into a dictionary
    embeddings = dict(zip(["dog", "cat"], emb_mtr))
    a = recursive_compose((("dog", "cat"), "walked"), embeddings, 10)
    >>> array([0.18, 0.19, 0.35, 0.34, 0.38, 0.23, 0.31, 0.29, 0.27, 0.2 ])
    # a should be equal to np.mean(emb_mtr, 0) // 2 because "walked" is missing.
    z = np.allclose(a, np.mean(emb_mtr, 0) / 2)
    >>> True


    """
    if not isinstance(tree, (list, tuple)):
        return embeddings.get(tree, np.zeros(emb_size))
    res = []
    for x in tree:
        res.append(recursive_compose(x, embeddings, emb_size))
    return np.mean(res, 0)