## Türkçe
# Remotive & Tracker

## Proje Açıklaması

**Remotive** uygulaması, uzak bilgisayarınızı kontrol etmenizi sağlar. Kullanıcılar, uygulama aracılığıyla bilgisayarlarında çeşitli işlemleri gerçekleştirebilirler. **Tracker** uygulaması ise yüz ve göz hareketlerini izleyerek bilgisayarda eylemler yapmanıza olanak tanır. Remotive ve Tracker, birlikte çalışarak bilgisayar kontrolünü ve izlemeyi kolaylaştırır.

### Remotive Uygulaması

**Remotive**, bilgisayarınızı uzaktan kontrol etmenize olanak tanır. Firebase Realtime Database aracılığıyla komutları alır ve bunlara göre işlemler yapar. 

#### Özellikler

- Bilgisayar ekranından anlık görüntü alma
- Ses seviyesini artırma veya azaltma
- Uygulamaları kapatma
- Bilgisayarı kapatma veya yeniden başlatma
- Fare hareketlerini ve tıklamaları kontrol etme
- Göz hareketlerini izlemek için Tracker'ı başlatma

### Tracker Uygulaması

**Tracker**, göz hareketlerini ve yüz ifadelerini izleyerek bilgisayarda eylemler yapmanızı sağlar. Bu uygulama, yüz ve göz algılamayı kullanarak hareketleri tespit eder ve belirtilen eylemleri gerçekleştirir.

#### Özellikler

- Yüz algılama
- Göz algılama
- Göz merkezleme ve fare hareketleri
- Ekran tıklamaları

### Kurulum ve Kullanım

1. **Remotive Uygulamasını Çalıştırma**
   - `remotiveSon.py` dosyasını çalıştırarak Remotive uygulamasını başlatın.
   - Python 3 ve gerekli kütüphaneler (`requests`, `pyautogui`, `Pillow`, `qrcode`, `colorama`, `tkinter`) yüklü olmalıdır.
   - Firebase Realtime Database URL ve diğer yapılandırmaları kod içinde belirlemeniz gerekmektedir.

2. **Tracker Uygulamasını Çalıştırma**
   - `tracker.py` dosyasını çalıştırarak Tracker uygulamasını başlatın.
   - Python 3 ve gerekli kütüphaneler (`cv2`, `numpy`, `pyautogui`) yüklü olmalıdır.
   - Göz ve yüz algılama için uygun `haarcascade` dosyalarının mevcut olması gerekmektedir.

3. **Remotive Mobile Uygulaması**
   - **RemotiveMobile.apk** dosyasını Android cihazınıza yükleyin.
   - Uygulama, Remotive ile aynı Firebase Realtime Database'i kullanarak bilgisayarınıza bağlanabilir.

### Gereksinimler

- Python 3
- Gerekli Python kütüphaneleri
- Firebase Realtime Database
- Haarcascades dosyaları (Tracker için)

### Notlar

- **Remotive** ve **Tracker** uygulamaları, ayrı ayrı çalıştırılabilir veya birlikte kullanılabilir.
- **Remotive**'un çalışması için doğru Firebase yapılandırmasını yapmanız gerekmektedir.
- **Tracker** için `haarcascade` dosyalarının doğru şekilde yüklenmiş olması önemlidir.

### Katkıda Bulunanlar

- Emr - Proje Geliştiricisi



## English

# Remotive & Tracker

## Project Description

**Remotive** is an application that allows you to control your computer remotely. Users can perform various tasks on their computers through the app. **Tracker** is an application that tracks face and eye movements, enabling actions on the computer. Remotive and Tracker work together to simplify computer control and monitoring.

### Remotive Application

**Remotive** enables remote control of your computer. It receives commands via Firebase Realtime Database and performs actions based on those commands.

#### Features

- Capture screenshots from the computer
- Adjust the volume up or down
- Close applications
- Shut down or restart the computer
- Control mouse movements and clicks
- Start Tracker for eye movement monitoring

### Tracker Application

**Tracker** allows you to perform actions on the computer by tracking eye movements and facial expressions. This application uses face and eye detection to detect movements and execute specified actions.

#### Features

- Face detection
- Eye detection
- Eye centering and mouse movements
- Screen clicks

### Installation and Usage

1. **Running the Remotive Application**
   - Run the `remotiveSon.py` file to start the Remotive application.
   - Python 3 and necessary libraries (`requests`, `pyautogui`, `Pillow`, `qrcode`, `colorama`, `tkinter`) must be installed.
   - Firebase Realtime Database URL and other configurations need to be set in the code.

2. **Running the Tracker Application**
   - Run the `tracker.py` file to start the Tracker application.
   - Python 3 and necessary libraries (`cv2`, `numpy`, `pyautogui`) must be installed.
   - Haar cascade files for face and eye detection must be available.

3. **Remotive Mobile Application**
   - Install the **RemotiveMobile.apk** file on your Android device.
   - The app can connect to your computer using the same Firebase Realtime Database as Remotive.

### Requirements

- Python 3
- Required Python libraries
- Firebase Realtime Database
- Haar cascade files (for Tracker)

### Notes

- **Remotive** and **Tracker** can be run separately or together.
- **Remotive** requires correct Firebase configuration to function.
- Ensure that `haarcascade` files are correctly placed for **Tracker** to work properly.

### Contributors

- Emr - Project Developer
