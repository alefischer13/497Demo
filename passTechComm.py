def howToPassThisClass():
    print("You will pass!")

def howToFailThisClass():
    print("You will not pass!")

def main():
    isWorkingHard = True
    if isWorkingHard:
        howToPassThisClass()
    else:
        howToFailThisClass()

if __name__ == "__main__":
    main()
