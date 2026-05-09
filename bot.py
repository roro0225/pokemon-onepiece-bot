import requests
from bs4 import BeautifulSoup

WEBHOOK_URL = "https://discord.com/api/webhooks/1502751263262244867/b7rmjaflRArBcH5S46qQr9Gph1I_1EB67LOeGcE3U1tjVZenh_FvFv7qq55SxwB_sIG0"

# ===== 監視対象（福岡）=====
TARGET_SITES = [
    "https://www.aeon.jp/",
    "https://www.youmetown.co.jp/",
    "https://store.tsutaya.co.jp/",
    "https://geo-online.co.jp/",
    "https://www.yamada-denki.jp/"
]

KEYWORDS = [
    "ポケカ",
    "ポケモンカード",
    "ワンピースカード",
    "ワンピカード",
    "入荷",
    "再販",
    "抽選",
    "予約"
]

# ===== X監視アカウント =====
X_ACCOUNTS = [
    "amehuri11",
    "fDbmOz2bQQRbgsF",
    "keita_anime3939"
]

def send_discord(msg):
    try:
        requests.post(WEBHOOK_URL, json={"content": msg}, timeout=10)
    except:
        pass

def check_websites():
    headers = {"User-Agent": "Mozilla/5.0"}
    for url in TARGET_SITES:
        try:
            r = requests.get(url, headers=headers, timeout=10)
            text = r.text
            for keyword in KEYWORDS:
                if keyword in text:
                    send_discord(f"【福岡店舗検知】\n{keyword}\n{url}")
                    break
        except:
            continue

def check_x():
    headers = {"User-Agent": "Mozilla/5.0"}
    for account in X_ACCOUNTS:
        try:
            url = f"https://nitter.net/{account}"
            r = requests.get(url, headers=headers, timeout=10)
            if "tweet" in r.text:
                send_discord(f"【X監視】@{account} 更新検知")
        except:
            continue

# ===== 実行 =====
check_websites()
check_x()
