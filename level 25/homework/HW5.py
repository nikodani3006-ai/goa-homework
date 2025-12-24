# შექმენი ნებისმიერი list 5 ელემენტით, მომხმარებელს ჰკითხე: გინდა list-ის გასუფთავება? (yes/no), თუ პასუხი "yes"  გამოიყენე clear(), ბოლოს დაბეჭდე list
list = ["nika",72,"idk",True,2301]
question = input("Do you want to clear list? (yes/no):")
if question == "yes":
     print(list.clear())
else:
      print(list)