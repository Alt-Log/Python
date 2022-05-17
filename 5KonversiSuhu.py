print("---KONVERSI FAHRENHEIT KE KELVIN---")
fr=float(input("Masukkan Suhu Fahrenheit : "))
kv=5/9*(fr-32)+273

print("Fahrenheit= ",fr)
print("Kelvin= ",kv)

print("")
print("---KONVERSI KELVIN KE FAHRENHEIT---")
kv=float(input("Masukkan Suhu Kelvin : "))
fr=(kv-273)*9/5+32

print("Kelvin= ",kv)
print("Fahrenheit= ",fr)