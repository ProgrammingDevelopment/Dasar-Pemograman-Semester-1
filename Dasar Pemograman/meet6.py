print("  WARUNG AYAM GEPREK 1945  ")
print("===========================")
print("Kode Jenis Potong Harga")
print("===========================")
print("D    Dada    2500")
print("P    Paha    2000")
print("S    Sayap   1500")

banyak_jenis = int(input("Banyak Jenis : "))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []

i = 0
while i<banyak_jenis:
    print("Jenis ke - ", i+1)
    kode_potong.append(input("Kode Potong [D/P/S] : "))
    banyak_potong.append(int(input("Banyak potong : ")))

    if kode_potong[i] == "D" or kode_potong[i] == "d" :
        jenis_potong.append("Dada")
        harga.append("2500")
        jumlah.append(banyak_potong[i]*int("2500"))
    elif kode_potong[i] == "P" or kode_potong[i] == "p" :
        jenis_potong.append("paha")
        harga.append("2000")
        jumlah.append(banyak_potong[i]*int("2000"))
    elif kode_potong[i] == "S" or kode_potong[i] == "s" :
        jenis_potong.append("1500")
        jumlah.append(banyak_potong[i]*int("1500"))
    else :
        jenis_potong.append("kode salah")
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))
    i= i + 1