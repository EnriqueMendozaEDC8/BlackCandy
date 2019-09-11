#Import Libraries
from app import app
from flask import session,redirect,url_for,request,jsonify
#Import Model
import models.indexModel as indexModel

#   DO: FirstName LastName
#   Say hello world
#   @param 
#   @return text "hello world"
@app.route("/")
def index():
    return indexModel.index("myUser","myPassword")
    #return "hello world"

#   DO: FirstName LastName
#   Sum two parametters
#   Method POST,GET
#   @param number,number
#   @return sum of two parametters   
@app.route('/getsum', methods=['POST','GET'])
def get_tasks():
    if request.method == 'GET':
        value1 = request.args.get('value1')
        value2 = request.args.get('value2')
    elif request.method == 'POST':
        value1 = request.json.get('value1')
        value2 = request.json.get('value2')
    try:
        res = int(value1)+int(value2)
        return jsonify({'recta':res})
    except:
        return jsonify({'error':'you need send numbers'})