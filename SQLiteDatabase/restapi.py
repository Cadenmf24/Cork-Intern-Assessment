from dbUtil import *

def getCyberAssets():
    result = exec_get_all("SELECT name, type, os, serialNumber FROM cyberassets inner join serialnumber ON cyberassets.id = setialnumber.cyberassets_id")
    return result
    

def deleteCyberAssets(primaryid):
    exec_commit('DELETE FROM cyberassets WHERE id = %s', [primaryid])
    
