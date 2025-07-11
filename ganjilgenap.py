# KITA AKAN MELAKUKAN SISTEM SANDI JIKA SANDINYA SALAH MAKA DIA AKAN MEMBERI PERINGATAN SANDI SALAH DAN USER TIDAK DAPAT MEMASUKAN ANGKA KITA AKAN BELAJAR NANTI 
# KARENA KUOTA HABIS ANJIR GAK BISA PAKE INTERNET DAN GAK TAU INI CARANYA GIMANA YA ITU KITA MEGGUGANAK 'WHILE'

# disini kita akan melakukan codingan ganjil genap dengan input dari user dan nama user
nama = input("Masukan Nama :")
while True:
    sandi  = input("masukan Sandi anda : ")
    if sandi == "bintang123#":
        print("paswor benar")
        break
    else:
        print("masukan pasword anda lagi")

print(f"Halo {nama} Silahkan memasukan angka ")

angka  = int(input("Masukan Angka :"))
if angka % 2 == 0 :
    print("Angka Tersebut Adalah Bilangan 'GENAP'")

else :
    print("Angka Tersebut Adalah Bilangan 'GANJIL'")
    