import subprocess
from admin import Admin
root='190323'
path = '/home/oktay'
klasör=input("sifrelemek istediginiz klasör :")
sifre=input("root sifrenizi giriniz :")
if(sifre==root):
    print("Şifre Doğru")
    c1=Admin(klasör,sifre)
    subprocess.check_call(['xdg-open', path])
else:
    print("Sonuc Yanlış")

Admin.sifrelileri_listele()
