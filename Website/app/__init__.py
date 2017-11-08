#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:28:51 2016

@author: Shan
"""

from flask import Flask

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Shan1030'
app.config['MYSQL_DATABASE_DB'] = 'BigDataPro'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


from app import test