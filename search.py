import sys
import json
import requests
import argparse

url = "http://ixirc.com/api/?q="
search = ""
chanid = ""


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


def get_args():
    """get all args"""
    parser = argparse.ArgumentParser(
        description='Simple cli search for ixirc',
        epilog="More info later.")
    parser.add_argument('-V', '-v', '--version', action='version',
                        version='%(prog)s ' + "0.1")
    parser.add_argument(
        '-s', '--search', type=str, help='search string',
        required=False, default=None)
    parser.add_argument(
        '-c', '--chanid', type=str, help='channel id, see list:',
        required=False, default=None)
    parser.add_argument(
        '-p', '--page', action='store_true', help='page number',
        required=False)
    args = parser.parse_args()
    search = args.search
    chanid = args.chanid
    page = args.page
    conflictdate = args.chanid, args.page
    if all(conflictdate):
        sys.exit('Conflict in options: can not use \
                page option with chanid.')
    return search, chanid, page

search, chanid, page = get_args()


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


def main():
    print_search()


if __name__ == '__main__':
    main()
