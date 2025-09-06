import requests
from bs4 import BeautifulSoup

response = requests.get('https://reddit.com/r/ProgrammerHumor')
soup = BeautifulSoup(response.content, 'html.parser')

# allPosts = soup.find_all('shreddit-post')
print(soup)
# print(response.content.__sizeof__())
# print(soup.__sizeof__())
# for post in allPosts:
#     print(post.get('post-title'), post.get('content-href'))
