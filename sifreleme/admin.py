class Admin:
    sifreler=[]
    def __init__(self,isim,sifre):
        self.isim=isim
        self.sifre=sifre
        self.sifre_ekle()
        self.sifrelileri_listele()

    def sifre_ekle(self):
        Admin.sifreler.append("klasörün adı:"+str(self.isim)+"---sifresi: "+str(self.sifre))

    @classmethod
    def sifrelileri_listele(cls):
        print(cls.sifreler)
