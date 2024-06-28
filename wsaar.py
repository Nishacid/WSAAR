#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

# External Imports
import requests
import re
import argparse
import sys
# For better errors :)
from pwn import error
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

# Banner
def banner():
    banner = """
     _          __  _____       ___       ___   _____   
    | |        / / /  ___/     /   |     /   | |  _  \  
    | |  __   / /  | |___     / /| |    / /| | | |_| |  
    | | /  | / /   \___  \   / / | |   / / | | |  _  /  
    | |/   |/ /     ___| |  / /  | |  / /  | | | | \ \  
    |___/|___/     /_____/ /_/   |_| /_/   |_| |_|  \_\ 
    Web Security Academy Auto Recon
    @Nishacid
    """
    return banner

# Arguments 
def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", "-i", dest="host", default=None, help="Your Lab ID", required=True)
    parser.add_argument("--username", "-u", dest="username", default=None, help="Username for login", required=False)
    parser.add_argument("--password", "-p", dest="password", default=None, help="Password for login", required=False)
    parser.add_argument("--burp", "-b", action="store_true", default=None, help="Use burp proxy", required=False)
    # parser.add_argument("--headers", "-p", dest="headers", default=None, help="HTTP Header", required=False) -> todo
    return parser.parse_args()


def set_session(host):
    try:
        # Do first request
        session = requests.Session()
        
        if options.burp:
            print('Using burp proxy')
            proxy_url = 'http://127.0.0.1:8080'
            session.verify = False
            import warnings
            import urllib3
            # Suppress InsecureRequestWarning
            warnings.filterwarnings("ignore", message="Unverified HTTPS request", category=urllib3.exceptions.InsecureRequestWarning)

            session.proxies = {
                "http": proxy_url,
                "https": proxy_url
                }

        r = session.get(f"https://{host}.web-security-academy.net/", allow_redirects=False)
        
        if r.status_code == 504:
            print(colored("[!] The Web-Security Academy lab seems to be finished !", "red"))
            sys.exit()
            
        return session

    except requests.ConnectionError:
        print(colored("[!] The Web-Security Academy Lab seems down !", "red"))
        sys.exit()
        

if __name__ == "__main__":

    try:
        options = parseArgs()

        lab_id = options.host
        username = options.username
        password = options.password

        lab_id_pattern = re.compile("^([a-f0-9]{32})$")
        if lab_id_pattern.match(str(lab_id)):
            # let's go 
            print(banner())

            session = set_session(lab_id)

            # General Check
            print("\n[*] General Check...")
            is_admin_path(lab_id, session)
            is_register(lab_id, session)
            is_robots_file(lab_id, session)
            search_page(lab_id, session)
            is_comments(lab_id, session)
            is_feedback(lab_id, session)
            exploit_server(lab_id, session)
            is_newsletter(lab_id, session)

            
            print("\n[*] Non-session Cookies Check...")
            odd_cookies(lab_id, session)
            
            # Login Check
            print("\n[*] Login Check...")
            #login(lab_id, username, password)

            # Vulnerabilites Check
            
            # Deserialization Check
            #print("\n[*] Deserialization Check...")
            deserialization(login(lab_id, username, password, session))

            
            # CORS check 
            print("\n[*] CORS Check...")
            cors_subdomains(lab_id, session)
            
            # Access Control Check
            print("\n[*] Access Control Check...")
            transcript_ac(lab_id, session)

            # OAuth Check
            print("\n[*] OAuth Check...")
            oauth_check_path(lab_id, session)
            oauth_domain = oauth_get_domain(lab_id, session)
            if oauth_domain is None:
                oauth_domain = oauth_login_social(lab_id, session)
            else:
                oauth_login_social(lab_id, session)
            oauth_check_wellknown(oauth_domain, session)

            # LFI
            print("\n[*] LFI Check...")
            search_lfi(lab_id, session)
            
            # File Upload
            print("\n[*] File Upload Check...")
            is_upload_path(lab_id, session)
            
            # Business Logic
            print("\n[*] Business Logic Check...")
            business_logic(lab_id, session)
            
            # Information Disclosure
            print("\n[*] Information Disclosure Check...")
            git_exposed(lab_id, session)
            trace_admin(lab_id, session)
            debug_page(lab_id, session)
            error_page(lab_id, session)

            # SQLi 
            print("\n[*] SQL Injection Check...")
            sqli_param(lab_id, session)
            sqli_on_xml(lab_id, session)

            # SSRF
            print("\n[*] SSRF Check...")
            ssrf(lab_id, session)
            xxe_or_ssrf(lab_id, session)

            # XXE
            print("\n[*] XXE Check...")
            xxe_check(lab_id, session)

            # Web Cache Poisoning
            print("\n[*] Web Cache Poisoning Check...")
            web_cache_header(lab_id, session)
            web_cache_script(lab_id, session)
            web_cache_pragma_header(lab_id, session)
            
            # XSS
            print("\n[*] XSS Check...")
            xss_check(lab_id, session)
            xss_tracker_script(lab_id, session)
            xss_jquery_dom(lab_id, session)
            xss_angular_dom(lab_id, session)
            xss_dom_comment_post(lab_id, session)
            xss_link(lab_id, session)
            dom_message(lab_id, session)
            
            # HTTP Request Smuggling
            print("\n[*] HTTP Request Smuggling Check...")
            request_smuggling_ua(lab_id, session)
            request_smuggling_http2(lab_id, session)

            # WebSockets 
            print("\n[*] WebSockets Check...")
            live_chat_ws(lab_id, session)

            # Prototype Pollution
            print("\n[*] Prototype Pollution Check...")
            proto_check(lab_id, session)

            print("\n Execution completed, good luck for the next steps :)")
        else:
            print(colored("[!] It doesn't look like a lab ID !", "red"))
            sys.exit()
    except KeyboardInterrupt:
        print("Bye.")