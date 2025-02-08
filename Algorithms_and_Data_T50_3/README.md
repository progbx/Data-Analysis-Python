__Task description__

Given an integer __x__ (__0 <= x <= 100__) that denotes the progress in percents, print the
progress bar in the following format (below is an example for __x = 91__): <br>
"|#########|91%"

The progress bar is a one-line string, that consists of:
* The start character "|"
* 10 characters: a few "#" first, then " " (spaces). Each "#" character corresponds to 10% of the progress; you should display the maximum number of "#" characters so that the total progress does not exceed __x__.
* The rest of the characters should be " ", so that the total number of "#" and " " characters is 10.
* The end character "|".
* Progress (in percent), e.g., "91%".

Put your output in the string variable __progress_bar__.

<br>

__Test data sets examples__

| № |  Input data  | Expected output |
|:-----|:--------:|------:|
| 1   | 91 | \|#########\|91% |
| 2   |  100  |   \|##########\|100% |