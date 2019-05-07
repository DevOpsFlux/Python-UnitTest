# -*- coding: utf-8 -*- 
'''
    mssql 접속 테스트
'''
import os, sys, string
import pymssql
import json

def main() :

    conn = pymssql.connect(server='DBServerIP', user='UserID', password='Pwd', database='DBName', login_timeout=15, charset='UTF-8', as_dict=False, host='', appname=None, port='1433')
    cursor = conn.cursor()
    
    ## inline query
    #cursor.execute('SELECT top 3 * FROM tbl_Coded')
    # row = cursor.fetchone()
    # while row:
    #     print("%s %s" % (row[0], row[1]))
    #     row = cursor.fetchone()
    # conn.close()

    ## procedure
    cursor.callproc('Proc_GetCodeName', ('00001'))
    for row in cursor:
        print("Code=%s, Name=%s" % (row[0], row[1]))

       	codeinfo = {
            'Code' : row[0],
            'CodeName' : row[1]
        }

    conn.close()
    
    f = open("C:\Python37\MyModule\Mssql/test.log", 'a+', encoding="utf-8")
    f.write(json.dumps(codeinfo, ensure_ascii=False))
    f.write('\n')
    f.close()

    # with open("test", "a") as fout:
	#     fout.write(json.dumps(codeinfo))
	#     fout.write('\n')
    
    print(json.dumps(codeinfo, ensure_ascii=False))
    
    #print "$s"conn
    #cur = conn.cursor()
    #print cur
    #pymssql.connect(server='.', user='', password='', database='', timeout=0, login_timeout=60, charset='UTF-8', as_dict=False, host='', appname=None, port='1433', conn_properties, autocommit=False, tds_version='7.1') 
    
    
if __name__ == "__main__" :
    main()