# # mengambil input dari user
# # data yang di masukan pasti string

# # disini kita bisa menggunakan operator casting

while True:
    user = input("masukan username")
    if user == 'bintang':
        print("username benar")

    else:
        print("user name salah")


print("data = ", data, " type=", type(data))


 # jika ingin mengambil int, maka 
angka = float(input("masukan angka :" ))
angka = int(input("masukan angka :" ))

print("data = ", angka, " type=", type(angka))
print("data = ", angka, " type=", type(angka))

data_bool = bool(int(input("masukan data boolean : "))) # kalau boolean dia agak susah kita harus memindahkan dulu ke integer baru keboolean ini salah satu cata paling gampang

print("data = ", data_bool, " type=", type(data_bool))