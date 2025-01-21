#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

# External Imports
import requests
import re
import argparse
import sys
from termcolor import colored

# Local Imports
from vulnerabilities.lfi import *
from vulnerabilities.oauth import *
from vulnerabilities.login import *
from vulnerabilities.sqli import *
from vulnerabilities.ssrf import *
from vulnerabilities.xxe import *
from vulnerabilities.xss import *
from vulnerabilities.cors import *
from vulnerabilities.upload import *
from vulnerabilities.deserialization import *
from vulnerabilities.websocket_checks import *
from vulnerabilities.access_control import *
from vulnerabilities.business_logic import *
from vulnerabilities.information_disclosure import *
from vulnerabilities.web_cache_poisoning import *
from vulnerabilities.request_smuggling import *
from vulnerabilities.prototype_pollution import *
from vulnerabilities.enumeration import *

def banner():
    """
    Display the banner.
    """
    banner_text = """
     _          __  _____       ___       ___   _____   
    | |        / / /  ___/     /   |     /   | |  _  \  
    | |  __   / /  | |___     / /| |    / /| | | |_| |  
    | | /  | / /   \___  \   / / | |   / / | | |  _  /  
    | |/   |/ /     ___| |  / /  | |  / /  | | | | \ \  
    |___/|___/     /_____/ /_/   |_| /_/   |_| |_|  \_\ 
    Web Security Academy Auto Recon
    @Nishacid
    """
    return banner_text

def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", "-i", dest="host", required=True, help="Your Lab ID")
    parser.add_argument("--username", "-u", dest="username", help="Username for login")
    parser.add_argument("--password", "-p", dest="password", help="Password for login")
    parser.add_argument("--burp", "-b", action="store_true", help="Use burp proxy")
    return parser.parse_args()

def set_session(host, use_burp):
    """
    Set up the session for making requests.
    """
    try:
        session = requests.Session()
        
        if use_burp:
            print('Using burp proxy')
            proxy_url = 'http://127.0.0.1:8080'
            session.verify = False
            import warnings
            import urllib3
            warnings.filterwarnings("ignore", message="Unverified HTTPS request", category=urllib3.exceptions.InsecureRequestWarning)
            session.proxies = {"http": proxy_url, "https": proxy_url}

        response = session.get(f"https://{host}.web-security-academy.net/", allow_redirects=False)
        
        if response.status_code == 504:
            print(colored("[!] The Web-Security Academy lab seems to be finished!", "red"))
            sys.exit()
            
        return session

    except requests.ConnectionError:
        print(colored("[!] The Web-Security Academy Lab seems down!", "red"))
        sys.exit()

if __name__ == "__main__":
    try:
        options = parse_args()
        session = set_session(options.host, options.burp)
        # Add further functionality as needed
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))
        sys.exit(1)
