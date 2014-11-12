#We the people adlibs py
import urllib2
import simplejson as json
import nltk
import random
import argparse

p = argparse.ArgumentParser()

p.add_argument("key", nargs="+", help="Your PawPrints API Key")

args = p.parse_args()

api_key = args.key[0]
#Lets pull down the petitions from whitehouse.gov
dataResponse = urllib2.urlopen('https://pawprints.rit.edu/v1/petitions?key=' + api_key + '&limit=500')
dataJson = dataResponse.read()
dataResponse.close()

#Read the flatfile of petitions
#with open ("petitions.json", "r") as myfile:
#    dataJson=myfile.read().replace('\n', '')

#Lets parse the data from JSON to objects!
data = json.loads(dataJson)

#Get a random petition
dataID = random.randint(0, len(data)-1)

#Get the description of that petition
description = data[dataID]['description']

#Tell the user the tile of the petition
print "Title: " + data[dataID]['title']

#tokenize the description into a list of words
textData = nltk.word_tokenize(description)

#pair the words with their tags (adjective, verb, noun, etc.)
textTags = nltk.pos_tag(textData)

#remove duplicates from the tag list
manTags = list(set(textTags))

print "Please enter a word that fits each type given:"
outputString = description

#Lets add up to fifteen changed words in the petition
for index in range(15):
    #get a random tag from the tagList
    randTag =  manTags[random.randint(0,len(manTags)-1)]
    
    #Get the 'type' or word we are dealing with
    wordType = randTag[1]
    
    #Either query the user for a word of certain type or skip the word type if it's not good for adlibbing
    if wordType == "," or wordType == "TO" or wordType == "." or wordType == "POS" or wordType == "-NONE-" or wordType == ":" or wordType == "CD" or wordType == "DT":
        index-=1
        continue
    elif wordType == "NN" or wordType == "WP":
        print "TYPE: NOUN"
    elif wordType == "NNS":
        print "TYPE: NOUN (PLURAL)"
    elif wordType == "NNP":
        print "TYPE: PRONOUN"
    elif wordType == "PRP" or wordType == "PRPS" or wordType == "PRP$":
        print "TYPE: PROPER NOUN"
    elif wordType == "VB" or wordType == "VBG" or wordType == "VBP" or wordType == "VBZ" or wordType == "VBN":
        print "TYPE: VERB"
    elif wordType == "JJ":
        print "TYPE: ADJECTIVE"
    elif wordType == "RB":
        print "TYPE: ADVERB"
    else:
        print "TYPE: UNKNOWN"
    
    #Get a list of all the indices at which a word/tag pair occurs
    replacementIndices = [i for i, x in enumerate(textTags) if x == randTag]
    
    print "Please type in a word that matches the above type: "
    replWord = raw_input()
    
    #Now lets replace each occurrence of that word with Butts!
    outputString = outputString.replace(" "+randTag[0]+" ", " "+replWord+" ")

print "\n\nHere is the origional petition: \n"
print description
print "\n\nHere is what you created\n"
print outputString
