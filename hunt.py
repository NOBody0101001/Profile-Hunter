import subprocess
import requests
import pyfiglet
import datetime
import os
from threading import Thread
import re
import hashlib
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

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

def create_session():
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=0.1,
        status_forcelist=[500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

session = create_session()

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
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                print(f"\033[92m{site} - {url} - Bulundu\033[0m")
                found = True
            else:
                print(f"\033[91m{site} - {url} - Bulunamadı\033[0m")
        except requests.exceptions.RequestException as e:
            print(f"\033[91m{site} - {url} - Hata: {e}\033[0m")

    return found

def custom_search(username, site_name, site_url):
    url = site_url.format(username)
    try:
        response = session.get(url, timeout=10)
        if response.status_code == 200:
            print(f"\033[92m{site_name} - {url}\033[0m")
            print("Profil bulundu:", url)
            return True
        else:
            print(f"\033[91m{site_name} - {url} - Bulunamadı\033[0m")
            return False
    except requests.exceptions.RequestException as e:
        print(f"\033[91m{site_name} - {url} - Hata: {e}\033[0m")
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
    thread = Thread(target=find_user, args=(username,))
    thread.start()
    thread.join()

def find_email(email):
    found = False
    email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    sites = {
        "Gravatar": f"https://www.gravatar.com/{email_hash}",
        "Twitter": f"https://x.com/{email_hash}",
        "Instagram": f"https://www.instagram.com/{email_hash}",
        "Pornhub": f"https://www.pornhub.com/users/{email_hash}",
        "Amazon": f"https://www.amazon.com/gp/profile/amzn1.account.{email_hash}",
        "Roblox": f"https://www.roblox.com/search/users?keyword={email_hash}",
        "XHamster": f"https://nl.xhamster.com/categories/porn-for-women?username={email_hash}",
        "IXXX": f"https://www.ixxx.com/nl/a-z?username={email_hash}",
        "VaginaNL": f"https://vagina.nl/?username={email_hash}",
        "XVideos": f"https://www.xvideos.com/lang/nederlands?username={email_hash}",
        "Dak7": f"https://7dak.com/?username={email_hash}",
        "Domlepen": f"https://domlepen.com/?username={email_hash}",
        "Porncom": f"https://nl.porn.com/?username={email_hash}",
        "ThePornDude": f"https://theporndude.com/nl?username={email_hash}",
        "HDAbla": f"https://hdabla.net/?username={email_hash}",
        "Superporn": f"https://www.superporn.com/nl?username={email_hash}",
        "Pornoseyret": f"https://pornoseyret.net/gozluklu-uvey-annesiyle-birlikte-mutfakta-seks-vakti/?username={email_hash}",
        "SXVKT": f"https://sxvkt.online/?username={email_hash}",
        "31Vaxti": f"https://31vaxti.site/?username={email_hash}",
        "Facebook": f"https://www.facebook.com/{email_hash}",
        "Evooli": f"https://www.evooli.com/{email_hash}",
        "Upslut": f"https://upslut.com/{email_hash}",
        "Minecraft": f"https://www.minecraft.net/{email_hash}",
        "Telegram": f"https://t.me/{email_hash}",
        "TikTok": f"https://www.tiktok.com/@{email_hash}",
        "Snapchat": f"https://www.snapchat.com/add/{email_hash}",
        "WhatsApp": f"https://wa.me/{email_hash}",
        "eFootball": f"https://www.konami.com/efootball/{email_hash}",
        "CapCut": f"https://www.capcut.app/user/profile/{email_hash}",
        "YouTube": f"https://www.youtube.com/{email_hash}",
        "Twitch": f"https://www.twitch.tv/{email_hash}",
        "LinkedIn": f"https://www.linkedin.com/in/{email_hash}",
        "Pinterest": f"https://www.pinterest.com/{email_hash}",
        "SoundCloud": f"https://soundcloud.com/{email_hash}",
        "Tumblr": f"https://{email_hash}.tumblr.com",
        "Reddit": f"https://www.reddit.com/user/{email_hash}",
        "Discord": f"https://discord.com/users/{email_hash}",
        "Medium": f"https://medium.com/@{email_hash}",
        "Behance": f"https://www.behance.net/{email_hash}",
        "Vimeo": f"https://vimeo.com/{email_hash}",
        "Dribbble": f"https://dribbble.com/{email_hash}",
        "Stack Overflow": f"https://stackoverflow.com/users/{email_hash}",
        "DeviantArt": f"https://{email_hash}.deviantart.com",
    }

    for site, url in sites.items():
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                print(f"\033[92m{site} - {url} - Bulundu\033[0m")
                found = True
            else:
                print(f"\033[91m{site} - {url} - Bulunamadı\033[0m")
        except requests.exceptions.RequestException as e:
            print(f"\033[91m{site} - {url} - Hata: {e}\033[0m")

    return found

def main():
    check_dependencies()
    
    config = load_config()
    print("\033[94m--- 🔭User-Finder Başlatılıyor🔭 ---\033[0m")
    print(pyfiglet.figlet_format("User-Finder"))

    while True:
        print("\033[93mMade by protocolhere\033[0m")
        print("🔭Seçenekler🔭:")
        print("1. Kullanıcı adı ile arama yap")
        print("2. E-posta ile arama yap")
        print("3. Özelleştirilmiş arama yap")
        print("4. İstatistikleri görüntüle")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın (1-5): ")

        if choice == "1":
            username = input("Kullanıcı adını girin: ").strip()
            if validate_username(username):
                found = find_user(username)
                log_result(username, found)
            else:
                print("\033[93mGeçersiz kullanıcı adı. Lütfen tekrar deneyin.\033[0m")

        elif choice == "2":
            email = input("E-posta adresini girin: ").strip()
            if validate_email(email):
                found = find_email(email)
                log_result(email, found)
            else:
                print("\033[93mGeçersiz e-posta adresi. Lütfen tekrar deneyin.\033[0m")

        elif choice == "3":
            site_name = input("Site adını girin: ").strip()
            site_url = input("Site URL şablonunu girin (örnek: https://site.com/{username}): ").strip()
            username = input("Kullanıcı adını girin: ").strip()
            if validate_username(username):
                found = custom_search(username, site_name, site_url)
                log_result(f"{site_name} - {username}", found)
            else:
                print("\033[93mGeçersiz kullanıcı adı. Lütfen tekrar deneyin.\033[0m")

        elif choice == "4":
            display_statistics()

        elif choice == "5":
            print("\033[93mÇıkış yapılıyor...\033[0m")
            save_config(config)
            break

        else:
            print("\033[91mGeçersiz seçim. Lütfen 1-4 arasında bir seçim yapın.\033[0m")
            print("\033[93mMade by protocolhere\033[0m")
            print("\033[93mBye Bye 🧏\033[0m")

if __name__ == "__main__":
    main()
