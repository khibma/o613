
import json
import requests

class clash(object):

    def __init__(self, token, clanID):
        self.token = token
        self.clanID = "%23"+clanID
        self.baseURL = "https://api.clashroyale.com/v1"
        self.headers = headers = {'authorization': self.token,
                                 'Accept': "application/json"}

        self.clanInfo = self.getClanInfo()

    def getClanInfo(self):

        clanURL = "{}/clans/{}".format(self.baseURL, self.clanID)
        r = requests.get(clanURL, headers=self.headers)

        return r.json()

    def getPlayerInfo(self, playerID):

        playerURL = "{}/players/%23{}".format(self.baseURL, playerID)
        r = requests.get(clanURL, headers=self.headers)

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
    token = config.get("CLASH", "token")    
    clanID = config.get("CLASH", "clanID")    

    CR = clash(token, clanID)

    print(CR.clanInfo)

if __name__ == "__main__":

    go()
