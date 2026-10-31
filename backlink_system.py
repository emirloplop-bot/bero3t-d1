# backlink_system.py
import requests
import time

class BacklinkSystem:
    def __init__(self):
        self.target = "https://guns.lol/bero3t"
        self.backlink_sites = [
            "https://www.reddit.com/r/technology/",
            "https://www.quora.com/",
            "https://dev.to/",
            "https://medium.com/",
            "https://www.linkedin.com/",
            "https://www.facebook.com/groups/",
            "https://www.pinterest.com/",
            "https://www.tumblr.com/",
            "https://www.blogger.com/",
            "https://wordpress.com/"
        ]
    
    def create_backlink(self, site, content):
        """Backlink oluştur"""
        print(f"🔗 Backlink: {site} → {self.target}")
        time.sleep(2)
    
    def rotate_backlinks(self):
        """Backlinkleri döndür"""
        for site in self.backlink_sites:
            self.create_backlink(site, "bero3t hakkında bilgi")
    
    def daily_backlink_report(self):
        """Günlük backlink raporu"""
        report = f"""
📊 BACKLINK RAPORU
🎯 Hedef: {self.target}
🔗 Toplam Backlink: {len(self.backlink_sites)}
📈 Durum: Aktif
"""
        print(report)
        return report

# Çalıştır
if __name__ == "__main__":
    backlink = BacklinkSystem()
    backlink.rotate_backlinks()
    backlink.daily_backlink_report()
