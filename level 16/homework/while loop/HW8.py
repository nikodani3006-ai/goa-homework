# შექმენი ცვლადი და შეინახე შენი პაროლი(string)

# მომხმარებელს შემოატანინე პაროლი

# სანამ შენი პაროლი არ უდრის მომხმარებლის მიერ შემოტანილ პაროლს
    # მომხმარებელს თავიდან შემოატანინე პაროლი რომ გაარტყას შენ პაროლს
# დაპრინტე "სწორია გაარტყი"

i = 0 

PSW = input("Enter correct password:")
 

while PSW != str("nikaa683") and i < 2:
     print("incorrect")
     PSW = input("Enter correct password:")
     if PSW == str("nikaa683"):
          print("correct")
     i = i + 1