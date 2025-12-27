#  შექმენი ცარიელი სია.მომხმარებელმა შეიყვანოს რიცხვები მანამ, სანამ არ დაწერს "stop".დაამატე მხოლოდ დადებითი რიცხვები სიაში, უარყოფითი რიცხვები არ დაამატო, ბოლოს დაბეჭდე სია
list = []

while True:
     idk = input("Enter random numbers:")
     if idk == "stop":
        break
     gg = int(idk)
     if gg > 0 :
          list.append(gg)
print(list)
     