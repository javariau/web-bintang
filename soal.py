# kita di sini akan memasukan inputan nama user dan ketika user memasukan nama akan ada  tulisan halo nama user dan di suruh memasukan jenis kendaraan
while True:
    nama = input("masukan nama : ")
    if nama == "admin 123" :
        print("selamat nama anda benar")
        break
    else:
        print("maaf nama anda salah") # disini kita berhasil mempelajari while ya dan harus ada kondisi 'break'karena jika tidak ada kondisi break 
# walaupun inputan benar dia akan terus berulang karena tidak ada perintah untuk berhenti kerika inputan benar

kendaraan  = input("Masukan jenis kendaraan : ").lower() # ini supaya huruf besar dan kecil nya terbaca
darurat = "ambulance,pemadam kebakaran /damkar, truck tentara" # disini bisa menggunakan '[]' ini untuk tipe lsit yang di gunakan sekarang tipe str
print(f"jenis kenadaraan : {kendaraan}")
print("=========================================================")

if kendaraan == "mobil" :
    print("jenis kendaraan anda memiliki tarif Rp.12.000 ")

elif kendaraan == "motor":
    print("jenis kendaraan anda memuliki tarif Rp.5000")

elif kendaraan == "truck":
    print("jenis kendaraan anda memiliki tarif Rp.15.000")

elif kendaraan  in darurat:  # ini menggukanak 'in' bukan '==' atau yang perbandingan laiinya karena kia memasukan objeck dalam variable darurat
    print("GRATIS")

else :
    print("jenis kendaraan tidak termasuk")
