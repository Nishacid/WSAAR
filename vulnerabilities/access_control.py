#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

from termcolor import colored

# Checking for Transcript Script
def transcript_ac(host, session):
    r = session.get(f"https://{host}.web-security-academy.net/resources/js/viewTranscript.js")
    if r.status_code == 200:
        print(colored("[+] Possible Access Control vulnerability due to the Transcript script on /resources/js/viewTranscript.js", "green"))