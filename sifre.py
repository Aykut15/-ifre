import random

semboller="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = input("şifrenin uzunluğunu giriniz")
uzunluk = int(uzunluk)
sifre =""
for i in range(uzunluk):
     sifre += random.choice(semboller)
print(sifre)
