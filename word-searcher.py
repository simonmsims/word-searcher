import sys

PATH_DICT_SI = './dict/slovenian.txt'

ARGUMENT_WORD_LENGTH = 'word_length'


def word_searcher():
    args = _parse_arguments()
    if ARGUMENT_WORD_LENGTH in args:
        word_length = args[ARGUMENT_WORD_LENGTH]
        _search_for_word(word_length)
    else:
        raise Exception('Mandatory argument %s not set.' % ARGUMENT_WORD_LENGTH)


def _search_for_word(word_length):
    with open(PATH_DICT_SI) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        print ("TEST: '%s'" % line)
        if line.startswith('#'):
            pass
        elif word_length == len(line):
            print ("BINGO: '%s'" % line)
            pass


def _parse_arguments():
    if len(sys.argv) == 1:
        print("Input parameters are missing...")
        return []

    word_length = 0
    print(sys.argv[1])
    if sys.argv[1].startswith(ARGUMENT_WORD_LENGTH):
        result = sys.argv[1].split('=')
        print(result)
        if result[1].isdigit():
            word_length = int(result[1])
        else:
            raise Exception("Invalid value for parameter '%s'." % ARGUMENT_WORD_LENGTH)

    return dict(
        word_length=word_length,
    )


word_searcher()
