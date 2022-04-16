"""
App configuration:
Note that if you change something in .env, it's cached by pipenv. You have to
exit and re-attach the env to the shell.
"""

import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    FLASK_APP = os.environ["FLASK_APP"]
    FLASK_ENV = os.environ["FLASK_ENV"]
    FLASK_DEBUG = os.environ["FLASK_DEBUG"]
    CSRF_ENABLED = os.environ["CSRF_ENABLED"]
    SECRET_KEY = os.environ["SECRET_KEY"]
