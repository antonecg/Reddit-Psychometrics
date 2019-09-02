
import praw
import numpy as np
import matplotlib.pyplot as plt
import nltk
import pylab
from nltk.stem.porter import PorterStemmer
from itertools import groupby
import sys
import os
import csv
from scipy import stats


with open('neuroticism.csv') as f:
    reader = csv.reader(f, )
    neurodict = dict(reader)
with open('agr.csv') as h:
    reader = csv.reader(h, )
    agrdict = dict(reader)
with open('cons.csv') as i:
    reader = csv.reader(i, )
    consdict = dict(reader)
with open('ext.csv') as j:
    reader = csv.reader(j, )
    extdict = dict(reader)
with open('open.csv') as k:
    reader = csv.reader(k, )
    opendict = dict(reader)
    

# Taylor Jones was indespensible in the creation of this code

def words(entry):
    return filter(lambda w: len(w) > 0,
                  [w.strip("0123456789!:,.?(){}[]") for w in entry.split()])
# take from: http://swizec.com/blog/measuring-vocabulary-richness-with-python/swizec/2528 
def neuroscore(entry):
    d = {}
    stemmer = PorterStemmer()
    totalscorepost = 0
    scoreword = 0
    for w in words(entry):
        w = stemmer.stem(w).lower()
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1
        #scoreword = dict.get(w)
        try:
            totalscorepost += float(neurodict[w])
        except:
            continue

    
    try:
        return totalscorepost/float(len(d))
    except ZeroDivisionError:
        return 0
def agrscore(entry):
    d = {}
    stemmer = PorterStemmer()
    totalscorepost = 0
    scoreword = 0
    for w in words(entry):
        w = stemmer.stem(w).lower()
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1
        #scoreword = dict.get(w)
        try:
            totalscorepost += float(agrdict[w])
        except:
            continue

    
    try:
        return totalscorepost/float(len(d))
    except ZeroDivisionError:
        return 0
    
def conscore(entry):
    d = {}
    stemmer = PorterStemmer()
    totalscorepost = 0
    scoreword = 0
    for w in words(entry):
        w = stemmer.stem(w).lower()
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1
        #scoreword = dict.get(w)
        try:
            totalscorepost += float(consdict[w])
        except:
            continue
    try:
        return totalscorepost/float(len(d))
    except ZeroDivisionError:
        return 0
    
def extscore(entry):
    d = {}
    stemmer = PorterStemmer()
    totalscorepost = 0
    scoreword = 0
    for w in words(entry):
        w = stemmer.stem(w).lower()
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1
        #scoreword = dict.get(w)
        try:
            totalscorepost += float(extdict[w])
        except:
            continue
    try:
        return totalscorepost/float(len(d))
    except ZeroDivisionError:
        return 0
    
def openscore(entry):
    d = {}
    stemmer = PorterStemmer()
    totalscorepost = 0
    scoreword = 0
    for w in words(entry):
        w = stemmer.stem(w).lower()
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1
        #scoreword = dict.get(w)
        try:
            totalscorepost += float(opendict[w])
        except:
            continue
    try:
        return totalscorepost/float(len(d))
    except ZeroDivisionError:
        return 0

    


while True:
    person = input('Enter code: ')
    reddit = praw.Reddit(client_id='xxxxx,
                         client_secret=xxxx
                         user_agent=xxxx
   
    ltime =[]
    lnscore = []
    lascore =[]
    lcscore =[]
    lescore=[]
    loscore=[]
    lredditor =[]
    ltext= []
    submission = reddit.submission(id=person)
    submission.comment_sort = 'old'
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
    
        sentences = nltk.tokenize.sent_tokenize(comment.body)
        time = comment.created
        ltime.append(comment.created_utc)
        
        author = comment.author
        lredditor.append(author)

        
        text= str(comment.body)
        ltext.append(text)
        
        gettingneuro = neuroscore(text)
        lnscore.append(gettingneuro)
        
        gettingagr= agrscore(text)
        lascore.append(gettingagr)
        
        gettingext = extscore(text)
        lescore.append(gettingext)
        
        gettingcons = conscore(text)
        lcscore.append(gettingcons)
        
        gettingopen = openscore(text)
        loscore.append(gettingopen)

        
    atime = np.asarray(ltime)
    ay = np.asarray(lnscore)
    
    x = (atime)/86400
    y = (ay)
    finiteYmask = np.isfinite(y)
    yclean = y[finiteYmask]
    xclean = x[finiteYmask]
    x = xclean
    #print (x)
       
    print(ltime)
    print(lnscore)
    print(lascore)
    print(lcscore)
    print(lescore)
    print(loscore)
    print(lredditor)

