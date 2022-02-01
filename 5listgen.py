import json
import string

##
# source the word list
##

# words from https://github.com/dwyl/english-words
## only [[:alpha:]] words (words that only have letters, no numbers or symbols)
with open('words_dictionary.json') as json_file:
    data = json.load(json_file)
    words = data.keys() #get words

# all the 466kwords
# words_textfile = open("words.txt", "r")
# words = words_textfile.read().splitlines()

# maybe try https://github.com/mattbierner/urban-dictionary-word-list

##
# reduce to 5 letter words and make shure they are lowercase
## 

words = [word.lower() for word in words if len(word) == 5] # only five letter words and all in lower

##
# create dict which shows how prominent which letter is in this list
##

charcount = {}
for char in string.ascii_lowercase:
    charcount[char]=0;
for char in "".join(words):
    charcount[char]+=1;

##
# generate scores for words and order them acordingly
##

wordscores = {}

for word in words:
    wordscore = 0
    letters = list(dict.fromkeys(word)) #drop dublicate letters
    for letter in letters:
        wordscore += charcount[letter]
    wordscores[word] = wordscore

rankedwords = sorted(wordscores,key=wordscores.get, reverse=True)
print(rankedwords[:30])

##
# write list to file
## 

with open('5list.json', 'w') as outfile:
    json.dump(rankedwords, outfile)
