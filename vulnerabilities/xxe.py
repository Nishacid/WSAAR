#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

from termcolor import colored

# Check for XXE
def xxe_check(host, session):
    data = {
        b'<?xml version="1.0" encoding="UTF-8"?>'
    }
    headers = {
        'Content-Type': 'application/xml'
    }
    r = session.post(f"https://{host}.web-security-academy.net/product/stock", data=data, headers=headers)
    response = r.text
    if 'XML parser' in response:
        print(colored("[+] Highly Possible XXE due to XML Error Parsing on product check", "green"))
