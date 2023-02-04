#!/usr/bin/python3
import random
import time
import os

print("""
 _       ___ _____       ___         __      
| |     / (_) __(_)     /   | __  __/ /_____ 
| | /| / / / /_/ /_____/ /| |/ / / / _ / __ /
| |/ |/ / / __/ /_____/ ___ / /_/ / /_/ /_/ /
|__/|__/_/_/ /_/     /_/  |_\__,_/\__/\____/
                                                            Github: https://github.com/alp1903
""")
print("      --(:HELLO WORLD:)--")

ad = input("[+] Kişinin Adı >>")
file = open(ad+".txt", "a")
soyad = input("[+] Kişinin Soyadı >>")
dtarih = input("[+] Kişinin Doğum Tarihi >>")
adk = input("[+] Kişinin Ad Kısaltması >>")
soyadk = input("[+] Kişinin Soyad Kısaltması >>")
tkm = input("[+] Kişinin Tuttuğu Takım >>")
th = input("[+] Kişinin Tuttuğu Takım`ın tarihi >>")
pkod = input("[+] Kişinin Şehrin Plaka Kodu >>")
hyvn = input("[+] Kişinin Hayvanının Adı >>")
teln = input("[+] Kişinin telefon nosu >>")
anahtar1 = input("[+] Kişi Hakkında Anahtar Kelime >>")
anahtar2 = input("[+] Kişi Hakkında Anahtar Kelime >>")
anahtar3 = input("[+] Kişi Hakkında Anahtar Kelime >>")
anahtarr1 = input("[+] Kişi Hakkında Anahtar Rakam >>")
anahtarr2 = input("[+] Kişi Hakkında Anahtar Rakam >>")
anahtarr3 = input("[+] Kişi Hakkında Anahtar Rakam >>")
print("")
print("[!] İşlem Tamamlanıyor Lütfen Bekleyiniz")
time.sleep(0.7)
print("[!] Bilgiler Sisteme Kaydediliyor")
time.sleep(0.7)
print("[!] İşlem Tamamlandı")
time.sleep(0.3)
#Alp
liste = [ad, soyad, dtarih, adk, soyadk, tkm, pkod, hyvn, anahtar1, anahtar2, anahtar3, anahtarr1, anahtarr2, anahtarr3, th, teln]
print("[!] Lütfen 3 Saniye Bekleyiniz")
time.sleep(0.3)
op = 1
while op <= 1200:
	print(random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + "\n")
	print(random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + "\n")
	print(random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + "\n")
	print(random.choice(liste) + random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + random.choice(liste) + "\n")
	print(random.choice(liste) + random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + random.choice(liste) + "\n")
	print(random.choice(liste) + random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + random.choice(liste) + "\n")
	print(random.choice(liste) + random.choice(liste) + random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + random.choice(liste) + random.choice(liste) + "\n")
	print(random.choice(liste) + random.choice(liste) + random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + random.choice(liste) + random.choice(liste) + "\n")
	print(random.choice(liste) + random.choice(liste) + random.choice(liste) + random.choice(liste))
	file.writelines(random.choice(liste) + random.choice(liste) + random.choice(liste) + random.choice(liste) + "\n")
	op = op + 1

file.close()
os.system("clear")
os.system("sort -u {}.txt | uniq >> {}1.txt".format(ad, ad))
os.system("rm {}.txt".format(ad))
