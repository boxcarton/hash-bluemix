import os
import json
from flask import Flask

app = Flask(__name__)

app.config.from_object('hash.settings')
app.url_map.strict_slashes = False


import hash.core
import hash.models
import hash.controllers