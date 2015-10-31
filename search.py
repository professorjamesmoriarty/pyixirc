import json
import requests

url = "http://ixirc.com/api/?q="
search = "linux"
network = "92"


def print_search():
    search = "linux"
    weathers = requests.get("http://ixirc.com/api/?q=%s" % (search)).json()
    jsonData = json.loads(str(weathers).replace("'", '"'))
    jsons = jsonData['results']
    for er in jsons:
        title = er['name']
        packn = er['n']
        botn = er['uname']
        print(title)
        print(packn)
        print(botn)

print_search()
