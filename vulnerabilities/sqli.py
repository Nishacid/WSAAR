#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
from bs4 import BeautifulSoup
from termcolor import colored

# Check for SQLi
def sqli_param(host, session):
    sqli_filter = session.get(f"https://{host}.web-security-academy.net/filter?category=sqli")
    soup = BeautifulSoup(sqli_filter.content, "html.parser")
    is_sqli = soup.find("h1", text="sqli")
    if is_sqli:
        print(colored("[+] Possible SQLi due to filter?category=parameter", "green"))

# SQLi on XML
def sqli_on_xml(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/resources/js/xmlStockCheckPayload.js")
    if r.status_code == 200:
        print(colored("[+] Possible SQLi or XXE due to XML parsing on /resources/js/xmlStockCheckPayload.js", "green"))
