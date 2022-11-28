from time import sleep
while True:
  
  Boot = str(input("\033[0mWhich program do you want to boot? (Q1, Q2, Q3, Quit)\n"))
  
  if Boot == str("Q1"):
    print("\033[94mWelcome to Q1Length! This program will ask you for a word, and it will tell you the length of the word.\n\n")
    sleep(1.5)
    while True:
      Inp = str(input("\033[94mPlease enter a word to check the length of it.\n"))
      print("\n\033[95mYour word", Inp, "is", len(Inp), "characters long!\n")

      LoopYN = str(input("\033[93mDo you want to run this program again?\n"))
      if LoopYN == str("N"):
        del Inp
        del LoopYN
        del Boot
        print("\n\n")
        break
    continue

  elif Boot == str("Q2"):
    print("\033[94mWelcome to Q2Reverse! This program will ask you for a set of characters, and it will reverse them.\n\n")
    sleep(1.5)
    while True:
      Inp = str(input("Please enter your character set.\n")[::-1])
      print("\033[95mYour character set backwards is", Inp, "!\n")
      LoopYN = str(input("\033[93mDo you want to run this program again?\n"))
      if LoopYN == str("N"):
        del Boot
        del Inp
        del LoopYN
        print("\n\n")
        break
    continue

  elif Boot == str("Q3"):
    print("\033[94mWelcome to Q3WordTriangle! This program will ask you for a set of characters, and make a triangle out of it!\n\n")
    sleep(1.5)
    while True:
      Inp = str(input("Please enter your character set.\n"))
      print("\033[95m")
      for x in range (len(Inp)):
        for y in range(x+1):
          print(Inp[y],end=' ')
        print()
      LoopYN = str(input("\n\033[93mDo you want to run this program again?\n"))
      if LoopYN == str("N"):
        del Boot
        del Inp
        del LoopYN
        print("\n\n")
        break
    continue

  elif Boot == str("Quit"):
    quit("Okay.")