from abc import ABC, abstractmethod

class Hayvon(ABC):
    @abstractmethod
    def ovoz_ber(self):
        pass  # Bu yerda faqat strukturasi bo'ladi, ishlashi yo'q

class It(Hayvon):
    def ovoz_ber(self):
        print("Vov-vov!")

class Mushuk(Hayvon):
    def ovoz_ber(self):
        print("Miyav!")

# Obyektlar yaratish va chaqirish
it = It()
it.ovoz_ber()

mushuk = Mushuk()
mushuk.ovoz_ber()


