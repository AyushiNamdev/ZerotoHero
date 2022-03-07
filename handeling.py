def ask():
    waiting = True
    while waiting: #or while True
        try:
            n = int(input("enter a number"))
        except:
            print("please try again! \n")
            continue
        else:
            waiting = False
            #break

    print("Your number squared is:")
    print(n**2)

print(ask())