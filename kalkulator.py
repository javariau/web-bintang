angka1 = float(input("masukan angka pertama :"))
operator = input("masukan operator (+,-,/,*) :")
angka2 = float(input("masukan angka kedua :"))
if operator == "+" :
    hasil = angka1 + angka2
elif operator == "-" :
    hasil = angka1 - angka2
elif operator == "/" :
    hasil = angka1 / angka2
elif operator == "*" :
    if angka2 !=0 :
        hasil= angka1 / angka2
    else :
        hasil = "angka eror "
else :
        hasil = "tidak bisa di bagi 0"

print ("hasil = ", hasil)