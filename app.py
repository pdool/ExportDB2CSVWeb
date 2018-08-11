from flask import Flask, render_template, request, jsonify

from bojoy.main import dealOneFile, dealAllFiles, dealSqlMap, dealFiles
from bojoy.util.FileOperation import FileOp

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        dbIp = request.form['dbIp']
        dbPort = request.form['dbPort']
        dbName = request.form['dbName']
        logDBName = request.form['logDBName']
        userName = request.form['userName']
        pwd = request.form['pwd']
        dayStr = request.form['dayStr']
        sqls = request.files.getlist("sqls")
        sqlMap = dealSqlMap(sqls)
        config = request.files["config"]
        links = dealFiles(dbIp, dbPort, dbName, logDBName, userName, pwd, dayStr, sqlMap,config)


        # fileLength = len(request.form)
        # files = []
        # rows = (fileLength - 6)//3 + 1
        # for i in range(1,rows):
        #     upSql = request.files["file"+str(i)]
        #     cols = request.form['colsName' + str(i)]
        #     csvName = request.form['csvName' + str(i)]
        #     sql = upSql.read().decode('utf-8')
        #     # dealOneFile(dbIp,dbPort,dbName,logDBName,userName,pwd)
        #     files.append({"sqlName":csvName,"sql":sql,"colsName":cols})
        #
        # links = dealAllFiles(dbIp,dbPort,dbName,logDBName,userName,pwd,dayStr,files)
        return jsonify({'result': links})

    return render_template("upload.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
