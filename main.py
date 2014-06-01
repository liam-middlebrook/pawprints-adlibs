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
data = data['results'][random.randint(0, len(data['results']))]['body']
#print json.dumps(data, sort_keys=True, indent=4 * ' ')
#print data
description = data

#tokenize the description into a list of words
textData = nltk.word_tokenize(description)

#pair the words with their tags (adjective, verb, noun, etc.)
textTags = nltk.pos_tag(textData)

#remove duplicates from the tag list
manTags = list(set(textTags))

outputString = description
for index in range(5):
    #get a random tag from the tagList
    randTag =  manTags[random.randint(0,len(manTags))]
    
    print randTag
    
    #Get a list of all the indices at which a word/tag pair occurs
    replacementIndices = [i for i, x in enumerate(textTags) if x == randTag]
    
    print replacementIndices
    
    
    print "Please type in the replword: "
    replWord = raw_input()
    
    #Now lets replace each occurance of that word with Butts!
    outputString = outputString.replace(randTag[0], replWord)
print outputString
