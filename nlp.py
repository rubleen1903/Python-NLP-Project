from bs4 import BeautifulSoup

import urllib.request

import nltk

import matplotlib.pyplot as plt

from nltk.corpus import stopwords

response = urllib.request.urlopen('https://localhackday.mlh.io/local-hack-day-share-challenges')

html = response.read()

soup = BeautifulSoup(html,"html5lib")

text = soup.get_text(strip=True)

tokens = [t for t in text.split()]

clean_tokens = tokens[:]

sr = stopwords.words('english')

for token in tokens:

    if token in stopwords.words('english'):

        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key,val in freq.items():

    print (str(key) + ':' + str(val))
    freq.plot(20,cumulative=False)