n = int(input("kiritmoqchi bolgan soninggiz: "))

sonlar = []

for i in range(n):
    son = int(input(f"{i + 1}-sonni kiriting: "))
    sonlar.append(son)


musbat = 0
manfiy = 0
nol = 0

for son in sonlar:
    if son > 0:
        musbat += 1
    elif son < 0:
        manfiy += 1
    else:
        nol += 1

juft = [son for son in sonlar if son % 2 == 0]
toq = [son for son in sonlar if son % 2 != 0]

takrorlanmas = list(dict.fromkeys(sonlar))


saralangan = sorted(sonlar)


unikal_saralangan = sorted(set(sonlar), reverse=True)

print("\n--- Sonlar statistikasi ---")
print("Kiritilgan sonlar:", sonlar)
print("Musbat sonlar soni:", musbat)
print("Manfiy sonlar soni:", manfiy)
print("Nollar soni:", nol)
print("Juft sonlar:", juft)
print("Toq sonlar:", toq)
print("Takrorlanmaydigan sonlar:", takrorlanmas)
print("O'sish tartibida:", saralangan)

if len(unikal_saralangan) >= 2:
    print("Ikkinchi eng katta son:", unikal_saralangan[1])
else:
    print("Ikkinchi eng katta son mavjud emas.")



    
    