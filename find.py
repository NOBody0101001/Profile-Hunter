import subprocess
import requests
import pyfiglet
import datetime
import os
from threading import Thread
import re
import hashlib

def check_and_install(package):
    try:
        subprocess.check_call(["pip", "install", package])
        print(f"\033[92m{package} - Modül başarıyla yüklendi\033[0m")
    except Exception as e:
        print(f"\033[91m{package} - Modül yüklenirken bir hata oluştu: {e}\033[0m")

def update(package):
    try:
        subprocess.check_call(["pip", "install", "--upgrade", package])
        print(f"\033[92m{package} - Modül başarıyla güncellendi\033[0m")
    except Exception as e:
        print(f"\033[91m{package} - Modül güncellenirken bir hata oluştu: {e}\033[0m")

def check_dependencies():
    dependencies = ["requests", "pyfiglet"]
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"\033[92m{dep} - Kontrol edildi\033[0m")
            update(dep)
        except ImportError:
            check_and_install(dep)
        except Exception as e:
            print(f"\033[91m{dep} - Bir hata oluştu: {e}\033[0m")

def find_user(username):
    found = False
    sites = {
        "Twitter": f"https://x.com/{username}",
"Instagram": f"https://www.instagram.com/{username}",
"GitHub": f"https://github.com/{username}",
"Pornhub": f"https://www.pornhub.com/users/{username}",
"Amazon": f"https://www.amazon.com/gp/profile/amzn1.account.{username}",
"Roblox": f"https://www.roblox.com/search/users?keyword={username}",
"XHamster": f"https://nl.xhamster.com/categories/porn-for-women?username={username}",
"IXXX": f"https://www.ixxx.com/nl/a-z?username={username}",
"VaginaNL": f"https://vagina.nl/?username={username}",
"XVideos": f"https://www.xvideos.com/lang/nederlands?username={username}",
"Dak7": f"https://7dak.com/?username={username}",
"Domlepen": f"https://domlepen.com/?username={username}",
"Porncom": f"https://nl.porn.com/?username={username}",
"ThePornDude": f"https://theporndude.com/nl?username={username}",
"HDAbla": f"https://hdabla.net/?username={username}",
"Superporn": f"https://www.superporn.com/nl?username={username}",
"Pornoseyret": f"https://pornoseyret.net/gozluklu-uvey-annesiyle-birlikte-mutfakta-seks-vakti/?username={username}",
"SXVKT": f"https://sxvkt.online/?username={username}",
"31Vaxti": f"https://31vaxti.site/?username={username}",
"Facebook": f"https://www.facebook.com/{username}",
"Evooli": f"https://www.evooli.com/{username}",
"Upslut": f"https://upslut.com/{username}",
"Minecraft": f"https://www.minecraft.net/{username}",
"Telegram": f"https://t.me/{username}",
"TikTok": f"https://www.tiktok.com/@{username}",
"Snapchat": f"https://www.snapchat.com/add/{username}",
"WhatsApp": f"https://wa.me/{username}",
"eFootball": f"https://www.konami.com/efootball/{username}",
"CapCut": f"https://www.capcut.app/user/profile/{username}",
"YouTube": f"https://www.youtube.com/{username}",
"Twitch": f"https://www.twitch.tv/{username}",
"LinkedIn": f"https://www.linkedin.com/in/{username}",
"Pinterest": f"https://www.pinterest.com/{username}",
"SoundCloud": f"https://soundcloud.com/{username}",
"Tumblr": f"https://{username}.tumblr.com",
"Reddit": f"https://www.reddit.com/user/{username}",
"Discord": f"https://discord.com/users/{username}",
"Medium": f"https://medium.com/@{username}",
"Behance": f"https://www.behance.net/{username}",
"Vimeo": f"https://vimeo.com/{username}",
"Dribbble": f"https://dribbble.com/{username}",
"Stack Overflow": f"https://stackoverflow.com/users/{username}",
"DeviantArt": f"https://{username}.deviantart.com",
    }

    for site, url in sites.items():
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[92m{site} - {url} - Bulundu\033[0m")
            found = True
        else:
            print(f"\033[91m{site} - {url} - Bulunamadı\033[0m")

    return found

def custom_search(username, site_name, site_url):
    url = site_url.format(username)
    response = requests.get(url)
    if response.status_code == 200:
        print(f"\033[92m{site_name} - {url}\033[0m")
        print("Profil bulundu:", url)
        return True
    else:
        print(f"\033[91m{site_name} - {url} - Bulunamadı\033[0m")
        return False

def validate_username(username):
    if len(username) < 3:
        return False
    elif not username.isalnum():
        return False
    else:
        return True

def validate_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def log_result(identifier, found):
    with open("log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if found:
            f.write(f"{timestamp} - '{identifier}' bulundu\n")
        else:
            f.write(f"{timestamp} - '{identifier}' bulunamadı\n")

def load_config():
    config = {}
    if os.path.exists("config.txt"):
        with open("config.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
    return config

def save_config(config):
    with open("config.txt", "w") as f:
        for key, value in config.items():
            f.write(f"{key} = {value}\n")

def display_statistics():
    if os.path.exists("log.txt"):
        with open("log.txt", "r") as f:
            lines = f.readlines()
            total_searches = len(lines)
            total_found = sum(1 for line in lines if "bulundu" in line)
            total_not_found = total_searches - total_found
            print(f"Toplam aramalar: {total_searches}")
            print(f"Bulunan kullanıcılar: {total_found}")
            print(f"Bulunamayan kullanıcılar: {total_not_found}")
    else:
        print("Henüz hiç arama yapılmamış.")

def multi_threaded_find(username):
    found = find_user(username)
    log_result(username, found)

def find_email(email):
    found = False
    sites = {
        "Twitter": f"https://x.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Instagram": f"https://www.instagram.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"GitHub": f"https://github.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Pornhub": f"https://www.pornhub.com/users/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Amazon": f"https://www.amazon.com/gp/profile/amzn1.account.{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Roblox": f"https://www.roblox.com/search/users?keyword={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Gravatar": f"https://en.gravatar.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"XHamster": f"https://nl.xhamster.com/categories/porn-for-women?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"IXXX": f"https://www.ixxx.com/nl/a-z?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"VaginaNL": f"https://vagina.nl/?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"XVideos": f"https://www.xvideos.com/lang/nederlands?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Dak7": f"https://7dak.com/?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Domlepen": f"https://domlepen.com/?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Porncom": f"https://nl.porn.com/?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"ThePornDude": f"https://theporndude.com/nl?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"HDAbla": f"https://hdabla.net/?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Superporn": f"https://www.superporn.com/nl?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Pornoseyret": f"https://pornoseyret.net/gozluklu-uvey-annesiyle-birlikte-mutfakta-seks-vakti/?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"SXVKT": f"https://sxvkt.online/?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"31Vaxti": f"https://31vaxti.site/?email={hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Facebook": f"https://www.facebook.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Evooli": f"https://www.evooli.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Upslut": f"https://upslut.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Call of Duty": f"https://www.callofduty.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Minecraft": f"https://www.minecraft.net/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"LinkedIn": f"https://www.linkedin.com/in/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Adobe Creative Cloud": f"https://account.adobe.com/profile/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Bitbucket": f"https://bitbucket.org/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"GitLab": f"https://gitlab.com/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
"Slack": f"https://{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}.slack.com",
"Zoom": f"https://zoom.us/profile/{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}",
    }

    for site, url in sites.items():
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[92m{site} - {url} - Bulundu\033[0m")
            found = True
        else:
            print(f"\033[91m{site} - {url} - Bulunamadı\033[0m")

    return found

def multi_threaded_find_email(email):
    found = find_email(email)
    log_result(email, found)

def filter_user(username):
    filtered_username = re.sub(r'[^a-zA-Z0-9]', '', username)
    print(f"Filtrelenmiş kullanıcı adı: {filtered_username}")
    return filtered_username

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n\033[93mModül ve kütüphaneler kontrol ediliyor...\033[0m")
    check_dependencies()

    ascii_art_user_finder = pyfiglet.figlet_format("User Finder")
    print(ascii_art_user_finder)

    config = load_config()

    while True:
        print("\n\033[93mMade By protocolhere\033[0m")
        print(" ")
        print("1. Kullanıcıyı Bul")
        print("2. Özel Arama Yap")
        print("3. İstatistikleri Görüntüle")
        print("4. E-posta ile Arama")
        print("5. Çıkış")
        
        choice = input("Lütfen bir seçenek seçin: ")

        if choice == "1":
            username = input("Lütfen aramak istediğiniz kullanıcı adını girin: ")
            if validate_username(username):
                filter_choice = input("Filtrelemek ister misiniz? (y/n): ")
                if filter_choice.lower() == "y":
                    filtered_username = filter_user(username)
                    multi_threaded_find(filtered_username)
                elif filter_choice.lower() == "n":
                    multi_threaded_find(username)
                else:
                    print("Geçersiz bir seçenek girdiniz.")
            else:
                print("Geçersiz kullanıcı adı. Lütfen tekrar deneyin.")
        elif choice == "2":
            pass
        elif choice == "3":
            display_statistics()
        elif choice == "4":
            email = input("Lütfen aramak istediğiniz mail adresini girin: ")
            if validate_email(email):
                multi_threaded_find_email(email)
            else:
                print("Geçersiz mail adresi. Lütfen tekrar deneyin.")
        elif choice == "5":
            print("Programdan çıkılıyor...")
            save_config(config)
            break
        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")

    print("\n\033[93mMade By protocolhere\033[0m")
    print("Programdan çıkıldı.")
