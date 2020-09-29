import random

word_list = ['menu', 'restroom', 'mutation',
'jockey', 'leaflet', 'complain',
'health', 'heal', 'prevalence',
'gossip', 'side', 'exploration',
'statement', 'customer', 'fee',
'dividend', 'shake', 'sushi','boba',
'spectacular', 'speaker', 'terrfic',
'awesome', 'deleting', 'hangman', 'gymnastics'
'yoga']

game_status = "restarting"
while True:
    if game_status == "restarting":
        guess_count = 0
        letters = list()
        word = word_list[random.randint(0, len(word_list)-1)]
        for i in range(len(word)):
            letters.append('_')
        print("LET'S PLAY HANGMAN!")
        print("Your word: " + ("_"*len(word)))
        letters_guessed = list()
    if guess_count == len(word) * 2:
        print("YOU GUESSED TOO MANY TIMES! YOU LOSE!")
        print("Your word was " + word)
        play_again = input("Would you like to play again? (type 'yes' or 'no')")
        if play_again == 'yes':
            game_status = "restarting"
            continue
        elif play_again == 'no':
            break
        else:
            print("I did not understand that; I assume you don't want to play.")
            break
    print("Pick a letter: ")
    letter = input()
    if letter.isalpha() and len(letter) == 1:
        blankword = ""
        if letter in word:
            index_count = 0
            for i in word:
                if i == letter:
                    letters[index_count] = i
                index_count += 1
            for i in letters:
                blankword += i
            print(blankword)
            if blankword == word:
                print("YOU WIN!")
                play_again = input("Would you like to play again? (type 'yes' or 'no')")
                if play_again == 'yes':
                    game_status = "restarting"
                    continue
                else:
                    break

        else:
            print("Sorry, that letter isn't in the word! Try again...")
            guess_count += 1
            print(blankword)
        letters_guessed.append(letter)
        print("You have guessed these letters: ", letters_guessed)
        print("You have " + str((len(word)*2) - guess_count) + " strikes left.")
    else:
        print("Not a valid letter.")
    game_status = "in progress"

print("Thanks for playing hangman!")
