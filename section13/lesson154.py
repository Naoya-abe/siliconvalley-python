"""
urllibを使いやすくした3rd partyライブラリ
"""

import requests

payload = {"key1": "value1", "key2": "value2"}

# get
# r = requests.get('http://httpbin.org/get', params=payload)

# get(timeout)
r = requests.get('http://httpbin.org/get', params=payload, timeout=1)

# post
# r = requests.post('http://httpbin.org/post', data=payload)

# put
# r = requests.put('http://httpbin.org/put', data=payload)

# delete
# r = requests.delete('http://httpbin.org/delete', data=payload)

print(r.status_code)
print(r.text)
print(r.json())
