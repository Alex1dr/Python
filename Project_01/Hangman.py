import random
print('H A N G M A N')

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')[:4]
    if menu == "exit":
        break
    elif menu == "play":
        list_word = ('python', 'java', 'kotlin', 'javascript')
        random_word = random.choice(list_word)
        input_list = ['-'] * len(random_word)
        all_litters_list = []
        lives = 1
        eng_lowercase_letters = list("eyuioaqwrtpsdfghjklzxcvbnm")
        while lives <= 8:
            flag_ = False
            flag_double = False

            print('')
            print("".join(input_list))
            input_letter = input("Input a letter: ")

            if input_letter in all_litters_list:
                flag_double = True


            for i in range(len(random_word)):
                if input_letter == random_word[i] and input_letter not in all_litters_list:
                    input_list[i] = input_letter
                    flag_ = True

            if not flag_:
                if len(input_letter) != 1:
                    print("You should input a single letter")
                elif input_letter not in eng_lowercase_letters:
                    print("Please enter a lowercase English letter")
                elif input_letter in all_litters_list:
                   print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word")
                    lives += 1
            all_litters_list.append(input_letter)

            if '-' not in input_list:
                break

        input_list_ = "".join(input_list)
        if input_list_ == random_word:
            #print()
            print(f"You guessed the word {input_list_}!\nYou survived!")
        else:
            print("You lost!")

