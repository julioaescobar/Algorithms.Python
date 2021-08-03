import re
import pprint
import unidecode

def normalize(word):
    return unidecode.unidecode(word)

def wordCounter(test):
    hash = {}
    test = re.sub("\?|!","",test)
    for word in test.split(" "):
        word = word.lstrip()
        if(normalize(word) in hash):
            hash[normalize(word)] += 1
        else:
            hash[normalize(word)] = 1

    pprint.pp(hash)

test = "hola que tal? cómo estás? qué tal te va? cómo te fue hoy? hoy vas a programar? estás?"
wordCounter(test)