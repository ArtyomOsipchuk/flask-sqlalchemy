from requests import get, post, put
from pprint import pprint

# pprint(get('http://127.0.0.1:5000/api/news').json())

# pprint(get('http://localhost:5000/api/news/1').json())

# pprint(get('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

# pprint(get('http://localhost:5000/api/news/q').json())

# print(post('http://localhost:5000/api/news').json())
# print(post('http://localhost:5000/api/news',
# json={'title': 'Заголовок'}).json())
# print(post('http://localhost:5000/api/news',
#          json={'title': 'Заголовок',
#                 'content': 'Текст новости',
#                'user_id': 1,
#                 'is_private': False,
#                'is_published': True}).json())

print(put('http://localhost:5000/api/news/3',
          json=[{'title': 'Новый заголовок этой новости',
                 'content': 'Текст новости'}]).json())
