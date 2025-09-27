import random

#değişkenler
characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
number=int(input("Parolanın uzunluğu kaç olsun?"))
password=""

for i in range(number):

    characters = random.choice(character)
    password += character

print("PAROLA:",password)
