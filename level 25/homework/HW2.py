#  შექმენი list: fruits = ["apple", "banana", "apple", "orange"] მომხმარებელს შეაყვანინე ხილი, თუ list-ში უკვე არის ეს ხილი
# remove()-ით წაშალე მხოლოდ პირველი შემხვედრი, თუ არ არის ლისტში მაშინ დაბეჭდე შესაბამისი შეტყობინება

fruits = ["apple", "banana", "apple", "orange"] 

fruit = input("Enter fruit you like:")
if fruit in fruits:
     fruits.remove(fruit)
     print(fruits)
else:
     print("this fruit is not in list")