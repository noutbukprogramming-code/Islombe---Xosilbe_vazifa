ombor = {}

while True:
    print("\n===== MAHSULOTLAR OMBORI =====")
    print("1. Yangi mahsulot qo'shish")
    print("2. Mahsulot narxi yoki miqdorini o'zgartirish")
    print("3. Mahsulot qidirish")
    print("4. Umumiy qiymatni hisoblash")
    print("5. Miqdori 5 tadan kam mahsulotlar")
    print("6. Barcha mahsulotlarni ko'rish")
    print("0. Chiqish")

    tanlov = input("Tanlang: \n\n")

    if tanlov == "1":
        nom = input("Mahsulot nomi: ")

        if nom in ombor:
            print("Bu mahsulot omborda mavjud!")
        else:
            narx = float(input("Mahsulot narxi: "))
            miqdor = int(input("Mahsulot miqdori: "))

            ombor[nom] = {
                "narx": narx,
                "miqdor": miqdor
            }

            print("Mahsulot qo'shildi!")

    elif tanlov == "2":
        nom = input("Mahsulot nomi: ")

        if nom not in ombor:
            print("Bunday mahsulot omborda mavjud emas!")
        else:
            print("1. Narxni o'zgartirish")
            print("2. Miqdorni o'zgartirish")

            tanlov2 = input("Tanlang: ")

            if tanlov2 == "1":
                yangi_narx = float(input("Yangi narx: "))
                ombor[nom]["narx"] = yangi_narx
                print("Narx yangilandi!")

            elif tanlov2 == "2":
                yangi_miqdor = int(input("Yangi miqdor: "))
                ombor[nom]["miqdor"] = yangi_miqdor
                print("Miqdor yangilandi!")

            else:
                print("Noto'g'ri tanlov!")

    elif tanlov == "3":
        nom = input("Qidirilayotgan mahsulot nomi: ")

        if nom in ombor:
            print("Mahsulot:", nom)
            print("Narxi:", ombor[nom]["narx"])
            print("Miqdori:", ombor[nom]["miqdor"])
        else:
            print("Mahsulot topilmadi!")

    elif tanlov == "4":
        umumiy = 0

        for nom in ombor:
            umumiy += ombor[nom]["narx"] * ombor[nom]["miqdor"]

        print("Ombordagi mahsulotlarning umumiy qiymati:", umumiy)

    elif tanlov == "5":
        for nom in ombor:
            if ombor[nom]["miqdor"] < 5:
                print(
                    nom,
                    "| Narxi:", ombor[nom]["narx"],
                    "| Miqdori:", ombor[nom]["miqdor"]
                )

    elif tanlov == "6":
        if len(ombor) == 0:
            print("Ombor bo'sh!")
        else:
            for nom in ombor:
                print(
                    nom,
                    "| Narxi:", ombor[nom]["narx"],
                    "| Miqdori:", ombor[nom]["miqdor"]
                )

    elif tanlov == "0":
        print("Dastur tugadi!")
        break

    else:
        print("Noto'g'ri tanlov!")
