#We the people adlibs py
import urllib2
from textblob import TextBlob
import random
import argparse

try:
    import simplejson as json
except ImportError:
    import json

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

textTags = TextBlob(description).tags

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
    if wordType == "," or wordType == "TO" or wordType == "." or wordType == "-NONE-" or wordType == ":" or wordType == "CD" or wordType == "LS":
        index-=1
        continue
    elif wordType == "CC":
        print "TYPE: COORDINATING CONJUNCTION"
    elif wordType == "DT":
        print "TYPE: DETERMINER"
    elif wordType == "EX":
        print "TYPE: EXISTENTIAL THERE"
    elif wordType == "FW":
        print "TYPE: FOREIGN WORD"
    elif wordType == "IN":
        print "TYPE: PREPOSITION OR SUBORDINATING CONJUNCTION"
    elif wordType == "JJ":
        print "TYPE: ADJECTIVE"
    elif wordType == "JJR":
        print "TYPE: ADJECTIVE COMPARATIVE"
    elif wordType == "JJS":
        print "TYPE: ADJECTIVE SUPERLATIVE"
    elif wordType == "MD":
        print "TYPE: MODAL"
    elif wordType == "NN":
        print "TYPE: NOUN SINGLUAR OR MASS"
    elif wordType == "NNS":
        print "TYPE: NOUN PLURAL"
    elif wordType == "NNP":
        print "TYPE: PROPER NOUN SINGULAR"
    elif wordType == "NNPS":
        print "TYPE: PROPER NOUN PLURAL"
    elif wordType == "PDT":
        print "TYPE: PREDETERMINER"
    elif wordType == "POS":
        print "TYPE: POSSESSIVE ENDING"
    elif wordType == "PRP":
        print "TYPE: PERSONAL PRONOUN"
    elif wordType == "PRP$":
        print "TYPE: POSSESIVE PRONOUN"
    elif wordType == "RB":
        print "TYPE: ADVERB"
    elif wordType == "RBR":
        print "TYPE: ADVERB COMPARATIVE"
    elif wordType == "RBS":
        print "TYPE: ADVERB SUPERLATIVE"
    elif wordType == "RP":
        print "TYPE: PARTICLE"
    elif wordType == "SYM":
        print "TYPE: SYMBOL"
    elif wordType == "UH":
        print "TYPE: INTERJECTION"
    elif wordType == "VB":
        print "TYPE: VERB BASE FORM"
    elif wordType == "VBD":
        print "TYPE: VERB PAST TENSE"
    elif wordType == "VBG":
        print "TYPE: VERB GERUND OR PRESENT PARTICIPLE"
    elif wordType == "VBN":
        print "TYPE: VERB PAST PARTICIPLE"
    elif wordType == "VBP":
        print "TYPE: VERB NON 3RD PERSON SINGULAR PRESENT"
    elif wordType == "VBZ":
        print "TYPE: VERB 3RD PERSON SINGULAR PRESENT"
    elif wordType == "WDT":
        print "TYPE: WH-DETERMINER"
    elif wordType == "WP":
        print "TYPE: WH-PRONOUN"
    elif wordType == "WP$":
        print "TYPE: POSSESIVE WH-PRONOUN"
    elif wordType == "WRB":
        print "TYPE: WH-ADVERB"
    else:
        index-=1
        continue

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
