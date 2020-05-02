# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:11:57 2020

@author: ankit
"""


import json
import requests
from flask_babel import _
from flaskApp import app

def translate(text, source_language, dest_language):
    if 'YD_TRANSLATOR_KEY' not in app.config or not app.config['YD_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    # auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    key=app.config['YD_TRANSLATOR_KEY']
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json'
                     '/translate?key={}&text={}&lang={}-{}'.format(
                         key, text, source_language, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    # return json.loads(r.text)['text']
    print(r.content.decode('utf-8-sig'))
    return json.loads(r.content.decode('utf-8-sig'))