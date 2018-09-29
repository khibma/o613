from flask import Flask, render_template
app = Flask(__name__)


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
   #CI = CR.getClanInfo()
   #print(CI)
   if (datetime.datetime.now() - CR.updateTime).seconds > 120:
        CR.getClanInfo()
        CR.updateTime = datetime.datetime.now()
   return render_template('index.html', everything=CR.clanInfo, t=CR.token, updatetime=CR.updateTime.strftime("%Y-%m-%d %H:%M"))

@app.route('/user/<user>')
def userRender(user):
   playerInfo = CR.getPlayerInfo(user)
        
   return render_template('user.html', user = user, pi = playerInfo, everything=CR, updatetime=CR.updateTime)

if __name__ == '__main__':

   app.run(debug = True)
   #app.run(host='0.0.0.0')