#Basic configuration
ENV = 'production'
DEBUG = True 
TESTING = False
SECRET_KEY = None
#Cokkies configuration
SESSION_COOKIE_NAME = None
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_PATH = None
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False
MAX_COOKIE_SIZE = 4093
#Aplication configuration
SERVER_NAME = None
APPLICATION_ROOT = '/'
PREFERRED_URL_SCHEME = 'http'
MAX_CONTENT_LENGTH = None
#Json configuration
JSON_AS_ASCII = True
JSON_SORT_KEYS = True
JSONIFY_PRETTYPRINT_REGULAR = False
JSONIFY_MIMETYPE = 'application/json'
#DataBaseConfiguration
url = 'localhost'
port = '27017'
database = 'test'
MONGO_URI = "mongodb://"+url+":"+port+"/"+database