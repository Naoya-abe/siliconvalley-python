import requests

r = requests.get('http://127.0.0.1:5000/employee/naoya')
print(r)

r = requests.post(
    'http://127.0.0.1:5000/employee', data={'name': 'naoya'}
)
print(r.text)

r = requests.put(
    'http://127.0.0.1:5000/employee', data={'name': 'naoya', 'new_name': 'abe'}
)
print(r.text)

r = requests.delete(
    'http://127.0.0.1:5000/employee', data={'name': 'abe'}
)
print(r.text)
