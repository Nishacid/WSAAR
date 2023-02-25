#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
from termcolor import colored
import re

# Check for OAuth 2.0 Path
def oauth_check_path(host, session):
    paths = ["auth", "social-login", "authenticate", "oauth-callback", "authorization"]
    for path in paths:
        r = session.get(f"https://{host}.web-security-academy.net/{path}")
        if r.status_code == 200 or r.status_code == 400:
            print(colored(f"[+] Highly Possible OAuth 2.0 due to path /{path}", "green"))

# Check for OAuth 2.0 Path | Important to do it on the OAuth Server 
def oauth_check_wellknown(host, session):
    paths = [".well-known/oauth-authorization-server", ".well-known/openid-configuration", ".well-known/jwks.json"]
    for path in paths:
        r = session.get(f"https://{host}.web-security-academy.net/{path}")
        if r.status_code == 200:
            print(colored(f"[+] Highly Possible OAuth 2.0 due to well-known on /{path} on OAuth server", "green"))

# Get OAuth server domain
def oauth_get_domain(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/social-login")
    if r.status_code == 200:
        oauth_url = re.compile("content='[0-9];url=https:\/\/([a-z]{5}-[a-z0-9]{32})")
        find = re.search(oauth_url, r.text)
        if find:
            oauth_domain = find.group(1)
            print(colored(f"[+] OAuth Server Domain found : https://{oauth_domain}.web-security-academy.net", "green"))
            return oauth_domain

# Get OAuth login endpoint 
def oauth_login_social(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/login")
    if r.status_code == 200:
        # social media link
        social_media = re.compile("Login with social media")
        social_find = re.search(social_media, r.text)
        if social_find:
            print(colored("[+] Highly possible OAuth 2.0 due to \"Login With Social Media\" found on login page", "green"))
        # oauth url domain
        oauth_url = re.compile("https:\/\/(oauth-[a-z0-9]{32})")
        url_find = re.search(oauth_url, r.text)
        if url_find:
            oauth_domain = url_find.group(1)
            print(colored(f"[+] OAuth Server Domain found : https://{oauth_domain}.web-security-academy.net", "green"))
            return oauth_domain