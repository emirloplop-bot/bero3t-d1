# reporting.py
import requests
from datetime import datetime

class ReportSystem:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
    
    def send_daily_report(self):
        """Günlük rapor gönder"""
        now = datetime.now()
        report = f"""
📊 <b>BERO3T GÜNLÜK RAPOR</b>
📅 {now.strftime('%d.%m.%Y')}

✅ <b>Durum:</b>
• Google Search Console: Aktif
• Backlink: 10 site
• Sosyal Medya: 3 platform
• Telegram Bot: Çalışıyor

📈 <b>Hedefler:</b>
• Google'da ilk sayfa
• 1000+ ziyaretçi
• 10+ backlink

🚀 <b>Yarın:</b>
• Yeni içerikler
• Daha fazla backlink
• Sosyal medya paylaşımları

#bero3t #seo #dijital
"""
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": report,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data)
        print("📨 Günlük rapor gönderildi!")

# Çalıştır
if __name__ == "__main__":
    reporter = ReportSystem("6888524885:AAEHvwSRkNB2mY5v5izUhv_bTAMoDtJp83A", "5451721858")
    reporter.send_daily_report()
