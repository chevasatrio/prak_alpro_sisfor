#Looping masukan penanda dan data kosong

total = 0
banyak = 0

#
durasi = int(input("Waktu proses (menit,-1 selesai) :"))
while durasi != -1 :
    total  = total + durasi
    banyak = banyak + 1
    durasi = int(input("Waktu proses (menit,-1 selesai) :"))
    
if banyak == 0:
    print("Belum ada data yang dimasukkan")
else :
    print("Banyak data", banyak)
    print("Rata -rata", round (total / banyak,2), "menit")
    
#Waktu proses (menit,-1 selesai) :10 (True)
#Waktu proses (menit,-1 selesai) :15 (True)
#Waktu proses (menit,-1 selesai) :-1 (False) karena ditandai -1 itu false di while
#Banyak data 2 (Menghitung bedasarkan True,false tidak terhitung)
#Rata -rata 12.5 menit (Hasil dari pembagian 10 + 15 = 25 : 2 = 12,5 menit)
