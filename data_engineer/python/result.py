import requests
import pdb
from collections import defaultdict

response_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
response_comments = requests.get('http://jsonplaceholder.typicode.com/comments')

# Проверяем успешность запроса
if response_posts.status_code == 200 and response_comments.status_code == 200:
    # Получаем JSON из ответа
    posts = response_posts.json()
    comments = response_comments.json()

    # Создаем словарь для хранения количества комментариев к постам каждого п    user_posts = defaultdict(list)ользователя
    user_comments = defaultdict(list)
    result = {}
    
    for comment in comments:
        user_comments[comment["postId"]].append(comment)


    for post in posts:
        user_id = post["userId"]
        total_comments = len(user_comments.get(post["id"], []))
        arr = result.get(user_id)

        if arr is None:
          new_arr = []
          new_arr.append(total_comments)
          result[user_id] = new_arr
        else:
          result[user_id].append(total_comments)

    for user, value in result.items():
        total = sum(value)
        count = len(value)
        average = total / count
        print(f"Среднее количество комментариев для пользователя {user}: {average}")
   
else:
    print("Ошибка при выполнении запроса")
