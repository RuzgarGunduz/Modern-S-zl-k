meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
           "OK" : "Tamam" ,
            "CREEPY" : "korkunç" ,
            "OK BOMMER" : "TAMAM ŞAMPİYON" ,
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
   print("Bu kelimeyi biliyorsunuz!")
