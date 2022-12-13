# phrasegen

Simple *Python* method to to generate a passphrase of words read from a given text file.

The method requires the `random` module in order to work.

## Usage

The text file must contain at least one random word per line, for example:

```
flag
blue
fork
```

Length and case of the words does not matter, so the file can also look like this:

```
Beautiful
Bread
Glasses
```

In the included word list, all words have a length of 4 characters and start with a capital letter.

The method itself looks like this and should be more or less self explaining:

```python
phrasegen(count_words=4,        # number of words for the passphrase
          case_lower=False,     # return the passphrase only in lower case
          case_upper=False,     # return the passphrase only in upper case
          allow_same=True,      # allow the same word multiple times
          use_spaces=True,      # separate each word with a space character
          space_char=" "        # character to use as space
          file_list=None)       # the file from which to read the words
```

For example, if you want to create a passphrase with a length of 6 words from a file called `words.txt` in lower-case letters each separated with a blank space (default), it would like this

```python
phrasegen(count_words=6, case_lower=True, file_list="words.txt")
```

or in the short form:

```python
phrasegen(6, True, False, True, True, " ", "words.txt")
```

