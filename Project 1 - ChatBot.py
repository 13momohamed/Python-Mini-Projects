En = "How are you today? "
So = "See tahay? "
pyg = 'ay'

while True:
  Language = input("What is your preferred laguage? ")
  Language = Language.lower()
  if Language == "english":
    Prompt_En = input(En)
    break
  if Language == "somali":
    Prompt_So = input(So)
    break
  else:
    print("Try Again! I only speak English and Somali")

while Language == "english":
  Prompt_En = Prompt_En.lower()
  Day_So = "0"
  if "good" in Prompt_En:
    print("That's good to hear!")
    Day_En = input("Did you do anything fun today? ") 
    break
  if "bad" in Prompt_En:
    print("Oh no, that's terrible!")
    Day_En = input("Are you okay now? ")
    break
  else: 
    print("Wow!")
    Day_En = input("Are you feeling good? ")
    break


while Language == "somali":
  Prompt_So = Prompt_So.lower()
  Day_En = "0"
  if "feecan" in Prompt_So:
    print("Alhamdudlilah!")
    Day_So = input("Hada ma feecantahay? ")
    break
  if "xun" in Prompt_So:
    print("Miskeen!")
    Day_So = input("Maxa dhacey? Hada ma feecantahay? ")
    break
  else:
    print("Haye.") 
    Day_So = input("Maxa dhacey? Hada ma feecantahay? ")
    break



while Day_En.isalpha() == True or Day_So.isalpha() == True:
  Game_En = "0"
  Game_So = "0"
  if Day_En.isalpha() == True:
    Day_En = Day_En.lower()
    if Day_En == "yes":
      print("Cool!")
      Game_En = input("Do you want to play a game? ")
      break  
    if Day_En == "no": 
      print("Oh no!")
      Game_En = input("Do you want to play a game? ")
      break
    else:
      print("Try again, I only understand yes or no! ")   
  if Day_So.isalpha() == True:
    Day_So = Day_So.lower()
    Game_En = "0"
    if Day_So == "haa":
      print("Masha Allah!")
      Game_So = input("Ma ciirayi rabtaa? ")
      break
    if Day_So == "maya":
      print("Subhanallah!")
      Game_So = input("Ma ciirayi rabtaa? ")
      break
    else:
      print("Haa ama maya!")      

while Game_En.isalpha() == True or Game_So.isalpha() == True:
  if Game_En.isalpha() == True:
    Game_En = Game_En.lower()
    if Game_En == "yes":  
      original = input('Enter a word:')
      if len(original) > 0 and original.isalpha():
        print(original)
      else:
        print("Try Again")
      word = original.lower()
      first = word[0]
      new_word = word + first + pyg
      new_word = new_word[1:len(new_word)]
      print(new_word)  
      print("Thanks for playing, have a nice day!")
      break
    if Game_En == "no":  
      print("Bye Bye!")
      break
  if Game_So.isalpha() == True:
    Game_So = Game_So.lower()
    if Game_So == "haa":  
      original = input('Qor eeriyad:')
      if len(original) > 0 and original.isalpha():
        print(original)
      else:
        print("Qor mar kale")
      word = original.lower()
      first = word[0]
      new_word = word + first + pyg
      new_word = new_word[1:len(new_word)]
      print(new_word)  
      print("Mahdasanid. Maalin wanaagsan")
      break
    if Game_So == "maya":  
      print("Salamullah!")
      break