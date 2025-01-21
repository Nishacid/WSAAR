#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import re
import json
import requests
from bs4 import BeautifulSoup
from termcolor import colored

# Prompt for user credentials
def get_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

# Check for password change feature
def check_password_change(request):
    soup = BeautifulSoup(request, "html.parser")
    if soup.find("form", {"id": "change-password"}):
        print(colored("[+] Password change feature", "green"))

# Check for API Key in HTML
def check_api_key_html(request):
    pattern = re.compile(r'<span id="apikey">(.*)</span>')
    match = pattern.search(request)
    if match:
        print(colored(f"[+] User has an API Key: {match.group(1)}", "green"))

# Retrieve account details
def get_account_details(host, session):
    try:
        response = session.get(f"https://{host}.web-security-academy.net/accountDetails", verify=True)
        response.raise_for_status()
        print(colored("[+] Account details found on /accountDetails", "green"))
        data = json.loads(response.content)
        print(json.dumps(data, indent=4, sort_keys=True))
        check_cors_headers(response.headers)
    except requests.RequestException as e:
        print(colored(f"[-] Failed to retrieve account details: {e}", "red"))

# Check for stay logged-in functionality
def check_stay_logged_in(request):
    soup = BeautifulSoup(request, "html.parser")
    if soup.find('input', {"name": "stay-logged-in"}):
        print(colored("[+] Stay-Logged-In functionality on /login, possible Authentication vulnerability", "green"))

# Check for file upload form
def check_upload_form(request):
    soup = BeautifulSoup(request, "html.parser")
    if soup.find('input', {"type": "file"}):
        print(colored("[+] File upload feature on user account", "green"))

# Check for CORS headers
def check_cors_headers(headers):
    cors_headers = ['Access-Control-Allow-Credentials', 'Access-Control-Allow-Origin']
    for header in cors_headers:
        if header in headers:
            print(colored(f"[+] Potential CORS vulnerability due to {header} header in response", "green"))

# Get dynamic login path
def get_login_path(host, session):
    try:
        homepage = session.get(f'https://{host}.web-security-academy.net/', verify=True)
        soup = BeautifulSoup(homepage.text, 'html.parser')
        account_anchor = soup.find("a", text='My account')
        return account_anchor.attrs.get('href').strip('/')
    except AttributeError:
        return None
    except requests.RequestException as e:
        print(colored(f"[-] Failed to retrieve login path: {e}", "red"))
        return None

# Perform login request
def login(host, username, password, session):
    login_paths = [get_login_path(host, session)] or ["login", "sign-in"]
    for login_path in login_paths:
        try:
            response = session.get(f"https://{host}.web-security-academy.net/{login_path}", verify=True)
            response.raise_for_status()
            print(colored(f"[+] Login page found at /{login_path}", "green"))

            check_stay_logged_in(response.content)
            soup = BeautifulSoup(response.content, "html.parser")
            csrftoken = soup.find('input', {"name": "csrf"})
            data = {'username': username, 'password': password}
            if csrftoken:
                data['csrf'] = csrftoken['value']
                print(colored("[*] CSRF Token required for login", "yellow"))

            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'DNT': '1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Referer': f"https://{host}.web-security-academy.net/"
            }
            login_response = session.post(f"https://{host}.web-security-academy.net/{login_path}", data=data, headers=headers, verify=True)
            login_response.raise_for_status()

            soup = BeautifulSoup(login_response.content, "html.parser")
            if soup.find("div", {"id": "account-content"}):
                print(colored(f"[+] Successful login with {username} account", "green"))
                cookies = session.cookies.get_dict()
                session_cookie = cookies.get('session', '')

                if session_cookie.startswith("ey"):
                    print(colored("[*] The session cookie is a JSON web token (JWT)", "green"))

                print("\n[*] Account Information ")
                check_api_key_html(login_response.text)
                check_password_change(login_response.content)
                check_upload_form(login_response.text)
                get_account_details(host, session)

                return session_cookie
            else:
                print(colored(f"[-] Login with {username} failed", "red"))
        except requests.RequestException as e:
            print(colored(f"[-] Failed to access login page at /{login_path}: {e}", "red"))
    return None

# Main execution
if __name__ == "__main__":
    host = input("Enter host: ")
    username, password = get_credentials()
    session = requests.Session()
    login(host, username, password, session)
