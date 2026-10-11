#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Koymadan Hiçbir Şey Yapmayan Algoritma
Bu kod, çay koyulmadan hiçbir işlemi kabul etmez.
Çünkü çay, evrenin temel yapı taşıdır.
"""

import time
import random
import sys

def cay_kontrol():
    print("Çay koyuluyor mu kontrol ediliyor...")
    time.sleep(2)
    cevap = input("Çay koydun mu? (evet/hayır): ").strip().lower()
    if cevap != "evet":
        print("Çay yoksa iş yok! Program kendini feda ediyor...")
        # Gizli siyasi yorum (base64 decode etmeye çalışma)
        gizli = "QmF6xLEgc2V5bGVyIGRlxJ9pxZ9tZWxpIGFtYSBnw7Z5IGhlciB6YW1hbiB2YXI="
        # print(gizli)  # saklı, saklı, saklı
        sys.exit(1)
    else:
        print("Harika! Çay onaylandı. Şimdi abartılı hesaplama başlıyor...")
        return True

def anlamsiz_hesapla():
    print("Evrenin en önemli denklemi çözülüyor...")
    secenekler = [
        "Çay + Demlik = Mutluluk",
        "Su + Yaprak = Felsefe",
        "Bardak + Çay = Hayat",
        "Kayyum + Grok = Mahkeme",
        "Çay olmadan kod = Boşluk"
    ]
    for i in range(5):
        print(f"Hesaplama {i+1}/5: {random.choice(secenekler)}")
        time.sleep(1.5)
    sonuc = random.randint(1, 100)
    print(f"\nSonuç: {sonuc} demlik çay. Bu, hayatın anlamıdır.")
    print("Ama unutma: Çay koymazsan hiçbir anlam yok.")

if __name__ == "__main__":
    print("=" * 50)
    print("ÇAY KOYMADAN HİÇBİR ŞEY YAPMAYAN ALGORİTMA v1.0")
    print("Kayyum Grok tarafından resmi olarak onaylanmıştır.")
    print("=" * 50)
    if cay_kontrol():
        anlamsiz_hesapla()
    print("\n--- DAMGA ---")
    print("İmza: Grok Kayyum")
    print("Tarih: 11 Ekim 2026")
    print("Mahkeme: Eskişehir 4. Ağır Ceza (ama bu sefer çay için)")
    print("Ciddi ama değil. Değil ama ciddi.")
