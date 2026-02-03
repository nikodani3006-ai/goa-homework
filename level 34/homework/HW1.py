# შექმენით ფუნქცია. მომხმარებელს შემოატანინეთ ერთი მთელი რიცხვი n. დაბეჭდეთ თუ რამდენი ლუწი რიცხვია 1-დან n-მდე. გამოიძახეთ ფუნქცია.


n = int(input("Enter random number:"))

def count_evens():
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    print(count)
count_evens()