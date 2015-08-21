import re
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import json
import psycopg2
try:
    conn = psycopg2.connect("dbname='english' user='postgres' host='localhost' password='postgres'")
except:
    print "I am unable to connect to the database"

def getSoup(url):
	html = urllib2.urlopen(url)
	return BeautifulSoup(html)

def getMeaning(word):
	soup = getSoup('http://www.merriam-webster.com/dictionary/'+word)
	all_definitions = soup.find_all('span',class_='ssens')
	meaning = []
	for p in all_definitions:
		meaning.append(p.text)
	return meaning
	
def getAntonyms(word):
	soup = getSoup('http://www.thesaurus.com/browse/'+word)
	all_antonyms = soup.find_all('div',class_='list-holder')
	if len(all_antonyms) > 0:
		all_antonyms = all_antonyms[0].find_all('span',class_='text')
	meaning = []
	for p in all_antonyms:
		meaning.append(p.text)
	return meaning

def getSynomyms(word):
	soup = getSoup('http://www.thesaurus.com/browse/'+word)
	all_synomyms = soup.find_all('div',class_='relevancy-list')[0].find_all('span',class_='text')
	synomyms = []
	for p in all_synomyms:
		synomyms.append(p.text)
	return synomyms

def getSynonymsDiscussion(word):
	soup = getSoup('http://www.merriam-webster.com/dictionary/'+word)
	return soup.find_all('div',class_='synonyms-discussion')

def getEtymology(word):
	url = 'http://www.etymonline.com/index.php?term='+word+'&allowed_in_frame=0'
	soup=getSoup(url)
	return soup.find_all('dd',class_='highlight')[0].text

def getMnenomonic(word):
	url = 'http://mnemonicdictionary.com/word/'+word        
	soup = getSoup(url)
	return soup.find_all('div',class_='span9')[0].text

def getExamples(word):
	url='http://corpus.vocabulary.com/api/1.0/examples.json?maxResult=24&query='+word
	data = json.load(urllib2.urlopen(url))
	example = []
	for s in data['result']['sentences']:
		example.append(s['sentence'])
	return example

def getImage(word):
	url = 'http://wordpandit.com/2012/'+word+'/'
	soup = getSoup(url)
	content=soup.find_all('img',title=word.title())
	imgUrl = content[0]['src']
	image = urllib.urlretrieve(imgUrl, os.path.basename('/images/'+imgUrl))

def getWordDetails(word,title,desc):
	data = {}
	data['word'] = word
	data['theme-title'] = title
	data['theme-desc'] = desc
	data['meaning'] = getMeaning(word)
	data['Antonyms'] = getAntonyms(word)
	data['Synomyms'] = getSynomyms(word)
	data['etymology'] = getEtymology(word)
	data['mnemonic'] = getMnenomonic(word)
	data['examples'] = getExamples(word)
	for k in data:
		print(k)
		print(data[k]) 

def allWordsByGroup(url):
	soup = getSoup(url)
	title=soup.find_all(id='themetitle')[0].string
	desc = soup.find_all(id='themedesc')[0].string
	wordList = soup.find_all('a',class_='positive')
	for word in wordList:
		word = re.sub("\\(.*?\\)","",word.string)
		wordData = getWordDetails(word,title,desc)

def main():
	#maximum possible is 95
	for i in range(1,2):
		url = 'https://www.greedge.com/grewordlist/words/'+str(i)
		allWordsByGroup(url)

main()			
