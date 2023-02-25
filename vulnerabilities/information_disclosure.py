#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
from termcolor import colored

# Check for Information Disclosure .git exposed
def git_exposed(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/.git")
    if r.status_code == 200:
        print(colored("[+] Highly possible disclosure of sensitive information through .git", "green"))

# Check for trace method
def trace_admin(host, session):
    r = session.request('trace', f"https://{host}.web-security-academy.net/admin")
    if r.status_code == 200:
        print(colored("[+] Disclosure of sensitive information highly possible with the path /admin accepting the TRACE method", "green"))

# Check for debug page
def debug_page(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/cgi-bin/phpinfo.php")
    if r.status_code == 200:
        print(colored("[+] Highly possible disclosure of sensitive information by the debug page /cgi-bin/phpinfo.php", "green"))

# Check for error page
def error_page(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/product?productId='exemple'")
    if r.status_code == 500:
        print(colored("[+] Highly possible disclosure of sensitive information on an error page (stacktrace)", "green"))