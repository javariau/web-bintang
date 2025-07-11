# disini kita akan membuat pasword absurd
import random
huruf = "abcdehijklmnopqrstuvwxyz"
huruf_besar="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka ="0123456789"
karakter="@!#$/&*^&"

semua = huruf + huruf_besar + angka + karakter

pasword = ''.join(random.sample(semua,8))
print(f"ini pasword kamu: {pasword}")