#We the people adlibs py
import urllib2
import simplejson as json
import nltk
from collections import Counter

import random
#dataResponse = urllib2.urlopen('https://api.whitehouse.gov/v1/petitions.json?limit=300&offset=0')
#dataInfo = dataResponse.info()
#dataJson = dataResponse.read()
#dataResponse.close()

with open ("petitions.json", "r") as myfile:
    dataJson=myfile.read().replace('\n', '')
data = json.loads(dataJson)
dataID = random.randint(0, len(data['results'])-1)
description = data['results'][dataID]['body']
#print json.dumps(data, sort_keys=True, indent=4 * ' ')
#print data

#Tell the user the tile of the petition
print "Title: " + data['results'][dataID]['title']

#tokenize the description into a list of words
textData = nltk.word_tokenize(description)

#pair the words with their tags (adjective, verb, noun, etc.)
textTags = nltk.pos_tag(textData)

#remove duplicates from the tag list
manTags = list(set(textTags))

print "Please enter a word that fits each type given:"
outputString = description
for index in range(15):
    #get a random tag from the tagList
    randTag =  manTags[random.randint(0,len(manTags)-1)]
    
    wordType = randTag[1]
    #print wordType
    if wordType == "," or wordType == "TO" or wordType == "." or wordType == "POS" or wordType == "-NONE-" or wordType == ":" or wordType == "CD" or wordType == "DT":
        index-=1
        break
    elif wordType == "IN":
        print "TYPE: INTERJECTION"
    elif wordType == "CC":
        print "TYPE: CONJUNCTION"
    elif wordType == "NN" or wordType == "WP":
        print "TYPE: NOUN"
    elif wordType == "NNS":
        print "TYPE: NOUN (PLURAL)"
    elif wordType == "NNP" or wordType == "PRP":
        print "TYPE: PRONOUN"
    elif wordType == "VB" or wordType == "VBG" or wordType == "VBP" or wordType == "VBZ" or wordType == "VBN":
        print "TYPE: VERB"
    elif wordType == "JJ":
        print "TYPE: ADJECTIVE"
    elif wordType == "RB":
        print "TYPE: ADVERB"
    elif wordType == "PRPS" or wordType == "PRP$":
        print "TYPE: PREPOSITION"
    else:
        print "TYPE: UNKNOWN"
    #print randTag
    
    #Get a list of all the indices at which a word/tag pair occurs
    replacementIndices = [i for i, x in enumerate(textTags) if x == randTag]
    
    #print replacementIndices
    
    
    print "Please type in the replword: "
    replWord = raw_input()
    
    #Now lets replace each occurance of that word with Butts!
    outputString = outputString.replace(" "+randTag[0], " "+replWord)
print outputString
