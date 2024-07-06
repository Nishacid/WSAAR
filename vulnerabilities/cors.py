#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

from termcolor import colored

# Check for cors subdomain1
def cors_subdomains(host, session):
    subdomain = f"stock.{host}.web-security-academy.net"
    r = session.get(f"http://{subdomain}/?storeId=1&productId=1")
    if r.status_code == 200:
        print(colored(f"[*] Possible CORS vulnerability due to a trusted subdomain on {subdomain}","green"))
