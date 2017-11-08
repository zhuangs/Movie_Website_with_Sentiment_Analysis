#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:28:00 2016

@author: Shan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:35:11 2016

@author: Shan
"""

import random
import sys
import math
import collections
import re
import os
import io
import codecs

lables = ['pos', 'neg']

def lableToId(lable):#tranform the label to id
    for i in range(len(lables)):
        if lable == lables[i]:
            return i
    raise Exception('Error lable %s' % (lable))

def docdict():#return a zero vector which length is equal to the lables length
    return [0]*len(lables)

def loadFeatureWord():#load the feature words as the dictionary
    f = open('Dataset.txt')
    docCounts = eval(f.readline())
    features = set()
    for line in f:
        features.add(line.strip())
    f.close()
    #print (features)
    return docCounts,features

def trainBayes():
    docCounts,features = loadFeatureWord()
    #docCount = [0]*len(lables)
    wordCount = collections.defaultdict(docdict)
    tCount = [0]*len(docCounts)#store the words of every category
    for p in os.listdir('/Users/Shan/Downloads/aclImdb/train/pos'):
        pp = open('/Users/Shan/Downloads/aclImdb/train/pos/'+p, 'rt', encoding='utf-8');
        for line in pp:  
            words = line.split(' ')
            for word in words:
                if word in features:
                 word = re.sub(r"[^A-Za-z]+", '', word)
                 wordCount[word][0] += 1#calculate every feature words' frequency in all category
                 tCount[0] += 1
    for n in os.listdir('/Users/Shan/Downloads/aclImdb/train/neg'):
        nn = open('/Users/Shan/Downloads/aclImdb/train/neg/'+n, 'rt', encoding='utf-8')
        for line in nn:      
            words = line.split(' ')
            for word in words:
                if word in features:
                 word = re.sub(r"[^A-Za-z]+", '', word)
                 wordCount[word][1] += 1
                 tCount[1] += 1
    for k,v in wordCount.items():
        scores = [(v[i]+1) * 1.0 / (tCount[i]+len(wordCount)) for i in range(len(v))]#calculate the possiblities 
        print ('%s\t%s' % (k,scores))

def loadModel():
    #load the bayes model which also the result from the train step
    f = open('model.txt')
    scores = {}
    words = set()
    for line in f:
        word,counts = line.strip().rsplit('\t',1) 
        words.add(word)
        scores[word] = eval(counts)
    f.close()
    return scores,words
    
def testBayes():
    docCounts, features = loadFeatureWord()
    docscores = [math.log(count * 1.0 /sum(docCounts)) for count in docCounts]
    scores,wordDic= loadModel()
    print (scores)
    rCount = 0
    docCount = 0
    for p in os.listdir('/Users/Shan/Downloads/aclImdb/test/pos'):
        pp = open('/Users/Shan/Downloads/aclImdb/test/pos/'+p, 'rt', encoding='utf-8', errors='ignore');
        for line in pp: 
            words = line.split(' ')
            preValues = list(docscores)
            for word in words:
                if word in wordDic:
                 word = re.sub(r"[^A-Za-z]+", '', word)
                 for i in range(len(preValues)):
                     preValues[i]+=math.log(scores[word][i])
            m = max(preValues)
            pIndex = preValues.index(m)
            if pIndex == 0:
                rCount += 1
            print (lables[pIndex],words)
            docCount += 1
            #print (docCount)
        #print (rCount, docCount, rCount * 1.0 / docCount)
    
    for n in os.listdir('/Users/Shan/Downloads/aclImdb/test/neg'):
        nn = open('/Users/Shan/Downloads/aclImdb/test/neg/'+n, 'rt', encoding='utf-8', errors='ignore');
        for line in nn: 
            words = line.split(' ')
            preValues = list(docscores)
            for word in words:
                if word in wordDic:
                 word = re.sub(r"[^A-Za-z]+", '', word)
                 for i in range(len(preValues)):
                     preValues[i]+=math.log(scores[word][i])
            m = max(preValues)
            pIndex = preValues.index(m)
            if pIndex == 1:
                rCount += 1
            print (lables[pIndex],words)
            docCount += 1
            #print (docCount)
    print (rCount, docCount, rCount * 1.0 / docCount)
    
if __name__=="__main__":
    #trainBayes()
    testBayes()
    #loadModel()
    