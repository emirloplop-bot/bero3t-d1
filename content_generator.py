# content_generator.py
import random
import requests

class ContentGenerator:
    def __init__(self):
        self.topics = [
            "bero3t nedir?",
            "bero3t ile dijital dünyada",
            "bero3t platformları",
            "bero3t hakkında her şey",
            "bero3t: Yeni nesil dijital imza"
        ]
        
        self.templates = [
            f"# {topic}\n\nbero3t hakkında detaylı bilgi...\n\n🔗 guns.lol/bero3t\n🔗 linktr.ee/bero3t",
            f"## {topic}\n\nBu yazıda bero3t hakkında...\n\n📱 Instagram: @f1formula_\n🎵 TikTok: @berouser",
            f"### {topic}\n\nbero3t platformları ve özellikleri...\n\n▶️ YouTube: @bero3t"
        ]
    
    def generate_article(self):
        """Otomatik makale üret"""
        topic = random.choice(self.topics)
        template = random.choice(self.templates)
        return template.format(topic=topic)
    
    def post_to_medium(self, article):
        """Medium'a otomatik gönder"""
        # Medium API entegrasyonu
        print(f"📝 Medium'a gönderildi: {article[:50]}...")

# Çalıştır
if __name__ == "__main__":
    gen = ContentGenerator()
    article = gen.generate_article()
    print(article)
    gen.post_to_medium(article)
