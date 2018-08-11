#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import os

from bojoy.util.FileOperation import FileOp
from bojoy.util.MySqlConn import MySQL


def dealAllFiles(dbIp, dbPort, dbName, logDBName, dbUserName, dbPwd, dayStr, files):
    conn = MySQL(dbIp, dbPort, dbName, logDBName, dbUserName, dbPwd)
    conn.setDayStr(dayStr)
    links = []
    for item in files:
        colsName = item["colsName"]
        sqlName = item["sqlName"]
        sql = item["sql"]
        link = dealOneFile(conn, colsName, sqlName, sql, dayStr)
        links.append(link)

    return links



def dealOneFile(conn, colsName, csvName, sql, dayStr):
    csvFile = FileOp(os.getcwd() + "/static", csvName)
    csvFile.addRow(colsName.split(","))
    try:
        sqlResult, r = conn.query(sql)
        for x in r:
            csvFile.addRow(x)
        del csvFile
        # filePath = rootPath + "\\csvs\\SQL\\" + item[2] + dayStr + ".sql"
        # with open(filePath, 'w') as f:
        #     f.write(sqlResult)
        return csvName
    except Exception as e:
        print("出现问题" + str(e))

def dealSqlMap(sqlList):
    ret = {}
    for sqlFile in sqlList:
        sql = sqlFile.read().decode('utf-8')
        sqlName = sqlFile.filename
        ret[sqlName] = sql
    return ret


def readCsvConfig(csvConfig):
    csvConfig.save(os.path.join(os.getcwd() ,csvConfig.filename))
    configList = FileOp.showContent(os.getcwd(), csvConfig.filename)
    os.remove(os.path.join(os.getcwd() ,csvConfig.filename))
    return configList


def dealFiles(dbIp, dbPort, dbName, logDBName, dbUserName, dbPwd, dayStr, sqlMap,csvConfig):
    configList = readCsvConfig(csvConfig)
    conn = MySQL(dbIp, dbPort, dbName, logDBName, dbUserName, dbPwd)
    conn.setDayStr(dayStr)
    links = []
    for i in range(1, len(configList)):
        item = configList[i]
        sqlName = item[2] + ".sql"
        csvName = item[1] + dayStr+ ".csv"
        colsName = item[3]
        link = dealOneFile(conn,colsName,csvName,sqlMap[sqlName],dayStr)
        links.append(link)
    return links