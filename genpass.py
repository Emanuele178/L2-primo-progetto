import random

caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lunghezza = int(input("inserisci la lunghezza della password: "))

password = ""

for i in range(lunghezza):
    password += random.choice(caratteri)

print(password)

input("Premi INVIO Per Uscire ...")
