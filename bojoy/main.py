#!/usr/bin/python3
# -*- coding: utf-8 -*-
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


def dealOneFile(conn, colsName, sqlName, sql, dayStr):
    csvFile = FileOp(os.getcwd() + "\\static", sqlName + dayStr + ".csv")
    csvFile.addRow(colsName.split(","))
    try:
        sqlResult, r = conn.query(sql)
        for x in r:
            csvFile.addRow(x)
        del csvFile
        # filePath = rootPath + "\\csvs\\SQL\\" + item[2] + dayStr + ".sql"
        # with open(filePath, 'w') as f:
        #     f.write(sqlResult)
        return sqlName + dayStr + ".csv"
    except Exception as e:
        print("出现问题" + str(e))
