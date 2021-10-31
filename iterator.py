import requests
urls=('http://wiki.com', 'http://oreilly.com', 'http://twitter.com',
       'http://rtf.urfu.ru')

for resp in [requests.get(url) for url in urls]:
	print(len(resp.content), resp.status_code, resp.url, sep='->')

cont=requests.get('https://rtf.urfu.ru').content
with open('content.txt', mode='w') as f:
    print(cont,file=f)
