def calculate_grade(score):
    if score >= 70:
        return "Lulus"
    else:
        return "Tidak Lulus"

def print_header(biodata):
    print("===================================")
    print("        Universitas Mercubuana")
    print("      Jalan Kramat Raya No. 98")
    print("===================================")
    print(f"Nama Mahasiswa: {biodata['name']}")
    print(f"Kelas: {biodata['class_grade']}")
    print(f"ID Mahasiswa: {biodata['student_id']}")
    print("===================================")

def print_footer():
    print("===================================")

if __name__ == "__main__":
    # Input biodata mahasiswa
    biodata = {}
    biodata['name'] = input("Masukkan nama mahasiswa: ")
    biodata['class_grade'] = input("Masukkan kelas mahasiswa: ")
    biodata['student_id'] = input("Masukkan ID mahasiswa: ")

    print_header(biodata)

    # Input hasil ujian mahasiswa 
    try:
        exam_score = float(input("Masukkan nilai exam mahasiswa: "))
    except ValueError:
        print("Masukkan nilai dalam bentuk angka.")
        exit()

    # validasi nilai dan menghitung hasil nilai 
    if 0 <= exam_score <= 100:
        result = calculate_grade(exam_score)
        print(f"Hasil: {result}")
    else:
        print("Nilai tidak valid. Harap masukkan nilai antara 0 dan 100.")

    print_footer()
