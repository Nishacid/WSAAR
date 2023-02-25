#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
from termcolor import colored

# Check for Business Logic
def business_logic(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/cart")
    if r.status_code == 200:
        print(colored("[+] Highly possible business logic vulnerability due to /cart path", "green"))
