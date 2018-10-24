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

@app.route('/')
def index(everything=CR):

   if (datetime.datetime.now() - CR.updateTime).seconds > 120:
        CR.clanInfo = CR.getClanInfo()        
        CR.updateTime = datetime.datetime.now()
   return render_template('index.html', everything=CR.clanInfo, t=CR.token, updatetime=CR.updateTime.strftime("%Y-%m-%d %H:%M"))

@app.route('/user/', methods=['GET', 'POST'])
@app.route('/user/<u>', methods=['GET'])
def userRender(u=None):
   
   playerInfo = 9999
   uchest = {'items':[]}

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
      #battle = CR.getBattleLog(u)
        
   return render_template('user.html', pi = playerInfo, chst=uchest['items'], clanName=CR.clanName, updatetime=CR.updateTime.strftime("%Y-%m-%d %H:%M"))

if __name__ == '__main__':

   #app.run(debug = True)
   app.run(host='0.0.0.0')