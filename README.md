Son güncelleme tarihi:
22/06/2024|09:31

VPN kullanın yoksa çalışmaz!

⚠️GNU Affero Genel Kamu Lisansı v3.0 (AGPL-3.0). Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.⚠️

## Profile-Hunter

Profile-Hunter, belirli bir kullanıcı adını veya e-posta adresini farklı platformlarda arayarak bulmayı amaçlayan Python tabanlı bir araçtır. Bu araç, belirli bir kullanıcı adının veya e-posta adresinin mevcut olup olmadığını kontrol etmek için çeşitli web sitelerine HTTP istekleri gönderir.

## Gereksinimler:

Profile-Hunter'ı çalıştırmak için aşağıdaki Python modüllerini yüklemeniz gerekmektedir:

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
Profile-Hunter'ı yükleyin:

```
git clone https://github.com/NOBody0101001/Profile-Hunter
```
user-find'ı çalıştırın:

```
cd Profile-Hunter.py
```

```
python hunt.py
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
