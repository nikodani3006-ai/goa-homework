#  შექმენი ფუნქცია რომელიც მიიღებს სიტყვების სიას და დააბრუნებს მხოლოდ იმ სიტყვებს რომლებიც იწყება დიდი ასოთი
sia = ["Nika","beqa","saba","Gela"]

def greet(sia):
     for i in sia:
         if i == i.capitalize():
             return(i)
print(greet(sia))