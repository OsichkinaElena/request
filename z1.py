import requests
def determine_smartest():
    dict_intelligence = {}
    list_ = []
    url_hulk = "https://superheroapi.com/api/2619421814940190/332/powerstats/get"
    resp_hulk = requests.get(url_hulk).json()
    dict_intelligence[int(resp_hulk["intelligence"])] = "Hulk"
    url_thanos = "https://superheroapi.com/api/2619421814940190/655/powerstats/get"
    resp_thanos = requests.get(url_thanos).json()
    dict_intelligence[int(resp_thanos["intelligence"])] = "Thanos"
    url_captain_america = "https://superheroapi.com/api/2619421814940190/149/powerstats/get"
    resp_captain_america = requests.get(url_captain_america).json()
    dict_intelligence[int(resp_captain_america["intelligence"])] = "Captain America"
    print(f"Самый умный супергерой: {dict_intelligence[max(dict_intelligence)]}")
determine_smartest()
