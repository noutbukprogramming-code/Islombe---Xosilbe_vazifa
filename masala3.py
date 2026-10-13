
import random

chegara = [1, 100]
urinish = 0
urinish2 = 0

while True:
    taxmin = random.randint(*chegara)
    urinish += 1
    print(f"Siz o'ylagan son {taxmin} ga tengmi? ({chegara})")
    natija = input("(>, <, =): ")

    if natija == "=":
        print(f"🥳🥳 Men bu sonni {urinish} urinishda topdim.")
        urinish2 = urinish
        break
    elif natija == "<":
        print("☹️ Qaytadan urinib ko'raman.")
        chegara[1] = taxmin - 1
    elif natija == ">":
        print("☹️ Qaytadan urinib ko'raman.")
        chegara[0] = taxmin + 1
    else:
        print("Noto'g'ri belgi kiritildi!")
        urinish -= 1
        continue

    if chegara[0] > chegara[1]:
        print("😠 Yolg'on javoblar berildi!")
        break

if urinish2 > 0:
    if urinish2 <= 5:
        print("A'lo!!!")
    elif urinish2 >= 6 and urinish2 <= 10:
        print("Yaxshi")
    elif urinish2 > 10:
        print("Ko'proq mashq qilish kerak")
