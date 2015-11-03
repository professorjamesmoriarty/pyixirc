#!/usr/bin/python
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
        epilog="Made by shaggy")
    parser.add_argument('-V', '-v', '--version', action='version',
                        version='%(prog)s ' + "0.1")
    parser.add_argument(
        '-s', '--search', type=str, help='search string',
        required=False, default=None)
    parser.add_argument(
        '-c', '--chanid', type=str, help='channel id, see list:',
        required=False, default=None)
    parser.add_argument(
        '-r', '--reverse', action='store_true', help='reverse order',
        required=False)
    parser.add_argument(
        '-p', '--page', type=str, help='page number',
        required=False)
    args = parser.parse_args()
    search = args.search
    chanid = args.chanid
    page = args.page
    reverse = args.reverse
    conflictdate = args.chanid, args.page
    if all(conflictdate):
        sys.exit('Conflict in options: can not use \
                page option with chanid.')
    return search, chanid, page, reverse

search, chanid, page, reverse = get_args()


def print_search():
    searches = requests.get("http://ixirc.com/api/?q=%s&cid=%s&pn=%s" % (search,
                            chanid, page)).json()
    jsonData = json.loads(str(searches).replace("'", '"'))
    jsons = jsonData['results']
    for item in reversed(jsons):
        title = item['name']
        packn = item['n']
        botn = item['uname']
        chan = item['cname']
        netw = item['naddr']
        size = item['szf']
        print(tcolors.RED + title + tcolors.GREEN + " from", chan,
              tcolors.BLUE + "on", netw + tcolors.ENDC)
        print(tcolors.RED + size + tcolors.YELLOW + " /msg",
              botn, "xdcc send", packn, tcolors.ENDC)
        print("---------------------------------------------")


def main():
    try:
        print_search()
    except KeyError:
        print("No Result Found")

if __name__ == '__main__':
    main()
