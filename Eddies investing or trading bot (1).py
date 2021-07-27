# IF USER IS TOO YOUNG TO PLAY, USER CANNOT PLAY
Name = input("Name: ").upper()
Age = int(input("Age: "))
if Age >= 18 and Age < 100:
    print("you are old enough to play")

# does the user want trading bot or investing bot?
    BOT = str(input("Trading Bot (1) / Investing Bot (2): "))
# OPTIONS for trading bot
    if BOT == "1":
        print("welcome, you chose trading bot")

        TOTB = input("WHICH TRADING BOT DO YOU WANT? SAFE/MODERATE/RISKY ")
        if TOTB.lower() == str("SAFE"):
            print("You chose the SAFE ")
        HMMTI1 = input("how much money do you want to invest? ")
        AYS1 = input("you have chosen to invest $" + HMMTI1 + ", in SAFE, is this correct? ")
        if AYS1 == "yes":
            print("OKAY! $" + HMMTI1 + " will be invested into " + TOTB)


        elif TOTB.lower() == str("moderate"):
            print("You chose the MODERATE ")
            AYS1 = input("you have chosen to invest $" + HMMTI1 + " in MODERATE, is this correct? ")
            if AYS1 == "yes":
                print("OKAY! $" + HMMTI1 + " will be invested into " + TOTB)
                quit()

        elif TOTB.lower() == str("risky"):
            print("you chose the RISKY trading bot")
            HMMTI1 = input("how much do you want to invest? ")
            AYS1 = input("you have chosen to invest $" + HMMTI1 + " in RISKT is this correct? ")
            if AYS1 == "yes":
                print("OKAY! $" + HMMTI1 + " will be invested into " + TOTB)
                quit()

#OPTIONS for investing bot
    elif BOT == "2":
        print("welcome, you chose INVESTING BOT")
        TOIB = input("WHICH INVESTING BOT DO YOU WANT? SAFE/MODERATE/RISKY: ")
        if TOIB.lower() == str("safe"):
            print("you chose the SAFE INVESTING BOT")
            HMMTI = input("how much do you want to invest? ")
            AYS = input("you have chosen to invest $" + HMMTI + " in SAFE, is this correct? ")
            if AYS == "yes":
                print("OKAY! $" + HMMTI + " will be invested into " + TOIB)
                quit()

        elif TOIB.lower() == str("moderate"):
            print("You chose the MODERATE INVESTING BOT")
            HMMTI = input("how much do you want to invest? ")
            AYS = input("you have chosen to invest $" + HMMTI + " in MODERATE, is this correct? ")
            if AYS == "yes":
                print("OKAY! $" + HMMTI + " will be invested into " + TOIB)
                quit()

        elif TOIB.lower() == str("risky"):
            print("you chose the RISKY INVESTING BOT")
            HMMTI = input("how much do you want to invest? ")
            AYS = input("you have chosen to invest $" + HMMTI + " in RISKY, is this correct? ")
            if AYS == "yes":
                print("OKAY! $" + HMMTI + " will be invested into " + TOIB.upper() + " INVESTING BOT")
                quit()
    else:
        print("Sorry, there are only 2 options")
        quit()
#this end the code when user is underaged, making the res tof the code useless lol
elif Age >= 100:
    print("sorry " + Name + ", you are too old to play")
    quit()
elif Age <= 18:
    print("Sorry " + Name + ", you are too young to play")
    quit()

