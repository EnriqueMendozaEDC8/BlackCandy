#Import Libraries
from app import app
from flask_pymongo import PyMongo
import core.jsonEncoder as je

#Start Mongo on app
mongo = PyMongo(app)
app.json_encoder = je.JSONEncoder

#   DO: FirstName LastName
#   Verify of the user exist
#   @param Usernem,Password
#   @return json Object with data of user
def index(userName,password):
    try:
        user = mongo.db.users.find_one_or_404({"username":userName,"pass":password})
        return user
    except:
        return "you have an error pls configure your db connection"