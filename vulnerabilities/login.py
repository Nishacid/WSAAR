#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
import re
import json
import vulnerabilities.cors
from bs4 import BeautifulSoup
from termcolor import colored

# Checking for password change feature
def change_password(request):
    soup = BeautifulSoup(request, "html.parser")
    pattern_chpwd = soup.find_all("form", {"id": "change-password"})
    if pattern_chpwd:
        print(colored(f"[+] Password change feature", "green"))

# Checking for API Key
def is_api_key_html(request):
    pattern = re.compile('<span id="apikey">(.*)<\/span>')
    api_key = pattern.search(request)
    if api_key:
        print(colored(f"[+] User have an API Key : {api_key.group(1)}", "green"))

# Try to get some account details
def account_details(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/accountDetails")
    if r.status_code == 200:
        print(colored("[+] Account Details found on /accountDetails", "green"))
        data = json.loads(r.content)
        print(json.dumps(data, indent = 4, sort_keys=True))
        headers = r.headers
        cors_header_check(headers)

# Stay Login
def stay_login(request):
    soup = BeautifulSoup(request, "html.parser")
    stayLogin = soup.find('input', dict(name='stay-logged-in'))
    if stayLogin:
        stayLogin = True
        print(colored("[+] Stay-Logged-In functionality on /login, possible Authentication vulnerability", "green"))

# Is there an upload form ? 
def is_upload_form(request):
    soup = BeautifulSoup(request, "html.parser")
    uploadForm = soup.find('input', dict(type='file'))
    if uploadForm:
        print(colored("[+] File Upload feature on user account", "green"))


# Check for cors headers
def cors_header_check(requestHeaders):
    # all cors headers
    cors_headers = ['Access-Control-Allow-Credentials', 'Access-Control-Allow-Origin']
    for headers in cors_headers: 
        if requestHeaders.get(headers):
            print(colored(f"[+] Highly possible CORS due to {headers} Header in response", "green"))

# Let's perform a login request
def login(host, username, password, session):
    user = "wiener"
    passwd = "peter"
    login_path = ["login", "sign-in"]
    for login in login_path:
        login_exist = session.get(f"https://{host}.web-security-academy.net/{login}")
        if login_exist.status_code == 200:
            print(colored(f"[+] There is a login page on /{login}", "green"))
            
            # Custom Login 
            if username and password: 
                user = username
                passwd = password
            elif username and not password: 
                print("[!] Please provide a password !")
            elif password and not username:
                print("[!] Please provide a username !")
            # forgotpassword
            forgotpass_path = ["forgotpassword", "new-password", "forgot-password", "newpassword", "new_password"]
            for forgotpass in forgotpass_path:
                forgot_password = session.get(f"https://{host}.web-security-academy.net/{forgotpass}")
                if forgot_password.status_code == 200:
                    print(colored(f"[+] Forgot password functionality on /{forgotpass}", "green"))
            # StayLogin ?
            stay_login(login_exist.content)
            # Set CSRF Token
            soup = BeautifulSoup(login_exist.content, "html.parser")
            csrftoken = soup.find('input', dict(name='csrf'))
            if csrftoken:
                csrftoken = csrftoken['value']
                print(colored(f"[*] CSRF Token required for login", "yellow"))
                data = {
                'csrf': csrftoken,
                'username': user,
                'password': passwd
                }
            else: 
                data = {
                'username': user,
                'password': passwd
                }
            full_url = "https://{host}.web-security-academy.net/"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'DNT' : '1',
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Referer': full_url
            }
            login = session.post(f"https://{host}.web-security-academy.net/login", data = data, headers = headers)
            soup = BeautifulSoup(login.content, "html.parser")
            account_content = soup.find_all("div", {"id": "account-content"})
            if account_content and user == "wiener" and passwd == "peter":
                is_login = True
                print(colored("[+] Successful login with default wiener:peter account", "green"))
                # get cookies
                lab_cookies = session.cookies.get_dict()
                session_cookie = lab_cookies['session']
                print(colored(f"[*] Post-login cookies are : {lab_cookies}", "green"))
                if session_cookie.startswith("eyJ"):
                    print(colored("[*] The cookies is a JSON web tokens (JWT)", "green"))
                
                print("\n[*] Account Informations ")
                # Search for API Key
                is_api_key_html(login.text)
                # Search for password change 
                change_password(login.content)
                # Search for upload form 
                is_upload_form(login.text)
                # account details 
                account_details(host, session)
                
                return session_cookie
                
            elif account_content:
                is_login = True
                print(colored(f"[+] Successful login with custom {user}:{passwd} account", "green"))
                # get cookies
                lab_cookies = session.cookies.get_dict()
                session_cookie = lab_cookies['session']
                print(colored(f"[*] Cookies are : {lab_cookies}", "green"))
                if session_cookie.startswith("ey"):
                    print(colored("[*] The cookies appear to be a JSON web tokens (JWT)", "green"))
                
                print("\n[*] Account Informations ")
                # Search for API Key
                is_api_key_html(login.text)
                # Search for password change 
                change_password(login.content)
                # Search for upload form 
                is_upload_form(login.text)
                # account details 
                account_details(host, session)

                return session_cookie
            else: 
                if user == "wiener" and passwd == "peter": 
                    print(colored("[-] Default login doesn't work", "red"))
                else: 
                    print(colored("[-] Custom login doesn't work", "red"))
                print(colored("[*] You can try to Bruteforce with the username and password provided in the ./wordlists/ folder.", "yellow"))