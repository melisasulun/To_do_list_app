# Görevleri saklamak için liste
gorevler = []     #global değişken

def menu():
    while True:
        print("\n--- GÖREV YÖNETİMİ ---")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görev Düzenle")
        print("4. Görev Sil")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın (1-5): ")

        if secim == "1":
            gorevleri_listele() 
        elif secim == "2":
            gorev_ekle()
        elif secim == "3":
            gorev_duzenle()
        elif secim == "4":
            gorev_sil()
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")

# Dosyadan görevleri oku
def gorevleri_yukle():
    global gorevler
    try:
        with open("veriler/gorevler.txt", "r", encoding="utf-8") as dosya:  #"r":read : okumak
            print("Dosya bulundu, veriler çekiliyor")
            gorevler = [satir.strip() for satir in dosya.readlines()]
    except FileNotFoundError:
        print("Dosya Bulunamadı")
        gorevler = []  # Dosya yoksa boş liste ile başla

def gorevleri_kaydet():
    try:
        with open("veriler/gorevler.txt", "w", encoding="utf-8") as dosya:
            for gorev in gorevler:
                dosya.write(gorev + "\n")
    except Exception as e:              # Exception : hata
        print("Görevler kaydedilirken hata oluştu:", e)

def gorevleri_listele():
    if not gorevler:  # Liste boş mu?
        print("Hiç görev bulunmamaktadır.")
    else:
        print("\n--- GÖREV LİSTESİ ---")
        for i, gorev in enumerate(gorevler, start=1):   #enumerate: herhangi bir sayıdan başlatmak için kullanılır
            print(f"{i}. {gorev}")

def gorev_ekle():
    yeni_gorev = input("Yeni görev girin: ").strip()
    if yeni_gorev:  # Boş değilse
        gorevler.append(yeni_gorev)
        gorevleri_kaydet()
        print("Görev eklendi.")
    else:
        print("Görev boş olamaz!")

def gorev_duzenle():
    gorevleri_listele()
    if not gorevler:
        return  # Görev yoksa çık

    try:
        numara = int(input("Düzenlemek istediğiniz görev numarasını girin: "))
        if 1 <= numara <= len(gorevler):
            yeni_gorev = input("Yeni görev metnini girin: ").strip()   #strip: özel karakterleri sil
            if yeni_gorev:
                gorevler[numara - 1] = yeni_gorev  # Listedeki görevi güncelle
                gorevleri_kaydet()
                print("Görev başarıyla düzenlendi.")
            else:
                print("Görev boş olamaz!")
        else:
            print("Geçersiz görev numarası!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def gorev_sil():
    gorevleri_listele()
    if not gorevler:
        return  # Görev yoksa çık

    try:
        numara = int(input("Silmek istediğiniz görev numarasını girin: "))
        if 1 <= numara <= len(gorevler):
            silinen = gorevler.pop(numara - 1)  # Görevi listeden sil
            gorevleri_kaydet()
            print(f"'{silinen}' görevi silindi.")
        else:
            print("Geçersiz görev numarası!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")


# Program başlangıcı
gorevleri_yukle()
menu()
