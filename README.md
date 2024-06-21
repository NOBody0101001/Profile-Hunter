Son güncelleme tarihi:
21/06/2024|22:15

Eğer hata alıyorsanız VPN kullanın!

⚠️GNU Affero Genel Kamu Lisansı v3.0 (AGPL-3.0). Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.⚠️

## user-finder

user-finder, belirli bir kullanıcı adını veya e-posta adresini farklı platformlarda arayarak bulmayı amaçlayan Python tabanlı bir araçtır. Bu araç, belirli bir kullanıcı adının veya e-posta adresinin mevcut olup olmadığını kontrol etmek için çeşitli web sitelerine HTTP istekleri gönderir.

## Gereksinimler:

user-finder'ı çalıştırmak için aşağıdaki Python modüllerini yüklemeniz gerekmektedir:

• requests
• pyfiglet

Bu modüller, HTTP istekleri göndermek ve ASCII sanatı oluşturmak için kullanılmaktadır.

## Kurulum

• Python Sürümü: Python 3.6 veya üzeri bir sürümünün yüklü olduğundan emin olun.

Termux:

```
pkg install python
```

Linux:

```
sudo apt install python3 python3-pip
```
## yada bu
Linux:

```
sudo dnf install python3 python3-pip
```


• Bağımlılıkların Yüklenmesi: Gerekli bağımlılıkları yüklemek için terminal veya komut istemcisinde aşağıdaki komutları çalıştırın:

```
pip install requests pyfiglet
```
user-find'ı yükleyin:

```
git clone https://github.com/NOBody0101001/user-find
```
user-find'ı çalıştırın:

```
python find.py
```

## Kullanım

• 1: Kullanıcıyı Bul: 
Belirli bir kullanıcı adını arayarak bulun.

• 2: Özel Arama Yap: 
Henüz uygulamaya eklenmemiş özel arama işlevleri.

• 3: İstatistikleri Görüntüle: 
Yapılan arama istatistiklerini görüntüle.

• 4: E-posta ile Arama: 
Belirli bir e-posta adresini arayarak bulun.

• 5: Programdan Çıkış: 
Programı sonlandır.

## Lisans

⚠️GNU Affero Genel Kamu Lisansı v3.0 (AGPL-3.0). Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.⚠️
