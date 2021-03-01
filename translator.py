import csv
from rich import print

sentence = input("Type a sentence: ")
print(f'[red]\n[u]Original[/u]:\n - {sentence}[/red]')

# Convert string to list
list_of_words = sentence.split()
for word in list_of_words:
    csv_file = open('shakespear_words_data.csv', 'r')
    csv_data = csv.reader(csv_file)

    for data in csv_data:
        if word.lower() == data[0]:
            list_of_words[list_of_words.index(word)] = data[1]
            break

# Convert list back to string
sentence = " ".join(list_of_words)
print(f'[green bold]\n[u]Translated[/u]:\n - {sentence}[/green bold]')
