#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:55:13 2016

@author: Shan
"""
import re, math, collections, itertools,sys ,glob,os,json

print("hello word")

class Predict:
    
    posFeatures = dict()
    negFeatures = dict()
    moviesReview = {}
    movieNewScore = dict()
    
    def loadFeatures(self,file):
        f = open(file,'rt',encoding='utf-8')
        lines = f.readlines()
        
        for line in lines:
            word,counts = line.strip().rsplit('\t',1) 
           
            counts = eval(counts)
            Predict.posFeatures[word] = counts[0]
            Predict.negFeatures[word] = counts[1]
        print('load finish')
        f.close()
    
    def loadMoives(self,file):
        
        data = []
        with open(file,'rt') as f:
            for line in f:
                data.append(json.loads(line))
            for movie in data:
                
                asin = movie['asin']
                if asin in Predict.moviesReview:
                    
                    
                    Predict.moviesReview[asin].append(movie)
                    
                else:
                    Predict.moviesReview[asin] = []
                    Predict.moviesReview[asin].append(movie)
        

    def bayesPredict(self):
        wronpos = 0
        wroneg = 0
        allres = 0
        for asin in Predict.moviesReview.keys():
            comPol = dict()
            aveValue = 0
            
            for info in Predict.moviesReview[asin]:
                movieComment ={}
                comment = info['reviewText']
                socre = info['overall']
                comFeatures = comment.split(' ')
                tmpWordProbPos = dict()
                tmpWordProbNeg = dict()
                newScoreP = 0
                newScoreN = 0
                
                allres += 1
                
                for word in comFeatures:
                    word = re.sub(r"[^A-Za-z]+", '', word)
                    
                    if word in Predict.posFeatures.keys():
                        if word not in tmpWordProbPos.keys():
                            tmpWordProbPos[word] = Predict.posFeatures[word]
                    if word in Predict.negFeatures.keys():
                        if word not in tmpWordProbNeg.keys():
                            tmpWordProbNeg[word] = Predict.negFeatures[word]

                
                for word,value in tmpWordProbPos.items():
                     newScoreP += math.log(value)
                for word,value in tmpWordProbNeg.items():
                     newScoreN += math.log(value)  
               
                if newScoreP > newScoreN:
                    if info['overall'] >= 3:
                        comPol[info['reviewerID']] = info['overall']
                    else:
                        wronpos += 1
                        print('aaaaaaaaa')
                        comPol[info['reviewerID']] = info['overall'] + 1
                else:
                    if info['overall'] < 3:
                        comPol[info['reviewerID']] = info['overall']
                    else:
                        wroneg += 1
                        
                        comPol[info['reviewerID']] = info['overall'] - 1
                
                
            for value in comPol.values():
                aveValue += value
            
            aveValue /=  len(comPol)
            aveValue = "{:.2f}".format(aveValue)
               
                
            Predict.movieNewScore[asin] = aveValue
        f = open('predict/bayes/result.txt','w')
        f.truncate()           
        for key,value in Predict.movieNewScore.items():
            f.write(key + ' ' + value+ '\n')
        print('neg wrong:')
        print(wroneg)
        print('pos wrong:')
        print(wronpos)
        print('total reviews:')
        print(allres)
        
             
                
        
                

    

        
           
            

pre = Predict()
pre.loadFeatures('predict/bayes/model.txt')


pre.loadMoives('predict/bayes/reviews.json')      
pre.bayesPredict()     
      

  
                             
           
    
    
 
       
    