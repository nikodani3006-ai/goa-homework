# შექმენი ფუქნცია რომელიც მომხმარებელს შემოაყვანინებს რაღაც რიცხვს და დააბრუნებს სიტყვას ეს რიცხვი დადებითია უარყოფითია თუ ნულია
num = int(input("Enter random number:"))

def greet(num):
     if num > 0:
         return "დადებითია"
     elif num < 0: 
         return "უარყოფითია"
     else:
         return "ნულის ტოლია"
print(greet(num))