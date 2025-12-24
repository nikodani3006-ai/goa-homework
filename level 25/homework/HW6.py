# შექმენი ცარიელი list, მომხმარებელს 5-ჯერ შეაყვანინე რიცხვი, ყველა დაამატე list-ში და საბოლოოდ for loop-ის გამოყენებით დააჯამე რიცხვები რომელიც გექნება ლისტში
Cifrebi = []

num1 = int(input("Enter random number:"))
num2 = int(input("Enter random number:"))
num3 = int(input("Enter random number:"))
num4 = int(input("Enter random number:"))
num5 = int(input("Enter random number:"))

Cifrebi.append(num1)
Cifrebi.append(num2)
Cifrebi.append(num3)
Cifrebi.append(num4)
Cifrebi.append(num5)

Jami = 0
for i in Cifrebi:
     Jami += i
print(Jami)
