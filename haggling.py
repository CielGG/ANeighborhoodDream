def haggling():
    import random

    print("• Willow, The Snake Merchant • \n\nWelcome to my ssstore, are you interesssted in buying thisss? \nOh? The price isssn't to your liking? Well, why ssshould I change my price for you?")
    print("\n• RULES OF THE GAME • \nYour job is to guess the customers reason for buying that item. \nYou do this by typing a LETTER of your choosing\
    \nThe customer will describe the word before guessing! That is your hint. \nYou have 5 strikes or else the customer will walk out!\n")

    while True:
        # Mission Bit core values
        family = ['f', 'a', 'm', 'i', 'l', 'y']
        friend = ['f', 'r', 'i', 'e', 'n', 'd']
        betrayal = ['b', 'e', 't', 'r', 'a', 'y', 'a', 'l']
        reckless = ['r', 'e', 'c', 'k', 'l', 'e', 's', 's']
        opportunity = ['o', 'p', 'p', 'o', 'r', 't', 'u', 'n', 'i', 't', 'y']
        neighborhood = ['n', 'e', 'i', 'g', 'h', 'b', 'o', 'r', 'h', 'o', 'o', 'd']
        intelligence = ['i', 'n', 't', 'e', 'l', 'l', 'i', 'g', 'e', 'n', 'c', 'e']

        words = [family, friend, betrayal, neighborhood, opportunity, intelligence, reckless]
        random_word = random.choice(words)
        length = len(random_word)
        empty = ['_'] * length
        wrong_letters = []

        strikes = 0 

        description = {
            "family": "• The Customer • \nMy dad\'s birthday is soon, my broom just broke and I can\'t miss his birthday. It\'s been years since I\'ve visited.\nI wanna cherish the time I have left with him, is there any way for you to lower the price? Please?", 
            "friend": "• The Customer • \nHowdy, I heard you sell high quality wands for cheaper than the big stores in the city. \nAn important person to me has been wanting a wand for years and she just passed her AoM credentials. So I thought it only fit to get her one.",
            "betrayal": "• Isla, The Adventurer • \nHey Willow, I heard you\'ve been selling some interesting things recently...Apparently, some fairies as lanterns? \nJust rumors I\'ve been hearing of course. Since I\'m your dear neighbor can I get one voodoo doll for a discount?",
            "reckless": "• The Customer • \nHI! I don\'t have much money right now, but the forbidden spell book you\'re selling would really help with my situation! \nI don\'t know magic and it isn\'t the smartest thing to do, but I gotta make ends meet y\'know? So...could I ask for a cheaper price?",
            "opportunity": "• The Customer • \nOh, hello! You have speed-boost potions, right? Is there anything I can do to get a cheaper price? Huh, that looks similar to Esmerelda\'s...",
            "neighborhood": "• The Customer • \nHi!! Love your hair! I\'ve been looking everywhere for paper lanterns for the upcoming festival! You\'re going too right? I\'m a little short on cash, is that okay?",
            "intelligence": "• Lupin, The Professor • \n\'Ello, Willow. I \'eard you sell feathered pen kits? Can I get one \'em? Blimey! This price is far too high! Do you know your prices Willow??"
        }
        # no phew okok

        if length == 6:
            print('• Attempt •')
            if random_word == family:
                print(description['family'])
            else:
                print(description['friend'])
            while random_word: 
                user_input = input('\nEnter a letter: ').lower() 
                for i in range(length):
                    if user_input == random_word[i]:
                        if random_word[i] == random_word[i]:
                            empty[i] = random_word[i]
                for i in range(length):
                    print(empty[i] + ' ', end='')

                if user_input not in random_word:
                    strikes += 1        
                    if user_input in wrong_letters:
                        strikes -= 1
                    elif len(user_input) != 1:
                        print('\nInvalid choice')
                    else:
                        wrong_letters.append(user_input)
                    print(f"\nThats the wrong letter")
                    
                print(f"\nStrikes: {strikes}/5\nWrong letters: {wrong_letters}")  
                if strikes == 5:
                    print("\nYou lose, the customer left without buying anything.")
                    break
                elif '_' not in empty:
                    print('You win! You successfully scammed the customer :D!!')
                    break
                else:
                    continue

        if length == 8:
            print('• Attempt •')
            if random_word == betrayal:
                print(description['betrayal']) 
            else:
                print(description['reckless'])
            while random_word: 
                user_input = input('\nEnter a letter: ').lower() 

                for i in range(length):
                    if user_input == random_word[i]:
                        if random_word[i] == random_word[i]:
                            empty[i] = random_word[i]
                for i in range(length):
                    print(empty[i] + ' ', end='')

                if user_input not in random_word:
                    strikes += 1        
                    if user_input in wrong_letters:
                        strikes -= 1
                    elif len(user_input) != 1:
                        print('\nInvalid choice')
                    else:
                        wrong_letters.append(user_input)
                    print(f"\nThats the wrong letter")

                print(f"\nStrikes: {strikes}/5\nWrong letters: {wrong_letters}")  
                if strikes == 5:
                    print("\nYou lose, the customer left without buying anything.")
                    break
                elif '_' not in empty:
                    print('You win! You successfully scammed the customer :D!!')
                    break
                else:
                    continue

        if length == 11:
            print('• Attempt •')
            print(description["opportunity"]) 
            while random_word: 
                user_input = input('\nEnter a letter: ').lower() 
                for i in range(length):
                    if user_input == random_word[i]:
                        if random_word[i] == random_word[i]:
                            empty[i] = random_word[i]
                for i in range(length):
                    print(empty[i] + ' ', end='')

                if user_input not in random_word:
                    strikes += 1        
                    if user_input in wrong_letters:
                        strikes -= 1
                    elif len(user_input) != 1:
                        print('\nInvalid choice')
                    else:
                        wrong_letters.append(user_input)
                    print(f"\nThats the wrong letter")

                print(f"\nStrikes: {strikes}/5\nWrong letters: {wrong_letters}")  
                if strikes == 5:
                    print("\nYou lose, the customer left without buying anything.")
                    break
                elif '_' not in empty:
                    print('You win! You successfully scammed the customer :D!!')
                    break
                else:
                    continue

        if length == 12:
            print('• Attempt •')
            if random_word == neighborhood:
                print(description["neighborhood"]) 
            else:
                print(description["intelligence"]) 
            while random_word: 
                user_input = input('\nEnter a letter: ').lower() 
                for i in range(length):
                    if user_input == random_word[i]:
                        if random_word[i] == random_word[i]:
                            empty[i] = random_word[i]
                for i in range(length):
                    print(empty[i] + ' ', end='')

                if user_input not in random_word:
                    strikes += 1        
                    if user_input in wrong_letters:
                        strikes -= 1
                    elif len(user_input) != 1:
                        print('\nInvalid choice')
                    else:
                        wrong_letters.append(user_input)
                    print(f"\nThats the wrong letter")
                    #  

                print(f"\nStrikes: {strikes}/5\nWrong letters: {wrong_letters}")  
                if strikes == 5:
                    print("\nYou lose, the customer left without buying anything.")
                    break
                elif '_' not in empty:
                    print('You win! You successfully scammed the customer :D!!')
                    break
                else:
                    continue
        
        your_answer = input('Do you wish to continue this dream(y/n)? ').lower()
        if your_answer == 'y':
            continue
        elif your_answer == 'n':
            print('You have left the dream world.')
            break
        else:
            print('I\'m sorry, what did you say?')
            your_answer = input('Do you wish to continue this dream(y/n)? ').lower()
            if your_answer == 'n':
                break

    print("\n • ??'s Ending • \nAfter a long day of haggling and dealing with tiring customers. Willow closes the front door and flips the sign to closed. \nYou weren't able to fully breath in the atmosphere of the store." \
    "The gloomy weight of the air and random belongings, that don't match at all, \nscattered around the room feel off. You can tell something grim has happened in here. You go behind the cash register, \nyou hadn't noticed the drawers next to it." \
    "Curiously, you open the drawer, wondering what Willow could possibly be hiding." \
    "In shock, you see random trinkets, and a plastic piece of what looks like 2 guild IDs." \
    "On one, it says 'Willow'. On the other it says..." \
    "\n\nAzareth? Both have the snakey face on it. The one belonging to Azareth seems older and more accurate compared to its cheaply made copy." \
    "\n\nSo...who is Willow? Or should I say Azareth? Are either even their real name..?")