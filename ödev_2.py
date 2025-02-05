class kitap:
    def __init__(self, adi, yazari, sayfa_sayisi, isbn):
        self.adi = adi
        self.yazari = yazari
        self.sayfa_sayisi = sayfa_sayisi
        self.isbn = isbn
       
    def __str__(self):
        return f"{self.adi} - {self.yazari} ({self.sayfa_sayisi} sayfa) (ISBN: {self.isbn})"

class kutuphane:
    def __init__(self):
        self.kitaplar = []  #Liste oluşturduk kitaplar için
    
    def kitap_ekle(self, kitap):
        # ISBN listede var mı kontrol için
        for mevcut_bulunan_kitap in self.kitaplar:
            if mevcut_bulunan_kitap.isbn == kitap.isbn:
                print(f"Bu ISBN numarasıyla başka bir kitap zaten var: {kitap}")
                return 
        self.kitaplar.append(kitap)
        print(f"Kitap eklendi: {kitap}")
    
    def kitap_sil(self, isbn):
        kitap_bulundu = False
        #ISBN'ye sahip kitabı bulup silmek için kontrol eder burda
        for kitap in self.kitaplar:
            if kitap.isbn == isbn:
                self.kitaplar.remove(kitap)
                print(f"Kitap silindi: {kitap}")
                kitap_bulundu = True
                break  # Kitabı buldu sonra sildi
        
            else:   
               print(f"HATA: Bu ISBN numarasına sahip bir kitap bulunamadı: {isbn}")
    
    def kitaplari_goster(self):
        if self.kitaplar==0:
            print("Kütüphane şu anda boş.")
        else:
            print("Kütüphanedeki Kitaplar:")
            for kitap in self.kitaplar:
                print(kitap)


kutuphane = kutuphane()

kitap1 = kitap("abc", "Selen Gök", 4123, "123456789")
kitap2 = kitap("abd", "Mehmet Öz", 300, "987654321")

kutuphane.kitap_ekle(kitap1)  # İlk kitabı ekledim
kutuphane.kitap_ekle(kitap2)  # İkinci kitabı ekledim
kutuphane.kitap_ekle(kitap1)  # Aynı ISBN'ye sahip kitap tekrar eklenmeye çalışılınca hata verecek burada

kutuphane.kitaplari_goster()

kutuphane.kitap_sil("123456789")  
kutuphane.kitap_sil("000000001123")  

kutuphane.kitaplari_goster()
