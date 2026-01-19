# შექმენი სია სადაც შეიყვანთ როგორდც დადებით ასევე უარყოფით რიცხვებს,შენი დავალებაა გაიგო სიაშ მყოფი დადებით რიცხვების ჯამი და უარყოფით რიცხვების რაოდენობა
numbers = [56,34,-43.-5,3,-99,532]

total = 0
result = 0

for num in numbers:
     if num >= 0:
         result+=num
     elif num <= 0:
      total = total + 1
     print(result,total)