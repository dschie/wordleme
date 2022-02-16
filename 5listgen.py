import json
import string
from urllib.request import urlopen

##
# source the word list
##

# words from https://github.com/dwyl/english-words
## only [[:alpha:]] words (words that only have letters, no numbers or symbols)
# with open('words_dictionary.json') as json_file:
#     data = json.load(json_file)
#     words = data.keys() #get words

# all the 466kwords
# words_textfile = open("words.txt", "r")
# words = words_textfile.read().splitlines()

# maybe try https://github.com/mattbierner/urban-dictionary-word-list


# from the video about solving wordle with information theory: https://www.youtube.com/watch?v=v68zYyaEmEA
# possible words (from the wordle source code)
# https://raw.githubusercontent.com/3b1b/videos/master/_2022/wordle/data/possible_words.txt
resource = urlopen("https://raw.githubusercontent.com/3b1b/videos/master/_2022/wordle/data/possible_words.txt")
content =  resource.read().decode(resource.headers.get_content_charset())
words = content.splitlines()

# word frequency (extracted from http://commondatastorage.googleapis.com/books/syntactic-ngrams/index.html)
# https://raw.githubusercontent.com/3b1b/videos/master/_2022/wordle/data/freq_map.json 
resource = urlopen("https://raw.githubusercontent.com/3b1b/videos/master/_2022/wordle/data/freq_map.json")
content =  resource.read().decode(resource.headers.get_content_charset())
word_frequency =  json.loads(content)
print(len(word_frequency))



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
    wordscores[word] = wordscore*word_frequency[word]

rankedwords = sorted(wordscores,key=wordscores.get, reverse=True)

#multiply ranking with word frequency?


print([(word,wordscores[word]) for word in rankedwords[:30]])

##
# write list to file
## 

with open('5list.json', 'w') as outfile:
    json.dump(rankedwords, outfile)
