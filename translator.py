import csv
from rich import print

sentence = input("Type a sentence: ")
# Convert string to list
list_of_words, strikethrough_list = sentence.split(), sentence.split()

# Open csv file (needs to be opened multiple times to be read multiple times)
csv_file = open('./shakespeare_word_keys.csv', 'r')
csv_data = csv.reader(csv_file)

# Strike out words that need to be removed
for data in csv_data:
    if data[0] in list_of_words:
        strikethrough_list[list_of_words.index(data[0])] = f"[s]{data[0]}[/s]"

# Print new sentence with crossed out words
sentence = " ".join(strikethrough_list)
print(f'[red]\n[u]Original[/u]:\n - {sentence}[/red]')

for word in list_of_words:
    csv_file = open('./shakespeare_word_keys.csv', 'r')
    csv_data = csv.reader(csv_file)

    # Check for puntuation marks
    if word[-1] == ",":
        list_of_words[list_of_words.index(word)] = word.replace(",", "")
        word = word.replace(",", "")
    elif word[-1] == ".":
        list_of_words[list_of_words.index(word)] = word.replace(".", "")
        word = word.replace(".", "")

    for data in csv_data:
        # See if word is in csv_data (is it Shakespearean)
        if word.lower() == data[0]:
            replacement_word = data[1]
            # Change replacement word manually if there are multiple words
            # Ex. Thee, ye, and thou all mean "you"
            if data[0] == 'thee' or data[0] == 'ye' or data[0] == 'thou':
                replacement_word = 'you'
            elif data[0] == 'thine' or data[0] == 'thy':
                replacement_word = 'your'
            replacement_word = f"[bold u]{replacement_word}[/bold u]"
            list_of_words[list_of_words.index(word)] = replacement_word
            break

# Convert list back to string
sentence = " ".join(list_of_words)
print(f'[green]\n[u]Translated[/u]:\n - {sentence}[/green]')
