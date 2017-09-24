'''https://www.dataquest.io/blog/web-scraping-tutorial-python/

Initial script when working through dataquest. I think a notebook is more effective for learning though. 
'''

import requests 
from bs4 import BeautifulSoup

page = requests.get("http://insideairbnb.com/get-the-data.html")
page

page.status_code
page.content

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())


list(soup.children)
[type(item) for item in list(soup.children)] 
html = list(soup.children)[2]
list(html.children)
body = list(html.children)[3]
list(body.children)

p = list(body.children)[1]
p.get_text()


soup.find_all('p'))
soup.find_all('p', class_='outer-text')
soup.find_all(class_="outer-text")
soup.find_all(id="first")
soup.select("div p")


'''tims code for working with an API
requests.get('https://api.pinterest.com/v1/users/ksamanthalee/?access_token=AUAQamNd1y6Fu2v7GUwnYyAQAyrJFOc0-XNudR9EV94YAEA72AAAAAA&fields=first_name%2Cid%2Clast_name%2Curl%2Caccount_type%2Cbio%2Ccounts%2Ccreated_at%2Cimage%2Cusername')
<Response [200]>
requests.get('https://api.pinterest.com/v1/users/ksamanthalee/?access_token=AUAQamNd1y6Fu2v7GUwnYyAQAyrJFOc0-XNudR9EV94YAEA72AAAAAA&fields=first_name%2Cid%2Clast_name%2Curl%2Caccount_type%2Cbio%2Ccounts%2Ccreated_at%2Cimage%2Cusername').text
'{"data": {"username": "ksamanthalee", "bio": "", "first_name": "Samantha", "last_name": "Lee", "account_type": "individual", "url": "https://www.pinterest.com/ksamanthalee/", "created_at": "2014-05-22T04:40:16", "image": {"60x60": {"url": "https://s-media-cache-ak0.pinimg.com/avatars/ksamanthalee_1472246553_60.jpg", "width": 60, "height": 60}}, "counts": {"pins": 84, "following": 22, "followers": 8, "boards": 6}, "id": "490540721820952543"}}'
import json
resp = requests.get('https://api.pinterest.com/v1/users/ksamanthalee/?access_token=AUAQamNd1y6Fu2v7GUwnYyAQAyrJFOc0-XNudR9EV94YAEA72AAAAAA&fields=first_name%2Cid%2Clast_name%2Curl%2Caccount_type%2Cbio%2Ccounts%2Ccreated_at%2Cimage%2Cusername').text
json.loads(resp)
{'data': {'username': 'ksamanthalee', 'bio': '', 'first_name': 'Samantha', 'last_name': 'Lee', 'account_type': 'individual', 'url': 'https://www.pinterest.com/ksamanthalee/', 'created_at': '2014-05-22T04:40:16', 'image': {'60x60': {'url': 'https://s-media-cache-ak0.pinimg.com/avatars/ksamanthalee_1472246553_60.jpg', 'width': 60, 'height': 60}}, 'counts': {'pins': 84, 'following': 22, 'followers': 8, 'boards': 6}, 'id': '490540721820952543'}}
>>> obj = json.loads(resp)
'''