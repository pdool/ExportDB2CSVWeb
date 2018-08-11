#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

import pymysql


class MySQL(object):
    '''
    MySQL
    '''

    def setDayStr(self, dayStr):
        self.dayStr = "'" + dayStr + "'"

    def __init__(self, dbIp, dbPort, dbName, logDBName, dbUserName, dbPwd):
        """MySQL Database initialization """
        self.db = dbName
        self.logdb = logDBName
        # server = SSHTunnelForwarder(
        #     ssh_address_or_host=('118.89.188.233', 528),  # B机器的配置
        #     ssh_password="KNL2QvVDAuTgtE3B",
        #     ssh_username="root",
        #     local_bind_address=('127.0.0.1', 3306),  # 绑定的端口
        #     remote_bind_address=('10.66.220.202', 3306))
        # # 代理远程的端口
        # server.start()
        # self.conn = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
        #                             port=3306,
        #                             user='root',
        #                             passwd='SPQ7C7ZR4yvz6Q^^',
        #                             db='unity3dm_cn_cn_db341000000',
        #                             charset='utf8')
        self.conn = pymysql.connect(host=str(dbIp),
                                    port=int(dbPort),
                                    user=dbUserName,
                                    passwd=str(dbPwd),
                                    db=dbName,
                                    charset='utf8')
        # self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        self.cursor = self.conn.cursor()

    def query(self, sql):
        """  Execute SQL statement """

        try:
            self.conn.autocommit(False)
            sql = self.replaceSql(sql)
            self.cursor.execute(sql)

            self.conn.commit()
        except  Exception as e:
            print("出现问题" + str(sql))

        "done"
        # t = self.conn.store_result()
        # (field_info) =  t.describe()
        # print(field_info)
        return sql, self.cursor.fetchall()

    def show(self):
        """ Return the results after executing SQL statement """
        return self.cursor.fetchall()

    def __del__(self):
        """ Terminate the connection """
        self.cursor.close()
        self.conn.close()

    def replaceSql(self, sql):
        now = datetime.datetime.now()
        y = now.strftime('%Y')
        m = int(now.strftime('%m'))
        dateStr = y + "_" + str(m)
        if "{db.}" in sql:
            sql = sql.replace("{db.}", self.db)
        if "{logdb.}" in sql:
            sql = sql.replace("{logdb.}", self.logdb)
        if "{date}" in sql:
            sql = sql.replace("{date}", dateStr)
        if "{dayStr}" in sql:
            sql = sql.replace("{dayStr}", self.dayStr)
        return sql


if __name__ == '__main__':
    now = datetime.datetime.now()
    y = now.strftime('%Y')
    m = int(now.strftime('%m'))
    dateStr = y + "_" + str(m)
    print(dateStr)
