import requests
def determine_smartest(heroes):
    dict_intelligence = {}
    for hero in heroes:
        url_id = f"https://superheroapi.com/api/2619421814940190/search/{hero}"
        resp = requests.get(url_id).json()
        iq = resp["results"]
        dict_intelligence[int(iq[0]['powerstats']["intelligence"])] = hero
    print(f"Самый умный супергерой: {dict_intelligence[max(dict_intelligence)]}")
determine_smartest(["Hulk", "Captain America","Thanos"])
