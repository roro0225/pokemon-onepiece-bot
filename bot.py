import requests
import time

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
    data = {"content": message}
    requests.post(WEBHOOK_URL, json=data)

def check():
    for account in accounts:
        url = f"https://nitter.net/{account}"
        r = requests.get(url)
        text = r.text

        for keyword in keywords:
            if keyword in text:
                send_discord(f"検知: @{account} に {keyword}")
                break

check()
