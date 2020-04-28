# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 01:34:52 2020

@author: ankit
"""


from flaskApp import app,db

from flaskApp.models import User,Post

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}