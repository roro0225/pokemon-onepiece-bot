import requests
from bs4 import BeautifulSoup

WEBHOOK_URL = "https://discord.com/api/webhooks/1493663712546914314/aVHScNhzEeoRPGvkG6y2_lIwRJQIsrM6P47RtP2IF95SlNldiFTDaRD0sgwmI1N9Ji9T"

accounts = [
"amehuri11",
"fDbmOz2bQQRbgsF",
"keita_anime3939",
"shihandai_tcg0",
"PiROKiCHi_6513",
"Laurier_News",
"KAZOO7a",
"Lovery_lono"
]

keywords = [
"ポケカ",
"ポケモンカード",
"ワンピカード",
"ワンピースカード",
"入荷",
"再販",
"抽選",
"コンビニ",
"セブン",
"ファミマ",
"ローソン"
]

def send_discord(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message}, timeout=10)
    except:
        pass

def check():
    headers = {"User-Agent": "Mozilla/5.0"}
    
    for account in accounts:
        try:
            url = f"https://nitter.net/{account}"
            r = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")

            tweets = soup.find_all("div", class_="tweet-content")

            if not tweets:
                continue

            latest = tweets[0].text

            for keyword in keywords:
                if keyword in latest:
                    send_discord(f"検知: @{account}\n{latest}")
                    break

        except:
            continue

check()
