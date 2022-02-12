def findthecharachter(letter1,word):
   foundtheletter = False
   currentlocation = 0
   while foundtheletter == False:
       if word[currentlocation] == letter1:
           foundtheletter = True

       else:
           currentlocation=currentlocation+1
   return currentlocation

MAX_TRIES = 6
current_tries = 0
save_the_charechter = 0
HANGMAN_ASCII_ART = "hangman"
how_many_letters_habe_been_found = 0
THE_WORD_TO_GUESS = input("please intert the word we are going to play with ")
LENTH_OF_THE_WORD = len(THE_WORD_TO_GUESS)
THE_WORD = str("_" * LENTH_OF_THE_WORD)
print(THE_WORD)
guessletter = "none"
while current_tries < MAX_TRIES and how_many_letters_habe_been_found<LENTH_OF_THE_WORD:
    guessletter = input('please insert a letter').lower()
    if guessletter in THE_WORD_TO_GUESS:
        save_the_charechter=findthecharachter(guessletter,THE_WORD_TO_GUESS)
        print("the letter has been found in the word in the place:" + str(save_the_charechter+1)
        how_many_letters_habe_been_found = how_many_letters_habe_been_found+1
    else:
        print("the letter has not been found in the word")
        current_tries = current_tries+1

if(current_tries == MAX_TRIES):
    print("you lost :(")
else:
    print("you have won :)")


