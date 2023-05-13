import requests

TOKEN = ""
User_id = ""
text = ""

headers = {
    'authorization': TOKEN,
    'x-device-info': 'Yay 3.2.0 Web (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36)',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

for i in range(150):
        payload = {'comment': [text]}
        res = requests.post("https://api.yay.space/v1/users/reviews/"+ User_id,headers=headers,data=payload)
        print(res,res.text)
