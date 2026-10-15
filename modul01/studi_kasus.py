nama = input("Masukkan nama anda: ")
input_nilai = int(input("Masukkan nilai anda: "))
                  
if input_nilai >= 60:
     print (nama, "anda dinyatakan lulus")
     status = "Lulus"
else :
    print (nama, "anda dinyatakan tidak lulus")
    status = "Tidak Lulus"
    
if input_nilai >= 90:
    grade = "A"
elif input_nilai >= 80:
    grade = "B"
elif input_nilai >= 70:
    grade = "C"
else:
    grade = "D"
    
print (nama, "dengan nilai", input_nilai, "mendapatkan grade", grade, "dengan status", status)
    
    