print('NAMA : SRI ADININGSI')
print('NIM : E1E120020')
print('-------PROGRAM HITUNG BILANAGAN POSITIF PADA LIST-------')


def hitung(daftar):
    jumlah = 0
    banyak = 0
    for elemen in daftar:
        if elemen > 0:
            jumlah += elemen
            banyak += 1
    return jumlah, banyak


daftar = []
n = int(input("Masukkan jumlah elemen dalam list: "))
for i in range(n):
    elemen = int(input("Masukkan elemen ke-{}: ".format(i + 1)))
    daftar.append(elemen)
print("Elemen-elemen list yang dimasukkan:", daftar)

jumlah_positif, banyak_positif = hitung(daftar)
print("Banyaknya bilangan positif dalam list:", banyak_positif)
print("Jumlah bilangan positif dalam list:", jumlah_positif)
