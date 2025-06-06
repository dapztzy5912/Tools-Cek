
import requests
import os
import time
from colorama import Fore, init

init(autoreset=True)

def banner():
    os.system('clear')
    print(Fore.CYAN + '''
╔═╗┌─┐┬ ┬┬ ┬┌─┐┌─┐
║ ╦│ ││ ││ │├┤ └─┐
╚═╝└─┘└─┘└─┘└─┘└─┘
     MULTI TOOLS
''')
    print(Fore.YELLOW + '''
[1] Cek Cuaca
[2] Cek Username Sosmed
[3] Owner
[4] Keluar
''')

def cek_cuaca():
    os.system('clear')
    print(Fore.GREEN + "=== CEK CUACA ===")
    kota = input("Masukkan nama kota: ")
    url = f"https://wttr.in/{kota}?format=3"
    try:
        res = requests.get(url)
        print(Fore.CYAN + "\nHasil:")
        print(Fore.LIGHTWHITE_EX + res.text)
    except:
        print(Fore.RED + "Gagal mengambil data cuaca.")
    input(Fore.YELLOW + "\nTekan Enter untuk kembali ke menu...")

def cek_username():
    os.system('clear')
    print(Fore.GREEN + "=== CEK USERNAME ===")
    username = input("Masukkan username: ")

    platform_urls = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }

    print(Fore.CYAN + "\nHasil Pengecekan:")
    for platform, url in platform_urls.items():
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(Fore.RED + f"{platform}: TIDAK TERSEDIA ❌")
            elif r.status_code == 404:
                print(Fore.GREEN + f"{platform}: TERSEDIA ✅")
            else:
                print(Fore.YELLOW + f"{platform}: Tidak diketahui ⚠️")
        except:
            print(Fore.YELLOW + f"{platform}: Error koneksi")
    input(Fore.YELLOW + "\nTekan Enter untuk kembali ke menu...")

def owner():
    os.system('clear')
    print(Fore.MAGENTA + '''
====================
 Owner Tools by XdpzQ
====================
Nama    : XdpzQ
Asal    : SURABAYA
Status  : Wa😂
====================
''')
    input(Fore.YELLOW + "Tekan Enter untuk kembali ke menu...")

def main():
    while True:
        banner()
        pilih = input(Fore.LIGHTCYAN_EX + "Pilih menu (1/2/3/4): ")
        if pilih == "1":
            cek_cuaca()
        elif pilih == "2":
            cek_username()
        elif pilih == "3":
            owner()
        elif pilih == "4":
            print(Fore.GREEN + "Terima kasih telah menggunakan tools ini!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()
