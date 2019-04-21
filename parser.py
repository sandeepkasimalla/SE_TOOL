import os
import string
import bs4

path = "output/html/"

pages = string.ascii_lowercase

def parse(loc):
	with open(loc) as f:
		data = f.read().replace('\n','')
		soup = bs4.BeautifulSoup(data, "html.parser")
		# div.contents > ul > li
		for item in soup.select(".contents > ul > li"):
			print(item.text)	
		f.close()	

parse(path + 'globals_func.html')
for c in pages[1:]:
	try:
		parse(path + 'globals_func_'+c+'.html')
	except:
		a = 6
