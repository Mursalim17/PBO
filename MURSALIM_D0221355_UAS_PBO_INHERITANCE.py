# NAMA  = MURSALIM
# NIM   = D0221355
# KELAS = INFORMATIKA_G

import sys
class BangunDatar:
    def hitung_luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.__sisi = sisi

    def hitung_luas(self):
        luas = self.__sisi * self.__sisi
        return luas

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.__alas = alas
        self.__tinggi = tinggi

    def hitung_luas(self):
        luas = 0.5 * self.__alas * self.__tinggi
        return luas

class Lingkaran(BangunDatar):
    def __init__(self, r):
        self.__r = r

    def hitung_luas(self):
        luas = 22/7 * self.__r * self.__r
        return luas

class BangunRuang:
    def hitung_volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        print("Kubus")
        self.__sisi = sisi

    def hitung_volume(self):
        volume = self.__sisi * self.__sisi * self.__sisi
        return volume

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        print("Balok")
        self.__panjang = panjang
        self.__lebar = lebar
        self.__tinggi = tinggi

    def hitung_volume(self):
        volume = self.__panjang * self.__lebar * self.__tinggi
        return volume
    
class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.__jari_jari = jari_jari
        self.__tinggi = tinggi
    
    def hitung_volume(self):
        volume = 22/7 * self.__jari_jari * self.__tinggi
        return volume

def BangunDatar():
    while (True):
        menu = ["1. Persegi",
                "2. Segitiga",
                "3. Lingkaran",
                "4. Menu awal",
                "0. exit"]
        for men in menu:
            print(men)
        pilihan = int(input("masukan pilihan [1/2/3/4]> "))
        if pilihan == 1:
            print("==== PERSEGI ====")
            sisi = int(input("masukan sisi persegi : "))
            persegi = Persegi(sisi)
            print("luas persegi = {}".format(persegi.hitung_luas()))
                
        elif pilihan == 2:
            print("==== SEGITGA ====")
            alas = int(input("masukan alas segitiga : "))
            tinggi = int(input("masukan tinggi segitiga : "))
            segitiga = Segitiga(alas, tinggi)
            print("luas segitiga = {}".format(segitiga.hitung_luas()))
        
        elif pilihan == 3:
            print("==== LINGKARAN ====")
            r = int(input("masukan jari-jari lingkaran : "))
            lingkaran = Lingkaran(r)
            print("luas lingkaran = {}".format(lingkaran.hitung_luas()))
            
        elif pilihan == 4:
            mainMenu()
        elif pilihan == 0:
            sys.exit()
        else:
            print("pilihan anda salah!!")
               
def BangunRuang():
    while (True):
        menu = ["1. Kubus",
                "2. Balok",
                "3. Tabung",
                "4. Menu awal",
                "0. exit"]
        for men in menu:
            print(men)
        pilihan = int(input("masukan pilihan [1/2/3/4/5]> "))
        if pilihan == 1:
            print("==== KUBUS ====")
            sisi = int(input("masukan sisi kubus : "))
            kubus = Kubus(sisi)
            print("volume kubus = {}".format(kubus.hitung_volume()))
        
        elif pilihan == 2:
            print("==== BALOK ====")
            panjang = int(input("masukan panjang balok : "))
            lebar = int(input("masukan lebar balok : "))
            tinggi = int(input("masukan tinggi balok : "))
            balok = Balok(panjang, lebar, tinggi)
            print("volume balok = {}".format(balok.hitung_volume()))
        
        elif pilihan == 3:
            print("==== TABUNG ====")
            r = int(input("masukan jari-jari tabung : "))
            tinggi = int(input("masukan tinggi tabung : "))
            tabung = Tabung(r, tinggi)
            print("volume tabung = {}".format(tabung.hitung_volume()))
        
        elif pilihan == 4:
            mainMenu()
        elif pilihan == 0:
            sys.exit()
        else:
            print("pilihan anda salah!!")
            
def mainMenu():
    while(True):
        menu = ["1. Bangun Datar",
                "2. Bangun Ruang",
                "0. exit"]
        for men in menu:
            print(men)
        pilihan = int(input("masukan pilihan [1/2/0]> "))
        if pilihan == 1:
            BangunDatar()
        elif pilihan == 2:
            BangunRuang()
        elif pilihan == 0:
            sys.exit()
mainMenu()
