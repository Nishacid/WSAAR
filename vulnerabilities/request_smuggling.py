#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
from termcolor import colored

# Check for Request Smuggling
def request_smuggling_ua(host, session):
    headers = {
        'User-Agent': 'smuggy_request'
    }
    r = session.get(f"https://{host}.web-security-academy.net/post?postId=1", headers=headers)
    if 'smuggy_request' in r.text:
        print(colored("[+] Highly Possible Request Smuggling due to reflected User-Agent in post comment", "green"))

def request_smuggling_http2(host, session):
    scripts = ["resources/js/analyticsFetcher.js"]
    for path in scripts:
        r = session.get(f"https://{host}.web-security-academy.net/{path}")
        if r.status_code == 200:
            print(colored(f"[+] Possible Request Smuggling HTTP/2 due to analytics script on /{path}", "green"))