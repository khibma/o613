from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

class ReusableForm(Form):
    pid = TextField('PLayerID:', validators=[validators.required()])
 

import configparser
import os, sys
from sys import platform
import datetime
config = configparser.ConfigParser()
config.read(os.path.join(sys.path[0],"clash/settings.ini"))
tokenLocal = config.get("CLASH", "tokenLocal")    
tokenAzure = config.get("CLASH", "tokenAzure")    
clanID = config.get("CLASH", "clanID")    

sys.path.append(os.path.join(sys.path[0], "clash"))
import clash
t = tokenAzure if platform != "win32" else tokenLocal

CR = clash.clash(t, clanID)
print(CR)

def fixTime(t):   
    return (t - datetime.timedelta(hours=5)).strftime("%Y-%m-%d %H:%M")

@app.route('/')
def index(everything=CR):

   if (datetime.datetime.now() - CR.updateTime).seconds > 120:
        CR.clanInfo = CR.getClanInfo()        
        CR.updateTime = datetime.datetime.now()
   return render_template('index.html', everything=CR.clanInfo, t=CR.token, updatetime=fixTime(CR.updateTime))

@app.route('/user/', methods=['GET', 'POST'])
@app.route('/user/<u>', methods=['GET'])
def userRender(u=None):
   
   playerInfo = 9999
   uchest = {'items':[]}
   warInfo = {'warWins': 0, 'warLose': 0, 'collectWin': 0, 'collectLose': 0}

   if not u:
      form = ReusableForm(request.form)
      if request.method == 'POST':
         u = request.form['pid']
         print(u)

   #if form.validate():
   #   playerInfo = CR.getPlayerInfo(searchPid)

   if u:
      playerInfo = CR.getPlayerInfo(u)
      uchest = CR.getUpcomingChests(u)
      battle = CR.getBattleLog(u)

      for b in battle:
          if b['type'] == "clanWarCollectionDay":
            if b['team'][0]['crowns'] > b['opponent'][0]['crowns']:
              warInfo['collectWin'] +=1
            else:
              warInfo['collectLose'] +=1
          if b['type'] == "clanWarWarDay":
            if b['team'][0]['crowns'] > b['opponent'][0]['crowns']:
              warInfo['warWins'] +=1
            else:
              warInfo['warLose'] +=1
    
   return render_template('user.html', pi = playerInfo, w=warInfo, chst=uchest['items'], clanName=CR.clanName, updatetime=fixTime(CR.updateTime))

if __name__ == '__main__':

   #app.run(debug = True)
   app.run(host='0.0.0.0')