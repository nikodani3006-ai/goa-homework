# შექმენი ფუქნცია რომელიც იღებს რიცხვების სიას და აბრუნებს მათ საშუალოს

sia = [21,34,124,4534,2,314,1432,42]

def greet(sia):
     total = 0
     for i in sia:
        total += i
                 
     return total / len(sia)
print(greet(sia))