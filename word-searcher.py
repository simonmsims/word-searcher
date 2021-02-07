import sys

PATH_DICT_SI = './dict/slovenian.txt'

ARGUMENT_WORD_LENGTH = 'word_length'
ARGUMENT_WORD_SET = 'word_set'


def word_searcher():
    word_set = []
    word_length = 0
    args = _parse_arguments()
    if ARGUMENT_WORD_LENGTH in args:
        word_length = args[ARGUMENT_WORD_LENGTH]
    if ARGUMENT_WORD_SET in args:
        word_set = args[ARGUMENT_WORD_SET]
    if word_length > 0:
        _search_for_word(word_length, word_set)
    else:
        raise Exception('Mandatory argument %s not set.' % ARGUMENT_WORD_LENGTH)


def _search_for_word(word_length, word_set):
    with open(PATH_DICT_SI) as f:
        lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
        if line.startswith('#'):
            pass
        elif word_length == len(line):
            found = True
            if len(word_set) > 0:
                for char in word_set:
                    if char not in line:
                        found = False
                for char in line:
                    if char not in word_set:
                        found = False
            if found:
                print ("'%s'" % line)


def _parse_arguments():
    if len(sys.argv) == 1:
        print("Input parameters are missing...")
        return []

    word_length = 0
    word_set = []
    print(sys.argv[1])
    if sys.argv[1].startswith(ARGUMENT_WORD_LENGTH):
        result = sys.argv[1].split('=')
        print(result)
        if result[1].isdigit():
            word_length = int(result[1])
        else:
            raise Exception("Invalid value for parameter '%s'." % ARGUMENT_WORD_LENGTH)
    if len(sys.argv) > 2 and sys.argv[2].startswith(ARGUMENT_WORD_SET):
        result = sys.argv[2].split('=')
        result = result[1].split(',')
        for char in result:
            word_set.append(char)

    return dict(
        word_length=word_length,
        word_set=word_set
    )


word_searcher()
