class Hayvan: #PARENT
    def __init__(self, isim, yas): 
        self.isim = isim
        self.yas = yas 
    
    def ses(self): 
        print(f"{self.isim} diyor ki: Ben bir hayvanım!")  



class Kopek(Hayvan):  #CHILD
    def __init__(self, isim, yas, cins):
        super().__init__(isim,yas)
        self.cins = cins


    def havla(self): 
        print(f"{self.isim}havlıyor:hav-hav!")




at = Hayvan(isim="At", yas=5)
at.ses()
eşek = Hayvan("Eşek", 2)
eşek.ses()



"""tarçın = Kopek("Tarçın", 3)
tarçın.ses()
tarçın.havla()"""


"""karabaş = Kopek(cins = "Kangal")
karabaş.havla()"""


tarçın = Kopek("Tarçın", 3, "Ev köpeği")
tarçın.havla()