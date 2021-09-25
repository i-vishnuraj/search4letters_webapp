def search4letter(phrase: str, letters: str='aeiou') -> str:
    """ Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

