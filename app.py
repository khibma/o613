from flask import Flask, render_template
app = Flask(__name__)

stuff = {"clan":"xxx",
        "rank":5,
        "members":3,
        "trophies": 10,
        "description": "a description"}

memList = ["fred", "Bob", "Steve"]

import configparser
import os, sys
config = configparser.ConfigParser()
config.read(os.path.join(sys.path[0],"clash/settings.ini"))
token = config.get("CLASH", "token")    
clanID = config.get("CLASH", "clanID")    

sys.path.append(os.path.join(sys.path[0], "clash"))
import clash
CR = clash.clash(token, clanID)
print(CR)

@app.route('/')
def index(memList=memList, everything=CR):
   return render_template('index.html', members=memList, everything=CR.clanInfo)

@app.route('/user/<user>')
def userRender(user):
   return render_template('user.html', user = user)

if __name__ == '__main__':

   app.run(debug = True)