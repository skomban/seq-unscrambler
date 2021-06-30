import itertools
import os
import random
from collections import defaultdict

from nltk import tokenize

RESOURCE_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'resources'))


def get_vocab() -> list:
    """Load vocabulary from file.

    Returns:
        vocab: list
    """

    vocab = []
    with open(os.path.join(RESOURCE_DIR, "vocabulary.txt")) as f:
        for line in f:
            word = line.strip().lower()
            vocab.append(word)

    return vocab


def create_chars_to_words_map(vocab: list) -> defaultdict:
    """Create a map using sorted word chars as key and corresponding words as values

    Args:
         vocab: list

    Returns:
        charset_to_words_map: defaultdict
    """

    chars_to_words_map = defaultdict(list)
    for word in vocab:
        word = word.lower()
        charset_key = ''.join(sorted(word))
        chars_to_words_map[charset_key].append(word)

    return chars_to_words_map


def get_words_from_chars(chars: str, chars_to_words_map: defaultdict) -> list:
    """Find words in the map using sorted chars

    Args:
        chars: str
        chars_to_words_map: defaultdict

    Returns:
         words: list
    """

    chars = chars.lower()
    words = chars_to_words_map.get(''.join(sorted(chars)), chars)

    if isinstance(words, str):
        return [words]

    return words


def get_permutations(sentence: str, chars_to_words_map: defaultdict) -> list:
    """Create sentences using word permutations

    Args:
        sentence: str
        chars_to_words_map: defaultdict

    Returns:
         words: list
    """

    token_perm = []
    for token in tokenize.word_tokenize(sentence):
        if len(token) > 1:
            token_perm.append(get_words_from_chars(token, chars_to_words_map))
        else:
            token_perm.append([token])

    return list(itertools.product(*token_perm))


def scramble_words(sentence):
    """Shuffle characters in a word sequence

    Args:
        sentence: str

    Returns:
         scrambled_tokens: list
    """

    tokens = tokenize.word_tokenize(sentence)
    scrambled_tokens = []
    for token in tokens:
        if len(token) > 1:
            chars = list(token)
            random.shuffle(chars)
            token = ''.join(chars)
        scrambled_tokens.append(token)

    return ' '.join(scrambled_tokens)
