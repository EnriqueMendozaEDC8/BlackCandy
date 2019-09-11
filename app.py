#Import Libraries
from flask import Flask
import os
#Start Flask
app = Flask(__name__)
app.secret_key = os.urandom(24)
#Load Configuration
app.config.from_pyfile('core/config.py')
#Load Main Listener
from listener.index import *

#Run App
if __name__ == '__main__':
    app.run()
