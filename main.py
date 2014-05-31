#We the people adlibs py
import urllib2
import simplejson as json
import nltk

#dataResponse = urllib2.urlopen('https://api.whitehouse.gov/v1/petitions.json?limit=300&offset=0')
#dataInfo = dataResponse.info()
#dataJson = dataResponse.read()
#dataResponse.close()

with open ("petitions.json", "r") as myfile:
    dataJson=myfile.read().replace('\n', '')
data = json.loads(dataJson)
data = data['results'][2]['body']
print json.dumps(data, sort_keys=True, indent=4 * ' ')
print data
testDescription = data

textData = nltk.word_tokenize(testDescription)
textTags = nltk.pos_tag(textData)
print textTags
