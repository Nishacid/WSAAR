#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import websocket
import re
from termcolor import colored

# def websocket_connect(host, session):
#     ws = websocket.WebSocket()
#     ws.connect("wss://{host}.web-security-academy.net/chat")
#     ws.send("Hello, Server")
#     print(ws.recv())
#     ws.close()

# Checking for live chat - WebSockets
def live_chat_ws(host, session):
        r = session.get(f"https://{host}.web-security-academy.net/chat")
        websocket = re.compile("action=\"(wss:\/\/[a-f0-9]{32}\.web-security-academy\.net\/chat)")
        if r.status_code == 200:
            websocket_pattern = websocket.search(r.text)
            if websocket_pattern:
                print(colored("[+] Highly Possible WebSocket vulnerability due to WebSocket endpoint on /chat", "green"))
                print(colored(f"[*] WebSocket Endpoint : {websocket_pattern.group(1)}", "green"))