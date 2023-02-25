#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
from bs4 import BeautifulSoup
from termcolor import colored

# Check for header in response
def web_cache_header(host, session):
    headers = ["X-Cache", "Vary", "Cache-Control"]
    r = session.get(f"https://{host}.web-security-academy.net/")
    for header in headers:
        cache_header = r.headers.get(header)
        if cache_header: 
            print(colored(f"[+] Highly possible Web Cache Poisoning due to {header} Header in response", "green"))

# Check for Tracking script
def web_cache_script(host, session):
    scripts_path = ["resources/js/tracking.js", "js/geolocate.js?callback=en"]
    for script in scripts_path:
        r = session.get(f"https://{host}.web-security-academy.net/{script}")
        if r.status_code == 200:
            print(colored(f"[+] Possible Web Cache Poisoning due to script on /{script}", "green"))

# Check for pragma request 
def web_cache_pragma_header(host, session):
    # does it want to give us the cache key ?
    headers = {
        'Pragma': 'x-get-cache-key'
    }
    r = session.get(f"https://{host}.web-security-academy.net/", headers=headers)
    x_cache_key = r.headers.get('X-Cache-Key')
    if x_cache_key: 
        print(colored(f"[+] Highly possible Web Cache Poisoning due to X-Cache-Key Header in response\n\t [*] Value for / : X-Cache-Key : {x_cache_key}", "green"))