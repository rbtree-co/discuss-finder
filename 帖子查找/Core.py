import requests
import sys

_uid = sys.argv[3]
__client_id = sys.argv[4]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "cookie": "_uid=" + _uid + ";__client_id=" + __client_id
}

i = int(sys.argv[1])

while 1:
    response = requests.get(
        "https://www.luogu.com.cn/discuss/" + str(i), headers=headers)
    response.encoding = 'utf-8'
    while response.status_code != 200:
        response = requests.get(
            "https://www.luogu.com.cn/discuss/" + str(i), headers=headers)
    s = response.text
    if s.find(sys.argv[2]) != -1:
        print(i)
    i -= 9
