import requests
from bs4 import BeautifulSoup

# 🔴 あなたのDiscord Webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1502751263262244867/b7rmjaflRArBcH5S46qQr9Gph1I_1EB67LOeGcE3U1tjVZenh_FvFv7qq55SxwB_sIG0"

# 監視アカウント
X_ACCOUNTS = [
    "pokeotk",
    "Lovery_lono"
]

# 検知キーワード
KEYWORDS = [
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

def check_x():
    headers = {"User-Agent": "Mozilla/5.0"}

    for account in X_ACCOUNTS:
        try:
            url = f"https://nitter.net/{account}"
            r = requests.get(url, headers=headers, timeout=10)

            soup = BeautifulSoup(r.text, "html.parser")
            tweets = soup.find_all("div", class_="tweet-content")

            if not tweets:
                continue

            latest = tweets[0].text

            for keyword in KEYWORDS:
                if keyword in latest:
                    send_discord(f"【検知】@{account}\n{keyword}\n\n{latest}")
                    break

        except:
            continue

check_x()
