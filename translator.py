import csv
from rich import print

sentence = input("Type a sentence: ")
print(f'[red]\n[u]Original[/u]:\n - {sentence}[/red]')

# Convert string to list
list_of_words = sentence.split()
for word in list_of_words:
    csv_file = open('./shakespeare_word_keys.csv', 'r')
    csv_data = csv.reader(csv_file)

    for data in csv_data:
        if word.lower() == data[0]:
            replacement_word = data[1]
            if data[0] == 'thee' or data[0] == 'ye' or data[0] == 'thou':
                replacement_word = 'you'
            elif data[0] == 'thine' or data[0] == 'thy':
                replacement_word = 'your'
            list_of_words[list_of_words.index(word)] = replacement_word
            break

# Convert list back to string
sentence = " ".join(list_of_words)
print(f'[green bold]\n[u]Translated[/u]:\n - {sentence}[/green bold]')
