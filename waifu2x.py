import requests, urllib, json
from urllib import request
import time
import socket
#------ Yang Recode Dosa, gw gak terima ini direcode kecuali izin dan ingin mengembangkannya -------------#

def information():
    print("Coded By Xnuvers007")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print(f"Hostname / Nama perangkat mu : {hostname}")
    print(f"IP Addressmu Adalah : {ip_address}\n")
    print("============================")
    warn = "file / foto yang sudah dijernihkan akan tersimpan dimana kamu meletakan aplikasi ini".upper()
    print(warn)
    print("============================\n")
    input("Press enter to continue...")

def menu():
    print("============= List Menu ===============\n")
    print("1. Menjernihkan foto via Link/Url")
    print("2. Menjernihkan foto via Foto yang sudah disimpan di komputer/hp")
    print("CTRL + C = Exit/Quit/Keluar")
    try:
        pilih = int(input("Masukan Pilihan : "))
        print("\n")
        if pilih==1:
            uerel()
        elif pilih==2:
            local()
        else:
            print("Tidak ada di menu akan mengulang kembali")
            print("Akan mengulang dalam waktu 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(1)
                print(i)
            menu()
    except KeyboardInterrupt or ValueError:
        print("Akan Keluar dalam ...")
        for i in range(1,4):
            i += 0
            print(i)
        exit(code=None)

def uerel():
    url = input("Masukan Url Gambar : ")
    r = requests.post("https://api.deepai.org/api/waifu2x",
                        data={'image':url,
                            },
                        headers={'api-key':'6bb16995-6df5-4b3d-a4b7-f0973f56ea82'}
                        #headers={'api-key':'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    r_dict = r.json()
    link = r_dict['output_url']
    print("\nSalin Linknya...!!! : "+link+"\n")
    print("Terus Tempel Lagi untuk jernihin...\n")
    i = str(input("Ingin menjernihkan lagi ? [Y/n] n/N = Langsung Download : "))
    if i=='Y' or i=='y':
        uerel()
    elif i=='n' or i=='N':
        down = requests.get(link, allow_redirects=True)
        nama = input("Masukan nama File : ")
        bertanya = input("Jpg [J] atau Png [P] ? : ")
        if bertanya=='j' or bertanya=='J':
            open(nama+".jpg", 'wb').write(down.content)
            print("Sudah Terdownload !!!")
        elif bertanya=='P' or bertanya=='p':
            open(nama+".png", 'wb').write(down.content)
            print("Sudah Terdownload !!!")
        else:
            print("Tidak Ditemukan")
            print("Akan Keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                print(i)
                time.sleep(1)
            exit(code=None)
    else:
        print("Not Found")
        print("Akan Keluar dalam 3 detik")
        for i in range(1,4):
            i += 0
            print(i)
            time.sleep(1)
        exit(code=None)

def local():
    lofile = input("Silahkan letakan lokasi file foto yang ingin di jernihkan atau drag ke sini : ")
    r = requests.post(
        "https://api.deepai.org/api/waifu2x",
        files={
            'image': open(lofile, 'rb'),
            },
        #headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        headers={'api-key':'6bb16995-6df5-4b3d-a4b7-f0973f56ea82'}
        )
    r_dict = r.json()
    link = r_dict['output_url']
    print("\nSalin Linknya...!!! : "+link+"\n")
    print("Terus Tempel Lagi untuk jernihin...\n")
    i = str(input("Ingin menjernihkan lagi ? [Y/n] n/N = Langsung Download : "))
    if i=='Y' or i=='y':
        uerel()
    elif i=='n' or i=='N':
        down = requests.get(link, allow_redirects=True)
        nama = input("Masukan nama File : ")
        bertanya = input("Jpg [J] atau Png [P] ? : ")
        if bertanya=='j' or bertanya=='J':
            open(nama+".jpg", 'wb').write(down.content)
            print("Sudah Terdownload !!!")
        elif bertanya=='P' or bertanya=='p':
            open(nama+".png", 'wb').write(down.content)
            print("Sudah Terdownload !!!")
        else:
            print("Tidak Ditemukan")
            print("Akan Keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                print(i)
                time.sleep(1)
            exit(code=None)
    else:
        print("Not Found")
        print("Akan Keluar dalam 3 detik")
        for i in range(1,4):
            i += 0
            print(i)
            time.sleep(1)
        exit(code=None)


information()
menu()
