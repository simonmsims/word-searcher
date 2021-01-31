# word-searcher

Word searcher is a robot designed for assistance whenever you get stuck in a game [Words of Wonders: Crossword to Connect Vocabulary](https://play.google.com/store/apps/details?id=com.fugo.wow&hl=en&gl=US])

## Deployment ##

### Installation ###

Prepare virtual environment 

Create environment for Python 3
```
$ python3 -m venv env
```

Activate environment for Python 3
```
$ source env/bin/activate
```

Install all the requirements
```
$ pip install -r requirements.txt
```

## Usage

```
$ python word-searcher word_length=[N] word_set=[char1,...,charN] word_offset=[char1,offset1] word_offset=[char2,offset2]
```
