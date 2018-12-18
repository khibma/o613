
import json
import requests
import datetime

class clash(object):

    def __init__(self, token, clanID):
        self.token = token
        self.clanID = "%23"+clanID
        self.baseURL = "https://api.clashroyale.com/v1"
        self.headers = headers = {'authorization': self.token,
                                 'Accept': "application/json"}
        self.updateTime = datetime.datetime.now()

        self.clanInfo = self.getClanInfo()
        self.clanName = self.clanInfo['name']

    def getClanInfo(self):

        clanURL = "{}/clans/{}".format(self.baseURL, self.clanID)
        r = requests.get(clanURL, headers=self.headers)

        return r.json()

    def clanWarLog(self):
        clanWarURL = "{}/clans/{}/warlog".format(self.baseURL, self.clanID)
        r = requests.get(clanWarURL, headers=self.headers)

        return r.json()

    def getPlayerInfo(self, playerID):
        playerID = playerID.strip("#")
        playerURL = "{}/players/%23{}".format(self.baseURL, playerID)
        r = requests.get(playerURL, headers=self.headers)

        return r.json()

    def getUpcomingChests(self, playerID):
        playerID = playerID.strip("#")
        uchestsURL = "{}/players/%23{}/upcomingchests".format(self.baseURL, playerID)
        r = requests.get(uchestsURL, headers=self.headers)

        return r.json()
    
    def getBattleLog(self, playerID):
        playerID = playerID.strip("#")
        battleURL = "{}/players/%23{}/battlelog".format(self.baseURL, playerID)
        r = requests.get(battleURL, headers=self.headers)

        return r.json()

    def getCards(self):

        cardsURL = "{}/cards".format(self.baseURL)
        r = requests.get(cardsURL, headers=self.headers)

        return r.json()

    def topClanWars(self, location='57000047'):
        p = {'limit': 300}
        topClanWarURL = "{}/locations/{}/rankings/clanwars".format(self.baseURL, location)
        r = requests.get(topClanWarURL, headers=self.headers, params=p)

        return r.json()

    def top300Clans(self, location='57000047'):
        p = {'limit': 300}
        topClanURL = "{}/locations/{}/rankings/clans".format(self.baseURL, location)
        r = requests.get(topClanURL, headers=self.headers, params = p)

        return r.json()

    def _saveJSONFile(self, f, j):
        ''' take a [f]ile location and [j]son and save to disk '''
        with open(f, 'w') as outfile:
            json.dump(j, outfile)


def go():
    import configparser
    import os, sys
    config = configparser.ConfigParser()
    config.read(os.path.join(sys.path[0],"settings.ini"))
    token = config.get("CLASH", "localtoken")    
    clanID = config.get("CLASH", "clanID")    

    CR = clash(token, clanID)

    print(CR.clanInfo)

if __name__ == "__main__":

    go()
