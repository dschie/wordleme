import json

# words from https://github.com/dwyl/english-words
## only [[:alpha:]] words (words that only have letters, no numbers or symbols)
with open('words_dictionary.json') as json_file:
    data = json.load(json_file)
    words = data.keys() #get words

# all the 466kwords
# words_textfile = open("words.txt", "r")
# words = words_textfile.read().splitlines()

# maybe try https://github.com/mattbierner/urban-dictionary-word-list

print(len(list(words)))
words = [word.lower() for word in words if len(word) == 5] # only five letter words and all in lower
print(len(list(words)))

with open('5list.json', 'w') as outfile:
    json.dump(words, outfile)