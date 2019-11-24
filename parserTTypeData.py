import requests
from bs4 import BeautifulSoup
import re
th = re.compile(r"<th>([а-яё\s]+)</th>", re.I)
assotiation = re.compile(r"<td>([а-яё\s]+)</td>", re.I)
prioritet = re.compile(r'<td[\d\w\s=""]*>([\d]+)</td>', re.I)
tdCode = re.compile(r'<td><code>(.*)</code></td>')
typeOperatorCode = re.compile(r'<td><a.*><code>(.*)</code></a></td>', re.I)
typeOperatorLinkStr = re.compile(r'<td><a.*>(.*)</a></td>', re.I)
r = requests.get("https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Operators/Operator_Precedence")
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find_all('tbody')[0]
stringTable = table.find_all('tr')
print(stringTable)
table = [];
for i in range(0, len(stringTable)):
	if i == 0:
		strTable = stringTable[i].find_all('th')
		#print(reg.findall(strTable))
		strTable = ''.join(str(i) for i in strTable)
		strTableCaption = th.findall(strTable)
		table.append(strTableCaption[0].ljust(20))
		table.append(strTableCaption[1].center(70))
		table.append(strTableCaption[2].center(30))
		table.append(strTableCaption[3].center(10))
		table.append('\n')
	else:
		strTable = stringTable[i].find_all('td')
		strTable = ''.join(str(i) for i in strTable)
		#Приоритет
		if prioritet.search(strTable):
			prioritetText = prioritet.findall(strTable)
			prioritetStr = ''.join(str(i) for i in prioritetText)
		#Столбец конкретных операторов
		if tdCode.search(strTable):
			tdCodeText = tdCode.findall(strTable)
			tdCodeStr = ''.join(str(i) for i in tdCodeText)
			tdCodeStr = tdCodeStr.replace('&lt;', '<')
			tdCodeStr = tdCodeStr.replace('&gt;', '>')
			tdCodeStr = tdCodeStr.replace('&amp;', '&')
		#Столбец ассоциаций
		if assotiation.search(strTable):
			assotiationText = assotiation.findall(strTable)
			assotiationStr = ''.join(str(i) for i in assotiationText)
		#Столбец с типом операторов
		if typeOperatorCode.search(strTable):
			typeOperatorCodeText = typeOperatorCode.findall(strTable)
			typeOperatorStr = ''.join(str(i) for i in typeOperatorCodeText)
			
		if typeOperatorLinkStr.search(strTable):
			typeOperatorLinkText = typeOperatorLinkStr.findall(strTable)
			typeOperatorLinkString = ''.join(typeOperatorLinkText)
		table.append(prioritetStr.ljust(20, ' '))
		table.append((typeOperatorStr+typeOperatorLinkString).center(70, ' '))
		table.append(assotiationStr.center(30, ' '))
		table.append(tdCodeStr.center(10, ' '))
		table.append('\n')
with open('operator.txt', 'w') as operator:
	operator.write(''.join(table))
input()
