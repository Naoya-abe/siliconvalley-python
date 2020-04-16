import requests

# r = requests.post(
#     'http://127.0.0.1:5000/post', data={'username': 'mike'}
# )

r = requests.put(
    'http://127.0.0.1:5000/post', data={'username': 'mike'}
)

# r = requests.delete(
#     'http://127.0.0.1:5000/post', data={'username': 'mike'}
# )

print(r.text)
