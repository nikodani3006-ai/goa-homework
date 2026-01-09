# მომხმარებელს შეაყვანინე პაროლი. თუ პაროლი მეტია ან ტოლია 8 სიმბოლოზე → "პაროლი საკმარისად ძლიერია", თუ ნაკლებია → "პაროლი სუსტია", გამოიყენე while,თუ მომხმარებელი სუსტ პაროლს შემოიყვანს რომ მომხმარებელმა ისევ შეიყვანოს ძლიერი პაროლი.
password = input("create your password:")

if len(password) >= 8:
     print("პაროლი საკმარისად ძლიერია")
else:
     print("პაროლი სუსტია")

while True:
     if len(password) != 8 :
      newpassword = input("Enter new password")
     if len(password) >= 8:
         break
