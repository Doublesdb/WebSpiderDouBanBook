import re

with open('Regular Expression.txt','r',encoding='utf-8') as file_re:
    content = file_re.read()
    STR = r'class="nbg" href="(.*?)".*?src="(.*?)".*?title="(.*?)".*?<div class="pub">\s*(.*?)\/.*?nums">(.*?)</span>.*?<p>(.*?)</p>'
    
    result = re.findall(STR, content, re.S|re.M)
    #print(result)
    
    with open('result.txt', 'w', encoding = 'utf-8') as file_result:
        file_result.seek(0)
        file_result.truncate()
        file_result.write(str(result))
