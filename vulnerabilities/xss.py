#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

from termcolor import colored

# Check for reflected word in response
def xss_check(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/foobar")
    response = r.text
    if 'foobar' in response:
        print(colored("[+] Possible XSS due to a reflected word in 404 response", "green"))

# Check for reflected script in response
def xss_tracker_script(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/?search=foobar")
    response = r.text
    if '<img src="/resources/images/tracker.gif?searchTerms=' in response:
        print(colored("[+] Possible XSS due to a tracking script during a search", "green"))

# Check for jQuery link 
def xss_jquery_dom(host, session):
    paths = ["resources/js/jqueryMigrate_1-4-1.js", "resources/js/jquery_1-8-2.js", "resources/js/jquery_3-0-0.js", "resources/js/jquery_1-7-1.js"]
    for path in paths:
        r = session.get(f"https://{host}.web-security-academy.net/{path}")
        if r.status_code == 200:
            print(colored(f"[+] Possible DOM Based XSS through jQuery due to the included jQuery script /{path}", "green"))

# Check for Angular link 
def xss_angular_dom(host, session):
    paths = ["resources/js/angular_1-7-7.js"]
    for path in paths:
        r = session.get(f"https://{host}.web-security-academy.net/{path}")
        if r.status_code == 200:
            print(colored(f"[+] Possible DOM Based XSS through Angular due to the included Angular script /{path}", "green"))

# Check for escaping script when posting comment
def xss_dom_comment_post(host, session):
    paths = ["resources/js/loadCommentsWithVulnerableEscapeHtml.js"]
    for path in paths:
        r = session.get(f"https://{host}.web-security-academy.net/{path}")
        if r.status_code == 200:
            print(colored(f"[+] Possible DOM Based XSS when posting comment due to the included escaping script /{path}", "green"))

# Check for input reflected in link
def xss_link(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/?foobar")
    response = r.text
    if 'foobar' in response:
        print(colored("[+] Possible XSS due to a reflected word in response /?foobar (maybe link?)", "green"))

# Check for DOM XSS using web messages 
def dom_message(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/")
    response = r.text
    if "addEventListener('message" in response:
            print(colored("[+] Highly possible DOM based XSS due to ads feature and EventListener for message in home page", "green"))
    