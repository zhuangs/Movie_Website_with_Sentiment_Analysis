#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:04:10 2016

@author: Shan
"""
import collections
from flask import render_template, request, flash, redirect
from flaskext.mysql import MySQL
from app import app


mysql = MySQL()

mysql.init_app(app)
@app.route('/')
def hello():
  
    return render_template('hello.html')
   
@app.route('/recommand')
def recomSearch():
    
    
    
    return render_template('recomSearch.html')

@app.route('/recommandResult',methods = ['POST', 'GET'])
def recommand():
    
    result = request.args.get('movieName')
    newresult = ""
    
    if result != None:
        for c in result:
            if c == '+':
                newresult += " "
            else:
                newresult += c
   
    cursor = mysql.connect().cursor()
    
    
    cursor.execute("SELECT * from movie where title = %s",newresult)
    movie = cursor.fetchone()
    
    
    
    movieId = movie[0]
    cursor.execute("SELECT * from recommendation where movie_num = %s",movieId)
    recoMovies = cursor.fetchone()
    reco1 = recoMovies[1]
    reco2 = recoMovies[2]
    reco3 = recoMovies[3]
    reco4 = recoMovies[4]
    reco5 = recoMovies[5]
    reco6 = recoMovies[6]
    
    
    
  
    movieList = {}

    if reco1 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco1)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        reMovie['new_rating'] = reco1Res[13]

        movieList[reco1Res[13]] = reMovie
       
    if reco2 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco2)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        reMovie['new_rating'] = reco1Res[13]
        
        movieList[reco1Res[13]] = reMovie
        
    if reco3 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco3)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        reMovie['new_rating'] = reco1Res[13] 
        
        movieList[reco1Res[13]] = reMovie

    if reco4 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco4)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        reMovie['new_rating'] = reco1Res[13] 
        
        movieList[reco1Res[13]] = reMovie

    if reco5 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco5)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        reMovie['new_rating'] = reco1Res[13] 
        
        movieList[reco1Res[13]] = reMovie

    if reco6 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco6)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        reMovie['new_rating'] = reco1Res[13] 
        
        movieList[reco1Res[13]] = reMovie
    
    
    '''
    if movie == None:
        flash('Movie %s is not found',% movie)
        return redirect(url_for('recommand'))
    '''
    
    od = collections.OrderedDict(sorted(movieList.items(),reverse=True))
    
    return render_template("recomResult.html",movie=od,movie1=movieList)

    
    
    

  

@app.route('/movie', methods = ['GET', 'POST'])
def movie():
    movieName = request.args.get('movieName')
    print (movieName)
    newName = ""
    if movieName != None:
        for c in movieName:
            if c == '+':
                newName += " "
            else:
                newName += c
    print (newName)
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from movie where title = %s",newName)
    movie = cursor.fetchone()
    if movie is not None:
       movieId = movie[0]
       cursor.execute("SELECT * from review where movie_num = %s",movieId)
       review = cursor.fetchone()
    if movie == None:
        flash('Movie %s not found.' % movie)
        return redirect(url_for('/'))
    ss = movie[1]
    if review == None:
        flash('Review %s not found.' % movie)
        return redirect(url_for('/'))
    details = {'title': movie[1], 'director': movie[2], 'actor1':movie[3], 'actor2':movie[4], 'actor3':movie[5],'genre':movie[6], 'country':movie[7],'language':movie[8], 'year':movie[9],'content_rating':movie[10],'image':movie[11], 'imdb_rating':movie[12], 'new_rating':movie[13]}
    reviewList = {'review1': review[1],'review2': review[2],'review3': review[3]}
    



    
    cursor.execute("SELECT * from recommendation where movie_num = %s",movieId)
    recoMovies = cursor.fetchone()
    reco1 = recoMovies[1]
    reco2 = recoMovies[2]
    reco3 = recoMovies[3]
    reco4 = recoMovies[4]
    
    
    
  
    movieList = {}

    if reco1 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco1)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]

        movieList[reco1Res[0]] = reMovie
       
    if reco2 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco2)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        
        movieList[reco1Res[0]] = reMovie
        
    if reco3 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco3)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        
        movieList[reco1Res[0]] = reMovie

    if reco4 != 0:
        cursor.execute("SELECT * from movie where movie_num = %s", reco4)
        reco1Res = cursor.fetchone()
        
        reMovie = dict()
        reMovie['title'] = reco1Res[1]
        reMovie['image'] = reco1Res[11]
        
        movieList[reco1Res[0]] = reMovie

    
    return render_template('movieProfile.html', title='movie', details = details, reviewList = reviewList, recomList = movieList)


@app.route('/prediction')
def prediction():
    
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from prediction where rate = '8-10'")
    firstClass = cursor.fetchall()
    cursor.execute("SELECT * from prediction where rate = '6-8'")
    secondClass = cursor.fetchall()
    cursor.execute("SELECT * from prediction where rate = '4-6'")
    thirdClass = cursor.fetchall()
    return render_template('prediction.html', firstClass = firstClass, secondClass = secondClass, thirdClass = thirdClass)