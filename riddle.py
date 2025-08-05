#RIDDLE
def riddle():
    print("Ah. Another traveller I see.") #ADD PLAYERS NAME WHEN EVERYTHING IS TOGETHER/MAKE INPUT IN BEGINNING OF GAME
    while True:
        riddle_question = input("I see in your minds eye..\nA riddle you seek! \nI shall grant your wish, after you share your desired difficulty. You may leave if you'd like, just say 'Exit' \n(Simple, Easy, Medium, Hard, Extreme): ").capitalize()
        if riddle_question == "Exit":
            break
    #RIDDLE easy DONE
        if riddle_question == 'Easy':
            print("I see, you are a smart one. You would like a calm mellow journey to ease your way into the winding path of riddles. And a riddle I shall give! You have 3 tries. ")
            for i in range(3):
                riddle_easy = input("\nWhy did the chicken cross the road?: ").capitalize()
                if riddle_easy == 'To get to the other side':
                    print("Correct! Wonderful! You have passed with flying colors. I enjoyed this chat, would you like to try another?\n ")
                    break
                else:
                    riddle_again = input("Wrong! Would you like to try again?: ").capitalize()
                    if riddle_again == 'No':
                        break

    #RIDDLE extra easy DONE
        elif riddle_question == 'Simple':
            print("I see, a light journey is what you seek. I shall deliver. You have 3 tries.")
            for i in range(3):
                riddle_extra = input("\nAlex's mom had four children. The first one was named May, the second was named June, and the third was named August. What was the fourth child's name? ").capitalize()
                if riddle_extra == "Alex":
                    print("Correct! Wonderful! You have passed with flying colors. I enjoyed this chat, would you like to try another?\n ")
                    break
                else:
                    riddle_again = input("Wrong! Would you like to try again?: ").capitalize()
                    if riddle_again == 'No':
                        break

    #RIDDLE medium
        elif riddle_question == 'Medium':
            print("The average response, nothing too hard or too easy for you. You like to test the waters without doubting or overestimating your ability to swim. I admire that. Well, here is your riddle. You have 3 tries, if you would like a hint, just tell me. ")
            for i in range(3):
                riddle_medium = input("\nA tangled truth \nno ease undone \nThe knife unravels \nwhat once was spun: ").capitalize()
                if riddle_medium == 'Hint':
                    print("\nHint 1: Focus on 'no ease undone'. What is something that is hard to undo, but able to 'unravel' with a knife? Dare I say, cut.")
                    riddle_medium_hint = input("Would you like another hint? ").capitalize()
                    if riddle_medium_hint == 'Yes':
                        print("\nHint 2: It's connected to rope. ")
                elif riddle_medium == 'Knot':
                    print("Correct! Wonderful! You have passed with flying colors. I enjoyed this chat, would you like to try another?\n ")
                    break
                else:
                    riddle_again = input("Wrong! Would you like to try again?: ").capitalize()
                    if riddle_again == 'No':
                        break
    #RIDDLE hard
        elif riddle_question == 'Hard':
            print("I see a truly brave character we have here. You have 3 tries. No matter how brave thou may be, if you would like a hint, just say it. Without further ado, here is the ultimate riddle: ")
            for i in range(3):
                riddle_hard = input("\nIf you throw me out the window, you'll leave a grieving wife, but drop me in the middle of a door, and you might just save a life. What am I? ").capitalize()
                if riddle_hard == 'Hint':
                    print("\n\nHint 1:There are 2 answers to this riddle. Think of the WORDS you are looking at, don't focus on WHAT it could be but WHERE it is.")
                    riddle_hard_hint = input("Would you like another hint? ").capitalize()
                    if riddle_hard_hint == 'Yes':
                        print("Hint 2: wiNdow? Throw it out of wiNdow.")
                elif riddle_hard == 'N':
                    print("Correct! How creative you are! Although, there is another answer. I suggest you try again! I enjoyed this chat, would you like to try another?\n ")
                    break
                elif riddle_hard == 'A baby':
                    print("Correct! Although, there is a more creative answer. I suggest you try again! I enjoyed this chat, would you like to try another?\n ")
                    break
                else:
                    riddle_again = input("Wrong! Would you like to try again?: ").capitalize()
                    if riddle_again == 'No':
                        break
    #RIDDLE EXTREMEE
        elif riddle_question == 'Extreme':
            print("Wow. Ha, you actually chose it. Well, you asked for it. One extreme riddle coming up. You have 3 tries, if you need a hint, just ask.")
            for i in range(3):
                riddle_extreme = input("\nWhat has four letters, sometimes has nine, always has six, and never has five? ").capitalize()
                if riddle_extreme == 'Hint':
                    print("Hint 1: Is it really a question?")
                    riddle_extreme_hint = input("Would you like another hint? ").capitalize()
                    if riddle_extreme_hint == 'Yes':
                        print("Hint 2: Hm, so it's not a question..What do you say to a statement? ")
                elif riddle_extreme == 'Yes':
                    print("Correct! Wonderful! You have passed with flying colors. I enjoyed this chat, would you like to try another?\n ")
                    break
                else:
                    riddle_again = input("Wrong! Would you like to try again?: ").capitalize()
                    if riddle_again == 'No':
                        break
#cutscene                    
    print("\n\n • Cairo's Ending • \n...You wake up from your everlasting dream. Feeling like a new person. You never knew your neighbor's life could be so enticing." \
    "\nYou gain a new appreciation for your neighbor Cairo." \
    "\nYou walk out of your house, looking for a particular fox. When you find them, you strike a conversation with them. Asking for a riddle." \
    "\n\n'I always appear with my companion. When you're close, we seem to arrive together. But from far away, I come first, and my companion follows. What am I?'" \
    "\n'Guess you'll have to think about it more~!'" \
    "\n'How did you know I loved riddles? Have you been stalking me comrad~?'" \
    "\n'Haha! Joking! Joking! I am curious though.'" \
    "\n\nYou: 'I just had a feeling.'")