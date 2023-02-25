#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
from termcolor import colored

# Check for Object prototype in JavaScript files
def proto_check(host, session):
    jsFiles = ["searchLogger.js", "deparam.js", "deparamSanitised.js", "jquery_parseparams.js", "searchLoggerFiltered.js", "searchLoggerAlternative.js", "searchLoggerConfigurable.js", "ga.js", "jquery_ba_bbq.js", "store.js"]
    for file in jsFiles:
        r = session.get(f"https://{host}.web-security-academy.net/resources/js/{file}")
        response = r.text
        source_keywords = ["prototype", "object"]
        sink_keywords = ["eval", "createElement", "innerHTML"]
        for source in source_keywords:
            if source in response:
                print(colored(f"[+] Possible Prototype Pollution due to the prototype source keyword '{source}' in '/{file}'", "green"))
        for sink in sink_keywords:
            if sink in response:
                print(colored(f"[+] Possible Prototype Pollution due to the sink function '{sink}' in '/{file}'", "green"))