#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto import Random
import sys
import os
import struct
from pip.backwardcompat import raw_input
#import QtLocation 5.3

def encrypt():
    yol ="/home/oktay/d/a.txt";
    dosya = yol;
    kelime='docx';
    dosya_uzantisi = dosya + ".enc"
    baslangic_vektoru = Random.new().read(AES.block_size)
    aes_modu = AES.MODE_CBC
    key = "abcde12345f6g7h8"
    encryptor = AES.new(key,aes_modu, baslangic_vektoru)
    karakter_sayisi = os.path.getsize(dosya) 

    with open(dosya, 'rb') as sifrelencek_dosya:
        with open(dosya_uzantisi, 'wb') as sifreli_dosya:
            sifreli_dosya.write(struct.pack("<Q",karakter_sayisi))
            sifreli_dosya.write(baslangic_vektoru)

            while True:
                for i in range(0,len(dosya)):
                    if kelime in dosya:
                        chunk = sifrelencek_dosya.read(64)
                        length = len(chunk)
                        if length == 0:
                            break
                        elif length % 16 != 0:
                            chunk += ' ' * (16 - length % 16)

                        sifreli_dosya.write(encryptor.encrypt(chunk))
                    else:
                        chunk = sifrelencek_dosya.read(64).decode('utf-8')
                        length = len(chunk)
                        if length == 0:
                            break
                        elif length % 16 != 0:
                            chunk += ' ' * (16 - length % 16)

                        sifreli_dosya.write(encryptor.encrypt(chunk))

def decrypt():
    yol ="/home/oktay/d/a.txt.enc";
    dosya = yol;
    aes_modu = AES.MODE_CBC
    key =  "abcde12345f6g7h8"
    outname = dosya[:-4]

    with open(dosya, 'rb') as sifreli_dosya:
        karakter_sayisi = struct.unpack('<Q', sifreli_dosya.read(struct.calcsize('Q')))[0]
        baslangic_vektoru = sifreli_dosya.read(AES.block_size)
        decryptor = AES.new(key, aes_modu, baslangic_vektoru)

        with open(outname, 'wb') as yeni_dosya:
            while True:
                chunk = sifreli_dosya.read(64)
                if len(chunk) == 0:
                    break
                yeni_dosya.write(decryptor.decrypt(chunk))

            yeni_dosya.truncate(karakter_sayisi)

encOrDec = raw_input("şifreleme için 1, şifreyi kaldırmak için 2 : ")
if encOrDec == '1':
    encrypt()
elif encOrDec == '2':
    decrypt()
else:
    print ("Geçerli bir seçim değil")
    sys.exit(1)
