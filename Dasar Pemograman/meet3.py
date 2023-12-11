class GeometryCalculator:
    def __init__(self):
        self.data = []

    def create_data(self, name, formula, calculation):
        data_entry = {'name': name, 'formula': formula, 'calculation': calculation}
        self.data.append(data_entry)

    def read_data(self):
        for idx, entry in enumerate(self.data, start=1):
            print(f"{idx}. Nama: {entry['name']}, Formula: {entry['formula']}, Kalkulasi: {entry['calculation']}")

    def update_data(self, index, name, formula, calculation):
        if 1 <= index <= len(self.data):
            self.data[index - 1] = {'name': name, 'formula': formula, 'calculation': calculation}
            print("Data berhasil diperbarui.")
        else:
            print("Index tidak valid.")

    def delete_data(self, index):
        if 1 <= index <= len(self.data):
            deleted_entry = self.data.pop(index - 1)
            print(f"Data {deleted_entry['name']} berhasil dihapus.")
        else:
            print("Index tidak valid.")

    def calculate_triangle_area(self, side_length):
        return (side_length ** 2 * (3 ** 0.5)) / 4

    def calculate_cube_volume(self, side_length):
        return side_length ** 3


def main():
    calculator = GeometryCalculator()

    # Menambahkan data
    calculator.create_data("Segitiga Sama Sisi", "sisi^2 * sqrt(3) / 4", "calculate_triangle_area(5)")
    calculator.create_data("Kubus", "sisi^3", "calculate_cube_volume(4)")

    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Perbarui Data")
        print("4. Hapus Data")
        print("5. Keluar")

        choice = input("Pilih menu (1-5): ")

        if choice == '1':
            name = input("Masukkan nama bangun datar/bangun ruang: ")
            formula = input("Masukkan formula: ")
            calculation = input("Masukkan kalkulasi: ")
            calculator.create_data(name, formula, calculation)

        elif choice == '2':
            calculator.read_data()

        elif choice == '3':
            index = int(input("Masukkan indeks data yang ingin diperbarui: "))
            name = input("Masukkan nama bangun datar/bangun ruang: ")
            formula = input("Masukkan formula: ")
            calculation = input("Masukkan kalkulasi: ")
            calculator.update_data(index, name, formula, calculation)

        elif choice == '4':
            index = int(input("Masukkan indeks data yang ingin dihapus: "))
            calculator.delete_data(index)

        elif choice == '5':
            print("Terima kasih! Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-5.")


if __name__ == "__main__":
    main()
