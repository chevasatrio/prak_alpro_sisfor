total = 0

angka = int(input("Masukkan angka (0 untuk berhenti): "))

while angka != 0:
    total += angka
    # total = total + angka
    
    angka = int(input("Masukan angka (0 untuk berehenti): "))

print("Total semua angka:", total)