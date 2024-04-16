from flask_restful import Resource

from flask_restful import request
from flask_restful import reqparse

from dbUtil import *

from restapi import *


class Getcyberassets(Resource):
    
    def get(self):
        
        cyberAssetsList = []
        cyberAssets = getCyberAssets()
        
        for i in cyberAssets:
            cyberAssetsList.append(i)
            
        return (cyberAssetsList, 201)

class Getcyberasset(Resource):

    def get(self, primaryid):

        if primaryid != None:
            cyberAsset = getCyberAsset(primaryid)

            return (cyberAsset, 201)
    
        return("ERROR, Asset does not exist", 406)
    
    
class Deletecyberassets(Resource):
    
    def delete(self, primaryid):
        
        print(primaryid)
        if (primaryid != None):
            deleteCyberAssets
            return ("Cyber Asset Deleted", 202)
        
        else:
            return ("ERROR, ASSET DOESN'T EXIST", 406)
    
    