# შექმენი list: colors = ["red", "blue", "green", "yellow"] მომხმარებელს შეაყვანინე ფერი, თუ არსებობს  დაბეჭდე მისი index(), თუ არა  დაბეჭდე "Not found"

colors = ["red", "blue", "green", "yellow"] 
user_colour = input("Enter colour you like:")
if user_colour in colors:
     print(colors.index(user_colour))
else:
     print("Not found")