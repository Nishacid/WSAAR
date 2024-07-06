#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

from termcolor import colored

# Checking for upload vulnerabilities
def is_upload_path(host, session):
        r = session.get(f"https://{host}.web-security-academy.net/files")
        if r.status_code == 403:
            print(colored("[+] Possible Upload vulnerability due to a /files/ path", "green"))