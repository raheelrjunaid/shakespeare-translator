# Welcome to the Shakespearean Word Translator
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
- Many words aren't going to be translated. [Contribute](#Contribution) to add to the list of words!
- The use of words such as "art" which translates to "are".
Shakespeare sometimes refers to the modern version of art which means that
translating the word would be incorrect.
> The output provides the input **and** the translation so the user can easily see the original word if the translation doesn't make sense.

## Contribution
### Words
There is a whole library full of words that aren't in the csv file (such as "liketh" or "doth"). Please feel free to add any to make this program more accurate!
### Issues
Please create an issue if there is something that doesn't work, or an improvement needs to be made. There are already existing issues that are up, so make sure to give those a look if you plan on forking the repo :smile:
