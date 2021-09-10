from yarl import URL 

url = URL('https://connpass.com/')

print(url / 'explore')
print(url / 'search' % {'q': 'aiohttp'})