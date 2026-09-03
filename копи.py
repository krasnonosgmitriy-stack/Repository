import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
jsons = response.json()

for post in jsons:
    print(f"Id: {post['id']} : {post['title']}")