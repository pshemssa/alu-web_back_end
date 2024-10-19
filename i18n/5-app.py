#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)

babel = Babel(app)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@app.route('/')
def hello():
    """ GET /
    Return:
      - Render template
    """
    login = False
    if g.get('user'):
        login = True
    return render_template('4-index.html', login = login)


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    """Get user information from users dict"""
    try:
        login_as = int(request.args.get('login_as'))
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request"""
    user = get_user()
    print(user)
    if user:
        g.user = user


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
