print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bild = 15
    if add_pepperoni == "Y":
        bild += 2
    if extra_cheese == "Y":
        bild += 1
    print(f"Your final bill is: ${bild}.")

if size == "M":
    bild = 20
    if add_pepperoni == "Y":
        bild += 3
    if extra_cheese == "Y":
        bild += 1
    print(f"Your final bill is: ${bild}.")

if size == "L":
    bild = 25
    if add_pepperoni == "Y":
        bild += 3
    if extra_cheese == "Y":
        bild += 1
    print(f"Your final bill is: ${bild}.")