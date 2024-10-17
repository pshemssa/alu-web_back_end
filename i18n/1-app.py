#!/usr/bin/env python3

"""Basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)
Babel = babel(app)

class config:
 """CONFIG CLASS"""
  
 LANGUAGES=["en", "fr"]
 Babel_default_locale = 'en'
 Babel_default_timezone = 'UTC'

app.config.from_object(config)

@app.route('/')
def index():
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()