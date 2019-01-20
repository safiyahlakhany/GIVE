from flask import Flask, render_template, request, url_for, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'give'
app.config['MONGO_URI'] = 'mongodb://saadiak2:saadia99@ds161804.mlab.com:61804/give'

mongo = PyMongo(app)
@app.route('/my_request', methods= ['POST', 'GET'])
def my_request():
    if request.method == 'POST':
        shelters = mongo.db.Homeless_shelters
        shelters.insert({'org': request.form.get('org', ''), 'email': request.form.get('email',''),
                         'zcode': request.form.get('zcode', ''), 'category': request.form.get('category','')})
        return render_template("Succeeded.html")
    else:
        return render_template("request.html")


@app.route('/donate', methods =['POST', 'GET'])
def donate():
    shelters = mongo.db.Homeless_shelters
    if request.method == 'POST':
        zipcode = request.form.get('zipcode','')
        category = request.form.get('category','')
        check = list()
        for doc in shelters.find({}):
          if doc['category'] == category:
            check.append((doc['org'], doc['email'], doc['zcode'], doc['category']))
            
          check = sorted(check, key= lambda y:y[0])
          
          
          
        
        
        return render_template("donation_options.html", check = check)
    else:     
        return render_template("donate.html")

@app.route('/')
def index():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)
    

#collection_test = mongo.db.test

#print(collection_test.find_one())
