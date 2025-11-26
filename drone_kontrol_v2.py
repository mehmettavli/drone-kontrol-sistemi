# =====================================
# DRONE KONTROL SİSTEMİ V2.0
# Fonksiyonlarla Tam Düzenlenmiş Sürüm
# =====================================

def sistem_baslat():
    print("=" * 50)
    print(" DRONE KONTROL SİSTEMİ V3.0")
    print("=" * 50)
    print(" Sistem kontrolleri yapılıyor...")
    print(" Motor: OK")
    print(" GPS: OK")
    print(" Kamera: OK")
    print(" Batarya: OK")
    print()

def batarya_hesapla(mesafe):
    return (mesafe / 10) * 2

def kalkis_yap(hedef_yukseklik, batarya):
    print(" AŞAMA 1: KALKIŞ")
    print("-" * 50)

    yukseklik = 0
    for h in range(0, hedef_yukseklik + 1, 10):
        yukseklik = h
        batarya -= 2
        print(f" Yükseklik: {yukseklik}m | Batarya: %{batarya}")

    print(" Hedef yüksekliğe ulaşıldı!\n")
    return batarya, yukseklik

def gorev_uc(batarya, yonler):
    print(" AŞAMA 2: GÖREV UÇUŞU")
    print("-" * 50)

    gorev_suresi = 0

    for yon in yonler:
        if batarya <= 30:
            print(" Batarya kritik! Görev sonlandırılıyor.\n")
            break

        gorev_suresi += 1
        batarya -= 3
        print(f" {yon} | {gorev_suresi}s | %{batarya} | 📷 Görüntü alındı")

    print()
    return batarya, gorev_suresi

def acil_durum_kontrol(batarya, yukseklik):
    print(" AŞAMA 3: ACİL DURUM KONTROLÜ")
    print("-" * 50)

    if 30 <= batarya <= 100 and yukseklik <= 300:
        print("Acil Durum Yok.\n")
        return False  # acil değil
    
    if batarya < 30 or yukseklik > 500:
        print("⚠ ACİL DURUM TESPİT EDİLDİ! ACİL İNİŞ GEREKLİ!\n")
        return True   # acil iniş gerekli

    print("Batarya değeri 0–100 arasında olmalıdır.\n")
    return True

def inis_yap(yukseklik, batarya, acil=False):
    if acil:
        print(" ACİL İNİŞ")
        inis_hizi = 20
    else:
        print(" AŞAMA 4: NORMAL İNİŞ")
        inis_hizi = 10

    print("-" * 50)

    while yukseklik > 0:
        yukseklik -= inis_hizi
        batarya -= 1

        if yukseklik < 0:
            yukseklik = 0

        print(f" Yükseklik: {yukseklik}m | Batarya: %{batarya}")

    print(" İniş tamamlandı!\n")
    return batarya

def gorev_raporu(baslangic, son, gorev_suresi):
    print(" GÖREV RAPORU")
    print("=" * 50)
    print(f" Başlangıç bataryası: %{baslangic}")
    print(f" Kalan batarya: %{son}")
    print(f" Harcanan batarya: %{baslangic - son}")
    print(f" Toplam görev süresi: {gorev_suresi}s")
    print("=" * 50)


# =====================================
# ANA PROGRAM
# =====================================

sistem_baslat()

batarya = 100
baslangic_batarya = batarya
hedef_yukseklik = 50
yonler = ["Kuzey", "Doğu", "Doğu", "Kuzey", "Batı", "Batı", "Güney"]

# 1. Kalkış
batarya, yukseklik = kalkis_yap(hedef_yukseklik, batarya)

# 2. Görev uçuşu
batarya, sure = gorev_uc(batarya, yonler)

# 3. Acil durum kontrol
acil_mi = acil_durum_kontrol(batarya, yukseklik)

# 4. İniş
batarya = inis_yap(yukseklik, batarya, acil=acil_mi)

# 5. Rapor
gorev_raporu(baslangic_batarya, batarya, sure)
