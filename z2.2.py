import json

import requests
def upload(file_list, token_):
    token = token_
    headers = {"Content-Type": "application/json", "Authorization": "OAuth {}".format(token)}
    params = {"path": f"test/test.txt",  "overwrite": True}
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    r = requests.get(url, headers=headers, params=params)
    res = r.json()
    if "href" in res.keys():
        upload_ = requests.put(url=res["href"], data=open(file_list, "rb"), headers=headers, params=params)
    else:
        print("ссылка не получена")
    if upload_.status_code == 201:
        print("Success")
upload("test.txt","AQAAAABWrP_vAADLW4E1JGNgw0CnrfvS9Q-wRGQ")