import tkinter as tk
import requests
import socket
import pyautogui
import time
import os
import pyautogui
import http.server
import socketserver
import threading
import urllib3
import subprocess
import re
from colorama import Fore
import qrcode
from tkinter import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

previous_response = None

def read_from_firebase():
    url = "YOUR_FIREBASE_URL/" + ip_without_dots + ".json"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        return None

httpd = None
global kullaniciad
kullaniciad= os.getlogin()
global kurulumpath
kurulumpath = os.path.abspath("remotive.exe").replace("\\" , "/").replace("/remotive.exe" , "")

def controlscreen():
    main_thread.join()

    def get_current_wifi_ssid():
        try:
            result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
            output = result.stdout
            ssid_match = re.search(r'SSID\s+: (.+)', output)
            if ssid_match:
                return ssid_match.group(1).strip()
            else:
                return None
        except Exception as e:
            print("SSID alınamadı:", e)
            return None

    ssid = get_current_wifi_ssid()
    if ssid:
        print(Fore.GREEN + "Make sure that your phone is connected to that network: " , ssid)


    global httpd  

    if os.path.exists( kurulumpath + '/screenshot.png'):
        os.remove(kurulumpath + '/screenshot.png')

    screenshot = pyautogui.screenshot()
    screenshot.save(kurulumpath + '/screenshot.png')

    link = f"http://{socket.gethostbyname(socket.gethostname())}:8080/screenshot.png"
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)
    httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.start()

    print(f"Serving at {link}")
    time.sleep(7)

    httpd.shutdown()
    httpd.server_close()

    print("Token expired. Try to request again...")

    server_thread.join()

def update_data_labels():

    global previous_response
    firebase_data = read_from_firebase()

    if firebase_data:
        text_label.config(text=f"Connected")

        if firebase_data == '"left"':
            pyautogui.moveRel(-30, 0)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"doubleleft"':
            pyautogui.moveRel(-90, 0)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"volumeup"':
            pyautogui.press("volumeup" , 5)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"volumedown"':
            pyautogui.press("volumedown" , 5)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"altf4"':
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"right"':
            pyautogui.moveRel(30, 0)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"doubleright"':
            pyautogui.moveRel(90, 0)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"up"':
            pyautogui.moveRel(0, -30)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"doubleup"':
            pyautogui.moveRel(0, -90)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"down"':
            pyautogui.moveRel(0, 30)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"doubledown"':
            pyautogui.moveRel(0, 30)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"leftclick"':
            pyautogui.click()
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"doubleleftclick"':
            pyautogui.click(clicks=2)
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"rightclick"':
            pyautogui.rightClick()
            time.sleep(0.1)
            update_response_in_firebase('   ')
            previous_response = firebase_data

        if firebase_data == '"close"':
            update_response_in_firebase('   ')
            previous_response = firebase_data
            time.sleep(0.1)
            root.destroy()

        if firebase_data == '"link"':
            update_response_in_firebase('   ')
            previous_response = firebase_data
            controlscreen()

        if firebase_data == '"shutdown"':
            update_response_in_firebase('   ')  
            previous_response = firebase_data
            os.system("shutdown /s /t 10") 

        if firebase_data == '"restart"':
            update_response_in_firebase('   ')  
            previous_response = firebase_data
            os.system("shutdown /r /t 5") 

        if firebase_data == '"eyetrack"':
            update_response_in_firebase('   ')  
            previous_response = firebase_data
            pyautogui.keyDown('winleft')
            pyautogui.press('r')
            pyautogui.keyUp("winleft")
            pyautogui.write(kurulumpath + '/track2.exe')
            pyautogui.press('enter')

        elif "ꜳ" in firebase_data:
            x = firebase_data.replace("ꜳ", "")
            pyautogui.write(x.replace('"', ""))
            update_response_in_firebase('   ')
            previous_response = firebase_data
        
    else:
        text_label.config(text="Could not get command.")

    password_label.config(text=f"Your Password: {ip_without_dots}")

    root.after(500, update_data_labels)

def update_response_in_firebase(new_response):
    url = "https://remote-fa090-default-rtdb.firebaseio.com/" + ip_without_dots + ".json"
    requests.put(url, json=new_response, verify=False)

def main():
    global root
    global ip_without_dots
    root = tk.Tk()
    root.title("Remotive Client")
    dosya_adi = 'remotivelogo.png'
    ana_dizin = os.path.expanduser("~")

    def dosya_bul(dosya_adi, ana_dizin):
        for root, dirs, files in os.walk(ana_dizin):
            if dosya_adi in files:
                dosya_yolu = os.path.join(root, dosya_adi)
                return dosya_yolu
        return None

    dosya_yolu = dosya_bul(dosya_adi, ana_dizin)

    if dosya_yolu:
        img = tk.PhotoImage(file=dosya_yolu)
        root.tk.call('wm', 'iconphoto', root._w, img)

    window_width = 300
    window_height = 750
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.resizable(width=False, height=False)

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    root.configure(bg="#8ab888") 

    global text_label
    text_label = tk.Label(root, text="", font=("Helvetica", 14), padx=20, pady=10, fg="black", bg="#567e56")
    
    global password_label
    password_label = tk.Label(root, text=f"Your Password: {ip_without_dots}", font=("Helvetica", 12), padx=20, pady=10, fg="black", bg="#567e56")

    iplabel = tk.Label(root, text=f"Your Local IP: {socket.gethostbyname(socket.gethostname())}", font=("Helvetica", 12), padx=20, pady=10, fg="black", bg="#567e56")

    update_data_labels()

    text_label.pack(expand=True)

    password_label.pack(expand=False)

    img = qrcode.make(ip_without_dots)
    type(img)
    img.save(kurulumpath + "/qrcode.png")
    sunset_resized = img.resize((100, 100))
    sunset_resized.save(kurulumpath + '/qrcode.png')
    canvas = Canvas(root, width = 247, height = 110 , bg="#567e56" , highlightthickness=0)
    canvas.pack()
    qr_image = PhotoImage(file="qrcode.png")
    canvas.create_image(123.5 ,55 , anchor=CENTER, image=qr_image)
    os.remove(kurulumpath + "/qrcode.png")
    
    iplabel.pack(expand=True)

    img2 = qrcode.make(socket.gethostbyname(socket.gethostname()))
    type(img2)
    img2.save(kurulumpath + "/qrcode2.png")
    sunset_resized2 = img2.resize((100, 100))
    sunset_resized2.save(kurulumpath + '/qrcode2.png')
    canvas2 = Canvas(root, width = 245, height = 109 , bg="#567e56" ,  highlightthickness=0)
    canvas2.pack()
    qr_image2 = PhotoImage(file="qrcode2.png")
    canvas2.create_image(123.5 , 55 , anchor=CENTER, image=qr_image2)
    canvas2.place(y=610 , x=27)
    os.remove(kurulumpath + "/qrcode2.png")

    global main_thread
    main_thread = threading.Thread(target=update_data_labels)
    main_thread.start()

    root.mainloop()

if __name__ == "__main__":
    ip_without_dots = socket.gethostbyname(socket.gethostname()).replace(".", "")
    main()

#pyinstaller --onefile --icon=C:\Users\Emir\Desktop\RemoteControl\remotivelogo.png C:\Users\Emir\Desktop\Masaüstü\Kodlama\Projeler\remotiveSon.py
