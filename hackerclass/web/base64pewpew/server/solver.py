import requests
from base64 import b64decode
if __name__ == "__main__":
    url = 'http://localhost:9999'
    password = 'c3VwZXJzZWNyZXQ='.encode()
    params = {'password': b64decode(password)}
    res = requests.get(url=url, params=params)
    res = res.text.split("</html>")[1].strip()
    print(res)
