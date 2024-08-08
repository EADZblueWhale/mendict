meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "FAKE": "Gerçek olmayan / Sahte",
            "TROLL": "İronil bir şey",
            "BRUH": "Bir şey olacakken olmaması"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Anlayamadım, tekrar denermisiniz.")



