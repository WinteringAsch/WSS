coffee = 10
while True:
    money = int(input("insert money : "))
    if money == 300:
        print("Here's your coffee.")
        coffee = coffee -1
    elif money > 300:
        print("Here's your coffee and change %d." % (money -300))
        coffee = coffee -1
    else :
        print("Here's your money back.")
        print("%d coffee left." %coffee)
    if not coffee:
        print("No coffee left. Stop sale.")
        break
