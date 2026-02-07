# შექმენი ფუქნცია რომელიც მიიღებს რიცხვების სიას [3, 7, 1, 9] და დააბრუნებს ყველაზე დიდ რიცხვს
sia = [3, 7, 1, 9]

def greet(sia):
    udidesi = sia[0]

    for i in sia:
        if i > udidesi:
            udidesi = i

    return udidesi

print(greet(sia))