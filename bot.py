import requests

# 🔴 ここにあなたのDiscord Webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1502751263262244867/b7rmjaflRArBcH5S46qQr9Gph1I_1EB67LOeGcE3U1tjVZenh_FvFv7qq55SxwB_sIG0"

# 🔔 テスト通知（動作確認用）
def send_discord(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message}, timeout=10)
    except:
        pass

# 🚀 起動確認
send_discord("BOT正常起動")

# 🧠 監視キーワード（ここに追加OK）
keywords = [
    "ポケカ",
    "ポケモンカード",
    "ワンピカード",
    "ワンピースカード",
    "入荷",
    "再販",
    "抽選"
]

# 🔍 ここに将来API連携を追加します
print("BOT実行完了")
