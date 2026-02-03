# შექმენით ფუნქცია. შექმენით რიცხვებით სავსე სია, დაბეჭდეთ სიის უდიდესი ელემენტი. არ გამოიყენოთ max() ფუნქცია, გამოიყენეთ for ციკლი. გამოიძახეთ ფუნქცია.

numbers = [34,54,23,12,43,4,5,5,7342,344,546,65,6,]

def largest_number():
     largest = numbers [0]
     for num in numbers:       
         if num > largest:          
              largest = num
         print(largest)
largest_number()