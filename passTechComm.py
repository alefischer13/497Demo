def howToPassThisClass():
    print("You will pass!")

def howToFailThisClass():
    print("You will not pass!")

def main():
    isWorkingHard = True
    isWorkingHard = False
    if isWorkingHard:
        howToPassThisClass()

if __name__ == "__main__":
    main()
