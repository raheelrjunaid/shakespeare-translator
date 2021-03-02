# Welcome to the Shakespearean word Translator
This is a mini-project that converts words from a shakespearean phrase/sentence into regular english using a table of values (in CSV format).

![Terminal Screenshot](https://user-images.githubusercontent.com/60077374/109578792-09fa4d00-7ab5-11eb-8447-f9f8ec5600f0.png)
> The program uses the `rich` pip module give a readable output.

## Dependencies
You will need to install the rich package using the pip installer:
```python
pip3 install rich
```
That's it!

## Design
The design is meant to be compact and fast while also keeping it simple. You may notice that searching through the list of shakespearean words is implemented using a linear search algorithm, which is quite simple and time efficient as there isn't that many words.

### Flaws
There are a few flaws that can only be solved through human-interpretation or
artificial intellegence (that would also need some context).

#### Major
- The use of words such as "art" which translates to "are".
Shakespeare sometimes refers to the modern version of art which means that
translating the word would be incorrect.
#### Minor
- Punctuation also gets in the way as it is treated as 1 word meaning it won't
    be compared correctly. A period at the end of a word could be
removed (see the issues for more info.), but this could also be done manually
by the user.
- Words that have capitals are not returned as capitals. Every word is
    lowercased in the translation (see the issues for more info.).

## Contribution
### Words
There is a whole library full of words that aren't in the csv file (such as "Liketh"). Please feel free to add any to make this program more accurate!
### Issues
Please create an issue if there is something that doesn't work, or an improvement needs to be made. There are already existing issues that are up, so make sure to give those a look if you plan on forking the repo :smile:
