#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
from bs4 import BeautifulSoup
from termcolor import colored

# General Informations Check
# Check for existing Admin Panel
def is_admin_path(host, session):
    admin_path = ["admin", "admin-panel", "admin_panel", "admin_controls", "admin-controls"]
    for path in admin_path:
        r = session.get(f"https://{host}.web-security-academy.net/{path}")
        if r.status_code == 200:
            print(colored(f"[+] Admin Panel Found on /{path}", "green"))
        elif r.status_code == 401 or r.status_code == 403:
            print(colored(f"[+] Restricted Admin Panel Found on /{path}", "green"))

# Check for robots.txt file
def is_robots_file(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/robots.txt")
    if r.status_code == 200:
        print(colored("[+] Robots.txt Found", "green"))
        print(f"{r.text}\n")

# Check for register feature
def is_register(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/register")
    if r.status_code == 200:
        print(colored("[+] Register feature found at /register", "green"))

# Check for a search function
def search_page(host, session):
    # is input ?
    search_page = session.get(f"https://{host}.web-security-academy.net/")
    soup = BeautifulSoup(search_page.content, "html.parser")
    isSearch = soup.find('input', dict(name='search'))
    if isSearch:
        print(colored("[+] Search page Found", "green"))
    # Advanced Search page
    advanced_search = ["filteredsearch", "filtered_search"]
    for path in advanced_search:
        r = session.get(f"https://{host}.web-security-academy.net/{path}")
        if r.status_code == 302:
        print(colored("[+] Possible Advanced Search page on /{path}", "green"))
        elif r.status_code == 200:
        print(colored("[+] Advanced Search page on /{path}", "green"))

# Check for comments 
def is_comments(host, session):
    # Get commments 
    is_comment = session.get(f"https://{host}.web-security-academy.net/post?postId=1")
    # IsComment ?
    soup = BeautifulSoup(is_comment.content, "html.parser")
    isComment = soup.find('textarea', dict(name='comment'))
    if isComment:
        isComment = True
        print(colored("[+] Possibility to leave a comment on a post", "green"))

# Check for feedback
def is_feedback(host, session):
    # isFeedback ? 
    r = session.get(f"https://{host}.web-security-academy.net/feedback")
    if r.status_code == 200:
        print(colored("[+] Feedback feature on /feedback", "green"))

# Check for newsletter 
def is_newsletter(host, session):
    # Get page 
    is_newsletter = session.get(f"https://{host}.web-security-academy.net/")
    # IsNewsLetter ?
    if 'Sign up to our newsletter' in is_newsletter.text:
    # soup = BeautifulSoup(is_newsletter.content, "html.parser")
    # isComment = soup.find('form', dict(name='comment'))
        print(colored("[+] Newsletter form feature", "green"))

# Check for exploit server 
def exploit_server(host, session):
    # Get exploit server 
    exploit_server = session.get(f"https://{host}.web-security-academy.net/")
    # Exploit link ?
    soup = BeautifulSoup(exploit_server.content, "html.parser")
    exploitServer = soup.find('a', dict(id='exploit-link'))
    exploit_link = exploitServer = soup.find('a',dict(id='exploit-link'), href=True)
    if exploitServer:
        exploitServer = True
        exploitServer_link = exploit_link['href']
        print(colored(f"[+] Exploit server avaliable on {exploitServer_link}", "green"))
        try:
            r = session.get(f"{exploitServer_link}/email")
            if r.status_code == 200:
                print(colored(f"[+] Exploit server have an email server on {exploitServer_link}/email", "green"))
        except requests.ConnectionError:
            pass