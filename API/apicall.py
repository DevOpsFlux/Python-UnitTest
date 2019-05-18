# -*- coding: utf-8 -*- 

import requests
import json

def main():

	pool_id = ""
	size=20
	
	# [{"Name":"Test Data One","State":"Ready","Enabled":"True","LastTaskResult":"0x1","NextRunTime":"2019-05-18 16:29:32","RunningTime":"0"}
	#,{"Name":"Test Data Three,"State":"Ready","Enabled":"True","LastTaskResult":"0x0","NextRunTime":"2019-05-18 16:29:00","RunningTime":"0"}]
	url = "http://dev.flux.com/Batch/GateAPI/JsonAPI.aspx?p=http://127.0.0.1:10080/TaskWeb/Index"
	querystring = {"p1":"Play","p2":"list","p3":""}


	print(querystring)
	response = requests.request("GET", url, params=querystring)

	print(response.text)


	    #f = open(r"D:\Batch\Python\UnitTest\apicall.log", 'a+', encoding="utf-8")
	    #f = open(r"D:\Batch\Python\UnitTest\apicall.log", 'a+', encoding="utf-8")
	    #f.write(json.dumps(response , ensure_ascii=False))
	    #f.write(response )
	    #f.write('\n')
	    #f.close()


if __name__ == "__main__":
	main()

