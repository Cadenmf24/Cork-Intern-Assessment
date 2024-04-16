from dbUtil import *

def getCyberAssets(): # Returns all of the cyberAssets, joins serialnumbers
    result = exec_get_all("SELECT name, type, os, serialNumber FROM cyberassets inner join serialnumbers ON cyberassets_id = cyberassets.id")
    return result

def getCyberAsset(primaryId): # reuturns one cyber asset

    result = exec_get_all("SELECT name, type, os, SerialNumber FROM cyberassets inner join serialnumber ON cyberassets_id = cyberassets.id WHERE cyberassets.id = %s", [primaryId])

def deleteCyberAssets(primaryid): # deletes cyber asset
    exec_commit('DELETE FROM cyberassets WHERE id = %s', [primaryid])
    
