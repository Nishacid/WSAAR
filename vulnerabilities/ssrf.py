#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

from termcolor import colored

# Check for SSRF
def ssrf(host, session):
    r = session.post(f"https://{host}.web-security-academy.net/product/stock", data={
        'sotckApi': 'ssrf' 
    })
    if r.status_code == 400:
        print(colored("[+] Possible SSRF due to product stock checking on /product/stock", "green"))

# XXE or SSRF
def xxe_or_ssrf(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/resources/js/stockCheck.js")
    if r.status_code == 200:
        print(colored("[+] Possible SSRF or XXE due to product stock checking with javascript on /resources/js/stockCheck.js", "green"))
