from flask import Flask, render_template
app = Flask(__name__)

stuff = {"clan":"xxx",
        "rank":5,
        "members":3,
        "trophies": 10,
        "description": "a description"}

memList = ["fred", "Bob", "Steve"]

@app.route('/')
def index(stuff = stuff, memList=memList):
   return render_template('index.html', infos=stuff, members=memList)

@app.route('/user/<user>')
def userRender(user):
   return render_template('user.html', user = user)

if __name__ == '__main__':
   app.run(debug = True)