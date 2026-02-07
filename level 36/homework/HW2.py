# შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და დაითვლის ამ ტექსტში ხმოვნების რაოდენობას

def kmovnebii(text):
    kmovnebi = "aeiou"
    total = 0
    for i in text:
        if i in kmovnebi:
            total += 1
    return total

result = kmovnebii("rogoraxar")
print(result, "jami")