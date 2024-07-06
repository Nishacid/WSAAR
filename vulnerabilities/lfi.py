#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

from termcolor import colored

# Check for Path Traversal
def search_lfi(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/image?filename=59.jpg")
    if r.status_code == 200:
        print(colored("[+] Highly Possible Path Traversal through /image?filename=X", "green"))
    elif r.status_code == 400:
        print(colored("[+] Possible Path Traversal through /image?filename=X", "green"))