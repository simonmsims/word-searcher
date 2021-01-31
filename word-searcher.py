import sys


def word_searcher():
    args = _parse_arguments()
    pass


def _parse_arguments():
    if len(sys.argv) == 1:
        print("Input parameters are missing...")
        return []

    return dict(
        word_length='1',
    )


word_searcher()
