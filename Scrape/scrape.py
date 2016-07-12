from bs4 import BeautifulSoup
from django.utils.text import slugify
import requests
import random
import csv

user_agents = [  
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19',
 	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'
]

def get_requests(url):
	headers={'User-Agent':user_agents[random.randint(0,8)]}
	r = requests.get(url, headers=headers)
	# r = requests.get(url)
	html = r.text.encode('utf8')
	soup = BeautifulSoup(html, 'lxml')
	ex = soup.find('table', attrs={'class':"sortable"})
	table_rows = ex.findAll('tr')
	final_csv_row = []
	for table_row in table_rows[1:]:
		row = table_row.findAll('td')
		hero_name = row[1].text
		win_rate = row[2]['data-value']
		final_csv_row.append(dict(name=hero_name, win_rate=win_rate))
	final_csv_row = sorted(final_csv_row)
	print "For Phantom Assassin : "
	for row in final_csv_row:
		print row['name'], row['win_rate']
		
def main():
	base_url = "http://www.dotabuff.com/heroes/"
	hero_name = "Phantom Assassin"
	final_url  = base_url + slugify(hero_name) + "/matchups"
	get_requests(final_url)
	# get_requests("http://localhost:8000/test.html")

if __name__ == '__main__':
	main()
