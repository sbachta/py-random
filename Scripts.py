import requests
from bs4 import BeautifulSoup

response = requests.get('https://reddit.com/r/StarWars')
soup = BeautifulSoup(response.content, 'html.parser')

allPosts = soup.find_all('shreddit-post')

for post in allPosts:
    print(post.get('post-title'), post.get('content-href'))
