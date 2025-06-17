__Task description__

Implement the two custom exceptions: ```InputFormatError``` and ```SplitError```, both of which are derived from ```ValueError```.

Implement a function that splits the input text into the specified number of parts so that each part (except, possibly, for the last one) contains the same number of words. The function must raise the following exceptions:

```InputFormatError```, if the text contain characters other than English letters and whitespaces, or the words are separated by more than one whitespace

```ValueError```, if the number of text parts is not positive

```SplitError```, if the split cannot be done, i.e., the number of words in the text is less than the number of text parts

<br>

__Test data sets examples__

| № | Input data | Expected output |
|----------|----------|----------|
| 1    | Text to be split, 2     | Text to, be split     |
| 2    | Text of incorrect format!!, 2     | InputFormatError     |
| 3    | Invalid argument, 0     | ValueError     |
| 4    | Oh no, 3     | SplitError     |