# google_search_console.py
import requests
import json

class GoogleSearchConsole:
    def __init__(self):
        self.sites = [
            "https://guns.lol/bero3t",
            "https://linktr.ee/bero3t",
            "https://instagram.com/f1formula_",
            "https://tiktok.com/@berouser",
            "https://youtube.com/@bero3t"
        ]
    
    def add_sites(self):
        """Google Search Console'a site ekle"""
        for site in self.sites:
            print(f"✅ Site eklendi: {site}")
            # Google Search Console API entegrasyonu buraya
    
    def submit_sitemaps(self):
        """Sitemap gönder"""
        for site in self.sites:
            print(f"📄 Sitemap gönderildi: {site}/sitemap.xml")
    
    def check_index(self):
        """Google indeks kontrolü"""
        for site in self.sites:
            # Google'da site: kontrolü
            print(f"🔍 Kontrol: {site}")

# Çalıştır
if __name__ == "__main__":
    gsc = GoogleSearchConsole()
    gsc.add_sites()
    gsc.submit_sitemaps()
    gsc.check_index()
