import json
import requests

url = "http://ixirc.com/api/?q="
search = "linux"
chanid = "92"


class tcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_search():
    weathers = requests.get("http://ixirc.com/api/?q=%s&cid=%s" % (search,
                            chanid)).json()
    jsonData = json.loads(str(weathers).replace("'", '"'))
    jsons = jsonData['results']
    for er in jsons:
        title = er['name']
        packn = er['n']
        botn = er['uname']
        chan = er['cname']
        netw = er['naddr']
        size = er['szf']
        print(tcolors.RED + title + tcolors.GREEN + " from", chan,
              tcolors.BLUE + "on", netw + tcolors.ENDC)
        print(tcolors.RED + size + tcolors.YELLOW + " /msg",
              botn, "xdcc send", packn)

print_search()
