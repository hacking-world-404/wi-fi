#------------- IMPORT ------------#
from os import system as c
import time
import random

#---------------- COLOUR ----------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'

#---------------- LOGO ----------------#
def logo():
    c('clear')
    print(f"""{C}
  ▄▄▄▄▄  ▄▄▄▄▄  ▄▄▄▄▄ 
 ▐█   █▌▐█   █▌▐█    
 ▐█▀▀▀  ▐█▀▀▀  ▐█▀▀▀ 
 ▐█     ▐█     ▐█▄▄▄ 
                    
{Y}         HACKING WORLD  WIFI TOOL
""")

#---------------- MAIN MENU ----------------#
def menu():
    logo()
    print(f"{A}[1] WIFI PASSWORD HACK")
    print(f"{A}[2] WIFI MAC ADDRESS BYPASS")
    print(f"{A}[0] EXIT")
    print(f"{A}---------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        wifi_hack()
    elif choice == '2':
        mac_bypass()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION")
        time.sleep(1)
        menu()
#---------------- WIFI HACK ----------------#
def wifi_hack():
    logo()
    c('espeak "Starting WiFi Password Hack"')
    target = input(f"{C}ENTER WIFI NAME (SSID): ")
    print(f"{Y}[+] Searching for {target} ...")
    time.sleep(2)
    print(f"{G}[✓] Network Found!")
    time.sleep(1)
    print(f"{Y}[+] Starting Bruteforce Attack...")
    time.sleep(2)
    passwords = ['9808261','8096279','admin123','hackme123','wifi2024']
    for pw in passwords:
        print(f"{C}[*] Trying Password: {pw}")
        time.sleep(1)
    time.sleep(1)
    fake_pass = "wifi2025@@"
    print(f"{G}[✓] Password Found: {fake_pass}")
    input(f"{Y}Press Enter To Go Back...")
    menu()

#--------------- MAC BYPASS ----------------#
def mac_bypass():
    logo()
    c('espeak "Starting MAC Address Bypass"')
    print(f"{Y}[+] Changing MAC Address...")
    time.sleep(2)
    new_mac = f"00:1A:C2:{random.randint(10,99)}:{random.randint(10,99)}:{random.randint(10,99)}"
    print(f"{G}[✓] New MAC: {new_mac}")
    input(f"{Y}Press Enter To Go Back...")
    menu()

#---------------- START ----------------#
menu()