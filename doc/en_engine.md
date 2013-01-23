有道词典英文解析引擎
======

### original_query
说明: 请求查询字段    
类型: string    

### return_phrase
说明: 返回查询字段    
类型: string    
	
### phonetic_symbol    
说明: 音标    
类型: string    
	
### cn_translation    
说明: 中文翻译    
类型: list    

### word_forms()    
说明: 其他格式变形          
类型: 返回 dict    
格式: {'比较级': 'freer', '现在分词': 'freeing', '最高级': 'freest', '过去分词': 'freed', '过去式': 'freed'}

	mydictionary =  en_dictionary("free")    
	word_forms = mydictionary.word_forms()    
	for x in word_forms.keys():    
		print x + ":" + word_forms[x]


### example_sentence()
说明: 网络例句       
类型: 返回 dict      
格式: {例句1: 例句1翻译, 例句2: 例句2翻译, 例句3: 例句3翻译}    

	example_sentences = mydictionary.example_sentence()
    for x in example_sentences.keys():
        print x
        print example_sentences[x] + "\n"     
		
### yodao_link    
说明: 有道搜索链接    
类型: string    

### speak_link    
说明: 发音链接    
类型: file/mp3    

### speak()
说明: 发音
