# მომხმარებელს შეაყვანინე რიცხვები, მანამ სანამ არ შეიყვანს 0, ყოველი რიცხვის შემდეგ დაბეჭდე "დადებითია" ან "უარყოფითია".დაბეჭდე ბოლოს რიცხვების ჯამი. გამოიყენე while loop.
result = 0

while True:
     number = int(input("Enter random number:"))
     if number > 0:
         print("დადებითია")
     if number < 0 :
         print("უარყოფითია")
     if number == 0:
         break
     result += number
     print(result)

     