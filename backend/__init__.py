from flask import Flask
import flask_assets as assets

import os

def root_dir():  
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

app=Flask(__name__, root_path=root_dir())
app.config.from_object('backend.settings')
print root_dir() 

env = assets.Environment(app)

env.load_path = [
    os.path.join(root_dir(), 'assets/sass')
]

env.register(
    'css_all',
    assets.Bundle(
        'app.scss',
        filters='sass',
        output='css/app.scss.css'
    )
)

from backend import controller
