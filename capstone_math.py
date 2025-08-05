import random

# Easy Math (addition/subtraction)
def cap_math():
    def easy():
        # Subtraction

        for i in range(2):
            easy_sub_1, easy_sub_2 = random.randint(0,100), random.randint(0,20)
            easy_sub_answer = easy_sub_1 - easy_sub_2
            player_answer = input(f"{easy_sub_1} - {easy_sub_2} = ")
            if player_answer.lower() == "s":
                break
            player_answer = int(player_answer)
            if player_answer == easy_sub_answer:
                print("That's correct\n")
                
            else:
                print("This doesn't seem right. Let's try this again")
        
        # Addition
        # easy_add_1, easy_add_2 = random.randint(0,100), random.randint(0,100)
        # easy_add_answer = easy_add_1 + easy_add_2

        # while True:
        #     player_answer = input(f"{easy_add_1} + {easy_add_2} = ")
        #     if player_answer == "s" or "S":
        #         break
        #     player_answer = int(player_answer)
        #     if player_answer == easy_add_answer:
        #         print("That's correct\n")
        #         break
        #     else:
        #         print("This doesn't seem right. Let's try this again")

    # Medium (multiplication/division/exponents)
    def medium():
        # Multiplication
        while True:
            med_mult_1, med_mult_2  = random.randint(0,20), random.randint(0,20)
            med_mult_answer = med_mult_1 * med_mult_2
            player_answer = input(f"{med_mult_1} * {med_mult_2} = ")
            if player_answer.lower() == "s":
                break
            elif int(player_answer) == med_mult_answer:
                print("That's correct\n")
                break
            else:
                print("This doesn't seem right. Let's try this again")

        # Division
        med_div_1, med_div_2 = random.randint(0,20), random.randint(1,20)
        med_div_answer = round(med_div_1 / med_div_2, 1)

        while True:
            player_answer = input(f"To the nearest tenths: {med_div_1} / {med_div_2} = ")
            if player_answer.lower() == "s":
                break
            player_answer = float(player_answer)
            if player_answer == med_div_answer:
                print("That's correct\n")
                break
            else:
                print("This doesn't seem right. Let's try this again")

        # Exponents
        med_base, med_power = random.randint(0,10), random.randint(0,4)
        med_exponent_answer = med_base ** med_power

        while True:
            player_answer = input(f"{med_base} to the power of {med_power} = ")
            if player_answer.lower() == "s":
                break
            player_answer = int(player_answer)
            if player_answer == med_exponent_answer:
                print("That's correct\n")
                break
            else:
                print("This doesn't seem right. Let's try this again")

    # Hard (solve for x)
    def hard():

        hard_eq = {
        '1': "2x - 5 + 8x = 6x + 7",
        '2': "3(x+2) - 12 = -27"
        }
        hard_eq_ans = {
            '1': '3',
            '2': '-7'
        }

        while True:
            hints = ["Isolate the variable", "Isolate the constant", "Divide constant by coefficient of x"]
            fails = 0
            correct = 1
            hint_count = 0

            random_hard_eq = random.choice(list(hard_eq.keys()))

            player_answer = input(f'Solve for x: {hard_eq[random_hard_eq]}: ')

            if random_hard_eq == '1':
                answer = hard_eq_ans['1']
                if player_answer.lower() == 's':
                    break
                elif player_answer == answer:
                    print("That's correct!\n")
                    correct += 1
                    break
                else:
                    print("This doesn't seem right. Let's try this again.\n")
                    fails += 1
            elif random_hard_eq == '2':
                answer = hard_eq_ans['2']
                if player_answer.lower() == 's':
                    break
                elif player_answer == answer:
                    print("That's correct!\n")
                    correct += 1
                    break
                else:
                    print("This doesn't seem right. Let's try this again.\n")
                    fails += 1

            if 3 <= fails < 6 and hint_count < len(hints):
                player_hint = input('Do you want a hint? (y/n): ').lower()
                if player_hint == 'y':
                    print(hints[hint_count] + "\n")
                    hint_count += 1

            
            # player_answer = input(f"Solve for x: {hard_eq[random_hard_eq]}: ")
            # if player_answer.lower() == "s":
            #     break
            # if player_answer == hard_eq_ans[f"hard_eq_ans_{str(correct)}"]:
            #     print("That's correct \n")
            #     correct += 1
            #     break
            # else:
            #     print("This doesn't seem right. Let's try this again.\n")
            #     fails += 1

            # if 6 > fails >= 3 :
            #     player_hint = input("Do you want a hint? (y/n) ").lower()
            #     if player_hint == 'y':
            #         print(hints[hint_count])
            #         hint_count += 1

    # cutscene
    def math_pass():
        print("\n\n • Lupin\'s Ending • \nYou: Phew, all done grading these tests. That was harder than I expected. I am feeling a little tired. A quick nap wouldn’t hurt...\n"\
            "\nYou wake up from your everlasting dream to a new morning away from those horrid numbers. You gain a new understandinding of Lupin's hectic worklife." \
            "\nHaving to grade so many tests would tire anyone out. How has he managed to not go insane yet??" \
            "\nYou begin brewing a calming chamomile tea, known for its calming and sleep aiding abilities. Nervously, you head over to Lupin's house and begin knocking."\
            "\n'Who in the name of Odin is 'nocking this early in the morning. I ought to 'ave a word with you bumbling neighbors.'"\
            "\n'Bloody 'ell, you youngesters these days 'ave way too much tim... Oh is that for me? 'Ow did you know I 'aven't been able to sleep. Was it the eyebags?'"\
            "\n'For this I give you a B-, a respectable passing grade. Well, thanks for the tea neighbor, I ought to go back to sleep now before my next class starts'")
            
    def math_main():
        math_difficulty = input("(easy/medium/hard/all) ").lower()
        if math_difficulty == "easy":
            easy()
        elif math_difficulty == "medium":
            medium()
        elif math_difficulty == "hard":
            hard()
        elif math_difficulty == "all":
            easy()
            medium()
            hard()
        else:
            print('That isn\'t an option.')
        math_pass()

    print("You wake up in a large classroom, filled with several desks and a mountain of paperwork. \nOn the table next to you there is a large pile of ungraded tests. \n'Guess I should start grading..'")
    print("After a few hours, there are only a few tests left.\n 'Time to create the last few answer sheets..'")
    print("\nChoose which level of math difficulty you would like to solve. If you would like to skip the question type 's' when answering the question. ")
    math_main()
cap_math()