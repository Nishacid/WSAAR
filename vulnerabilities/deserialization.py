#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
import re
import base64
import urllib.parse
from termcolor import colored

"""
Ruby encoded object = BAhvOglVc2VyBzoOQHVzZXJuYW1lSSILd2llbmVyBjoGRUY6EkBhY2Nlc3NfdG9rZW5JIiVqMW5ncm11Y3FiZ2tuNDE2cjliNjhjYmJraTA0cTQ0cAY7B0YK
PHP encoded object = Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czoxMjoiYWNjZXNzX3Rva2VuIjtzOjMyOiJwbngxd2drcmwxdm1wMHdvdjliaHd1M2dpZXlyMG5seiI7fQ%3d%3d
"""

# Check for serialized Cookie
def deserialization(cookies):
    try:
        print("\n[*] Deserialization Check...")
        serialized = urllib.parse.unquote(cookies)
        deserialized = base64.b64decode(serialized).decode()
        
        # some patterns
        ruby_pattern = "BAhv" # Ruby Object
        php_pattern = "O:" # PHP Object

        if re.match(php_pattern, deserialized):
            print(colored(f"[+] PHP Object found : {deserialized}", "green"))
        elif re.match(ruby_pattern, serialized):
            print(colored(f"[+] Ruby Serialized Object found : {serialized}", "green"))
    except :
        pass