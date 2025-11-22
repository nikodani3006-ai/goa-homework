# შექმენით კალკულატორი როგორიც ჩვენ გავაკეთეთ,დაუმატეთ სხვა მათემატიკური ოპერატორები,ასევე დაუმატეთ შედარების ოპერატორებიც 


num1 = int(input("Enter any number:"))
num2 = int(input("Enter any number:"))
operator = input("<,+,-,**,%,/,*,,>")

if operator == "<":
     print(num1 < num2)
elif operator == "+":
     print(num1 + num2)
elif operator == "/":
     print(num1 / num2)
elif operator == "-":
     print(num1 - num2)
elif operator == ">":
     print(num1 > num2)
elif operator == "*":
     print(num1 * num2)
elif operator == "**":
     print(num1 ** num2)
elif operator == "%" :
     print(num1 % num2)


