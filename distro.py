class Produk:
    def __init__(self, kode_produk, jenis_produk, merek, ukuran, warna, jumlah_stok, harga_produk):
        self.kode_produk = kode_produk
        self.jenis_produk = jenis_produk
        self.merek = merek
        self.ukuran = ukuran
        self.warna = warna
        self.jumlah_stok = jumlah_stok
        self.harga_produk = harga_produk


class Transaksi:
    def __init__(self):
        self.jumlah_item = 0
        self.produk = []
        self.total = 0
        self.total_ppn = 0


# Global variables
produk_list = []
transaksi_list = []
index_transaksi = 0


def header():
    print("\n\t\t\t      =====================")
    print("\n\t\t\t\tDISTRO KECE BADAI")
    print("\n\t\t\t      =====================\n")


def footer():
    print("\n\n\t\t\t\t============================================")
    print("\t\t\t\tTERIMA KASIH SUDAH BERBELANJA DI DISTRO KAMI")
    print("\t\t\t\t============================================\n")


def menu():
    print("\n\t\t1. Tambah Produk")
    print("\n\t\t2. Lihat Semua Produk")
    print("\n\t\t3. Ubah Produk")
    print("\n\t\t4. Hapus Produk")
    print("\n\t\t5. Tambah Transaksi")
    print("\n\t\t6. Lihat Semua Transaksi")
    print("\n\t\t7. Tampilkan Invoice")
    print("\n\t\t8. Keluar")


def tambah_produk():
    kode_produk = input("\n\t\tMasukkan Kode Produk: ")
    jenis_produk = input("\n\t\tMasukkan Jenis Produk: ")
    merek = input("\n\t\tMasukkan Merek: ")
    ukuran = input("\n\t\tMasukkan Ukuran: ")
    warna = input("\n\t\tMasukkan Warna: ")
    jumlah_stok = int(input("\n\t\tMasukkan Jumlah Stok: "))
    harga_produk = int(input("\n\t\tMasukkan Harga Produk: "))

    produk = Produk(kode_produk, jenis_produk, merek, ukuran, warna, jumlah_stok, harga_produk)
    produk_list.append(produk)
    print("\n\t\tData produk berhasil ditambahkan!")


def lihat_semua_produk():
    if not produk_list:
        print("\n\t\tBelum ada data produk yang tersimpan.")
    else:
        print("\n\t\t   Kode Produk   Jenis Produk       Merek       Ukuran       Warna       Stok       Harga")
        print("\t\t-------------------------------------------------------------------------------------------")
        for produk in produk_list:
            print(f"\t\t   {produk.kode_produk:<14}{produk.jenis_produk:<16}{produk.merek:<12}"
                  f"{produk.ukuran:<12}{produk.warna:<12}{produk.jumlah_stok:<10}{produk.harga_produk}")


def ubah_produk():
    kode_produk = input("\n\t\tMasukkan Kode Produk yang akan diubah: ")

    for i, produk in enumerate(produk_list):
        if produk.kode_produk == kode_produk:
            print("\n\t\tData Produk yang Ingin diubah:")
            print("\n\t\t1. Jenis Produk\n\t\t2. Merek\n\t\t3. Ukuran\n\t\t4. Warna\n\t\t5. Jumlah Stok\n\t\t6. Harga")
            pilih_ubah = int(input("\n\t\tPilihan Anda: "))

            if pilih_ubah == 1:
                produk.jenis_produk = input("\n\t\tMasukkan Jenis Produk baru: ")
            elif pilih_ubah == 2:
                produk.merek = input("\n\t\tMasukkan Merek baru: ")
            elif pilih_ubah == 3:
                produk.ukuran = input("\n\t\tMasukkan Ukuran baru: ")
            elif pilih_ubah == 4:
                produk.warna = input("\n\t\tMasukkan Warna baru: ")
            elif pilih_ubah == 5:
                produk.jumlah_stok = int(input("\n\t\tMasukkan Jumlah Stok baru: "))
            elif pilih_ubah == 6:
                produk.harga_produk = int(input("\n\t\tMasukkan Harga Produk baru: "))
            else:
                print("\n\t\tPilihan tidak valid!")

            print("\n\t\tData produk berhasil diubah!")
            break
    else:
        print(f"\n\t\tData produk dengan kode produk {kode_produk} tidak ditemukan.")


def hapus_produk():
    kode_produk = input("\n\t\tMasukkan Kode Produk yang akan dihapus: ")

    for i, produk in enumerate(produk_list):
        if produk.kode_produk == kode_produk:
            del produk_list[i]
            print("\n\t\tData produk berhasil dihapus!")
            break
    else:
        print(f"\n\t\tData produk dengan kode produk {kode_produk} tidak ditemukan.")


def tambah_transaksi():
    transaksi = Transaksi()

    while True:
        lihat_semua_produk()
        if not produk_list:
            break

        kode_produk = input("\n\t\tMasukkan Kode Produk yang akan dibeli (tekan enter untuk selesai): ")
        if not kode_produk:
            break

        produk = next((p for p in produk_list if p.kode_produk == kode_produk), None)
        if produk:
            jumlah_beli = int(input("\n\t\tMasukkan Jumlah Produk yang akan dibeli: "))
            if jumlah_beli <= 0:
                print("\n\t\tJumlah produk yang dibeli harus lebih besar dari 0.")
                continue

            if jumlah_beli > produk.jumlah_stok:
                print("\n\t\tMaaf, jumlah stok produk tidak mencukupi.")
                continue

            transaksi.produk.append(produk)
            transaksi.jumlah_item += 1

            total_harga = produk.harga_produk * jumlah_beli
            transaksi.total += total_harga

            print(f"\n\t\tProduk {kode_produk} ditambahkan ke transaksi.")

        else:
            print(f"\n\t\tData produk dengan kode produk {kode_produk} tidak ditemukan.")

    transaksi_list.append(transaksi)
    print("\n\t\tTransaksi berhasil ditambahkan!")


def lihat_semua_transaksi():
    if not transaksi_list:
        print("\n\t\tBelum ada transaksi yang dilakukan.")
    else:
        for i, transaksi in enumerate(transaksi_list, start=1):
            print(f"\n\t\tTransaksi ke-{i}")
            print("\t\t---------------------------")
            
            for j, produk in enumerate(transaksi.produk, start=1):
                print(f"\t\t{produk.kode_produk} | {produk.jumlah_beli} pcs | Subtotal: Rp {produk.subtotal}")

            print("\t\t---------------------------")
            print(f"\t\tTotal: Rp {transaksi.total}")
            print(f"\t\tTotal dengan PPN: Rp {transaksi.total_ppn}")

def tampilkan_invoice(transaksi):
    total_bayar = 0

    print("\n\n\t\t\t\t\t\tInvoice Pembayaran")
    print("\t\t\t\t\t      ======================\n")
    print("\n")
    print("Kode Produk   Jenis Produk       Merek       Ukuran       Warna       Harga       Jumlah Beli       Subtotal(inc.diskon)")
    print("-------------------------------------------------------------------------------------------------------------------------------")

    for i, produk in enumerate(transaksi.produk, start=1):
        print(f"{produk.kode_produk} | {produk.jenis_produk} | {produk.merek} | {produk.ukuran} | {produk.warna} | {produk.harga_produk} | {produk.jumlah_beli} | {produk.subtotal}")

    print("------------------------------------------------------------------------------------------------------------------------------")


# Main program loop
while True:
    header()
    menu()

    pilihan = input("\n\t\tPilih menu (1-8): ")

    if pilihan == "1":
        tambah_produk()
    elif pilihan == "2":
        lihat_semua_produk()
    elif pilihan == "3":
        ubah_produk()
    elif pilihan == "4":
        hapus_produk()
    elif pilihan == "5":
        tambah_transaksi()
    elif pilihan == "6":
        lihat_semua_transaksi()
    elif pilihan == "7":
        if transaksi_list:
            index_tampil = int(input("\n\t\tMasukkan indeks transaksi untuk ditampilkan: "))
            if 0 < index_tampil <= len(transaksi_list):
                tampilkan_invoice(transaksi_list[index_tampil - 1])
            else:
                print("\n\t\tIndeks transaksi tidak valid.")
        else:
            print("\n\t\tBelum ada transaksi yang dilakukan.")
    elif pilihan == "8":
        footer()
        break
    else:
        print("\n\t\tPilihan tidak valid!")

    input("\n\t\tTekan ENTER untuk melanjutkan...")
