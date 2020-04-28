# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:25:12 2020

@author: ankit
"""


from flask import render_template
from flaskApp import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'),500