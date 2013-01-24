有道翻译解析引擎    
======    
    
### errorCode    
说明: 返回错误码    
类型: string    
值:    
	* 0 - 正常    
	* 20 - 要翻译的文本过长    
	* 30 - 无法进行有效的翻译      
    * 40 - 不支持的语言类型    
	* 50 - 无效的key    
    
### query    
说明: 请求查询字段    
类型: string    
    
### translation    
说明: 翻译结果    
类型: string    
    
### phonetic    
说明: 音标    
类型: string    
    
### explains    
说明: 中文释义    
类型: list    
    
### web_explains()    
说明: 网络词组    
类型: 返回dict    
格式: {'词组': [中文解释1, 中文解释2, 中文解释3]}    

	myfanyi = fanyi_dictionary("love")
	web_explains = myfanyi.web_explains()
    for explain in web_explains.keys():
		print  "\033[1;36;40m%s\033[0m" %explain
		for value in web_explains[explain]:
            print value
			
