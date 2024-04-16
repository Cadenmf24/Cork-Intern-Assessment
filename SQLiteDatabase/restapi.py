from dbUtil import *

def getCyberAssets():
    result = exec_get_all("SELECT name, type, os, serialNumber FROM cyberassets inner join serialnumbers ON cyberassets_id = cyberassets.id")
    return result
    
    result = exec_get_all('select courses.id, c_number, c_title, c_details, dept_id, department.name, college.name FROM courses inner join department ON department.id = courses.dept_id inner join college ON college.id = department.college_id order by id asc')


def deleteCyberAssets(primaryid):
    exec_commit('DELETE FROM cyberassets WHERE id = %s', [primaryid])
    
