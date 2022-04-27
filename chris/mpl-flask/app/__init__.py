"""
Basic app factory
"""

import os
import urllib
from pathlib import Path

from flask import Flask, redirect, request
from flask_assets import Environment, Bundle


from config import Config

# Import views after packages to be initialized in create_app()
from .routes import main

# App directory
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / "app"
UPLOAD_DIR = APP_DIR / "static" / "img" / "uploads"


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config["BASE_DIR"] = BASE_DIR
    app.config["APP_DIR"] = APP_DIR
    app.config["UPLOAD_DIR"] = UPLOAD_DIR

    # Fix Heroku http -> https

    @app.before_request
    def before_request():
        if 'DYNO' in os.environ: # Only runs when on heroku
            if request.url.startswith('http://'):
                url = request.url.replace('http://', 'https://', 1)
                code = 301
                return redirect(url, code=code)

    # Assets

    asset_env = Environment(app)

    # CSS
    css_bundle = Bundle(
        "css/normalize.scss",
        "css/main.scss",
        "css/forms.scss",
        filters="pyscss,cssmin",
        output="build/build.css",
    )
    asset_env.register("css_all", css_bundle)

    # Javascript
    js_bundle = Bundle(
        "js/main.js", filters="jsmin", output="build/build.js"
    )
    asset_env.register("js_all", js_bundle)

    # Blueprints

    app.register_blueprint(main.bp)

    # Template injection

    @app.context_processor
    def helpers():
        def currency(amount):
            return f"${amount:,.2f}"

        return dict(currency=currency)

    return app
