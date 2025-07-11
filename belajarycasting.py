# merubah dari satu tipe ketipe lain adalah casting
# disini kita belajar casting 
# ada yang namanya operator casting
# tipe data =  int, float , str ,bool

print("========dari 'INTEGER' ke sisanya =========================")
print("")
data_int= -1;
print("data = ",data_int, "type = " , type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ",data_float, "type = " , type(data_float))
print("data = ",data_str, "type = " , type(data_str))
print("data = ",data_bool, "type = " , type(data_bool))# di luar dari 0 nilai nya akan 'True' dan jika nilai nya sama dengan '0' maka nilainya akan 'False'
print(" ")

print("=========dari 'FLOAT' ke sisanya =========================")
print("")
data_float= 0;
print("data = ",data_float, "type = " , type(data_float))

data_int = int(data_float) # akan di bulat kan ke bawah 
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ",data_int, "type = " , type(data_int))
print("data = ",data_str, "type = " , type(data_str))
print("data = ",data_bool, "type = " , type(data_bool)) # aka 'False' ketika nilainya menjadi 0 
print(" ")


print("=========dari 'BOOLEAN' ke sisanya =========================")
print("")
data_bool= False;
print("data = ",data_bool, "type = " , type(data_bool))

data_int = int(data_bool) # akan di bulat kan ke bawah 
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ",data_int, "type = " , type(data_int))
print("data = ",data_str, "type = " , type(data_str))
print("data = ",data_float, "type = " , type(data_float)) # aka 'False' ketika nilainya menjadi 0 
print(" ")

print("=========dari 'STRING' ke sisanya =========================")
print("")
data_str = "10  ";
print("data = ",data_str, "type = " , type(data_str))

data_int = int(data_str) # akan di bulat kan ke bawah 
data_bool = bool(data_str)
data_float = float(data_str)
print("data = ",data_int, "type = " , type(data_int))
print("data = ",data_bool, "type = " , type(data_bool))
print("data = ",data_float, "type = " , type(data_float)) # aka 'False' ketika nilainya menjadi 0 
