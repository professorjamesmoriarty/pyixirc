#!/usr/bin/python
"""The script searches ixirc.com and parases
the simple json output"""

import sys
import json
import requests
import argparse


class termcolors:
    """Asign some cheap color output for the shell."""
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
    parser = argparse.ArgumentParser(description='Simple cli search for ixirc',
                                     epilog="Made by ShaggyTwoDope")
    parser.add_argument('-V',
                        '-v',
                        '--version',
                        action='version',
                        version='%(prog)s ' + "0.1")
    parser.add_argument('-s',
                        '--searchterm',
                        type=str,
                        help='search string',
                        required=True,
                        default=None)
    parser.add_argument('-c',
                        '--chanid',
                        type=str,
                        help='channel id, see list:',
                        required=False)
    parser.add_argument('-r',
                        '--reverse',
                        action='store_true',
                        help='reverse order',
                        required=False)
    parser.add_argument('-p',
                        '--page',
                        type=str,
                        help='page number',
                        required=False,
                        default=0)
    args = parser.parse_args()
    searchterm = args.searchterm
    chanid = args.chanid
    page = args.page
    reverse = args.reverse
    # conflictdate = args.chanid, args.page
    # if all(conflictdate):
    #     sys.exit('Conflict in options: can not use \
    #             page option with chanid.')
    if chanid == "mg":
        chanid = 92
    elif chanid == "elite":
        chanid = 275
    return searchterm, chanid, page, reverse


searchterm, chanid, page, reverse = get_args()


def do_search():
    searches = requests.get("https://ixirc.com/api/?q=%s&cid=%s&pn=%s" %
                            (searchterm, chanid, page)).json()
    jsondata = json.loads(str(searches).replace("'", '"'))
    jsons = jsondata['results']
    return jsons


def print_search():
    for item in reversed(do_search()):
        title = item['name']
        packn = item['n']
        botn = item['uname'] if "uname" in item else None
        chan = item['cname'] if "cname" in item else None
        netw = item['nname'] if "nname" in item else item['naddr'] if "naddr" in item else None
        size = item['szf'] if "szf" in item else None

        if title and packn and botn and chan and netw:
            print(termcolors.RED + title + termcolors.GREEN + " from", chan,
                  termcolors.BLUE + "on", netw + termcolors.ENDC)
            print(termcolors.RED + size + termcolors.YELLOW + " /msg", botn,
                  "xdcc send", packn, termcolors.ENDC)
            print("---------------------------------------------")


def print_pageinfo():
    for item in do_search():
        results = item['c']
        pagecount = item['pc']
        print(termcolors.RED + results + termcolors.GREEN + " results",
              termcolors.BLUE + "on total of ", pagecount + termcolors.ENDC)
        print("---------------------------------------------")


def main():
    try:
        print_search()
    except KeyError:
        print("No Result Found")


if __name__ == '__main__':
    main()
