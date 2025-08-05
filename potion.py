# 12 ingredients
# Starter      # [1]Fire -         [1]Flaming Mushroom             [repels water]                  
# Expert       # [2]Fire/Wind -    [2]Phoenix Feather              [repels water]    

# Expert       # [3]Wind -         [3]Zephyr's Embrace             [repels earth]    
# Easy         # [4]Wind/Light -   [4]Windbloom                    [repels earth]

# Starter      # [5]Water -        [5]Mermaid Tear                 [repels fire]
# Intermediate # [6]Water/Earth -  [6]Lotus Core                   [repels fire]

# Easy         # [7]Light -        [7]Star Sap                     [repels dark]
# Intermediate # [8]Light -        [8]Angel's halo                 [repels dark]

# Easy         # [9]Dark -         [9]Handful of Shadow            [repels light]
# Intermediate # [10]Dark/Earth -  [10]Moonlit Root                [repels light]

# Starter      # [11]Earth -       [11]Qilin Scale                 [repels wind]
# Intermediate # [12]Earth/Light - [12]Starlit Crystal             [repels dark]
                             
# Starter      # [13]Binding -     [13]Leaves of Symphony          [water, fire]
# Expert       # [14]Binding -     [14]Dragon's Eye                [light, dark]
# Intermediate # [15]Binding -     [15]Pearl Essence               [water, light]
# Expert       # [16]Binding -     [16]Sage's Sorrow               [water, dark]
# EXexpert     # [17]Binding -     [17]Lucid Fantasy               [water, fire, earth, wind, dark, light]

# 20 potions (for now)
    #EASY 
        # Fire Resistance Potion - Fire Immunity
        # Healing Potion - Healer's Kiss
        # Beauty Potion - Femme Fatale
            # Plastic surgery in a bottle!
        # Hair Growth Potion - Anti-Bald
        # Speed Potion - Shooting Star
        # Strength Potion - 

    #MEDIUM
        # Fire Magic Potion 
        # Water Magic Potion
        # MP Up Potion
        # Stamina Potion
        # Water Breathing Potion
        # Voice Amplification
        # Telekinesis Potion 

    # HARD
        # Sleep Potion
            # WILL change sleeping schedule, extreme increase in melatonin levels in less than 10 minutes.
        # Love Potion - Dragon's Heart
            # May cause side effects, such as, happiness, extreme increase in dopamine levels
        # Elemental Potion
        # Time Travel Potion
        # Flight Potion 
        # Youth Potion
        # Night Vision Potion 
        # Invisibility Potion 
        # Veil of the Dreamcatcher
            # Known to restore dreams long lost, this potion, entwines th drinker in a tapestry of vivid, restorative visions.

#STARTER
    # Starter ingredients:
        # Fire ingredient - [1]Flaming Mushroom             [repels water]
        # musical leaves - [11]Leaves of Symphony           [binding ingredient]
        # Water ingredient - [5]Mermaid Tear                [repels fire]
        # Earth type - [10]Qilin Scale                      [repels wind]


#POTIONS
    # Easy Potions:
        # [1]Flaming Mushroom + [11]Qilin Scale = Fire Resistance
        # [5]Mermaid Tear + [10]Qilin Scale = Healing Potion
        # [1]Flaming Mushroom + [5]Mermaid Tear + [13]Leaves of Symphony = Beauty Potion
        # [4]Windbloom + [5]Mermaid Tear = Hair Growth Potion
        # [4]Windbloom + [7]Star Sap = Speed Potion
        # [1]Flaming Mushroom + [10]Qilin Scale = Strength Potion
        # [1]Flaming Mushroom + [4]Windbloom

    # Medium Potions:
        # [1]Flaming Mushroom + [2]Phoenix Feather = Fire Magic Potion
        # [6]Lotus Core + [7]Star Sap + [15]Pearl Essence = Water Magic Potion
        # [6]Lotus Core + [9]Handful of Shadow = Water Breathing Potion

    # Expert Potions
        # [7]Angel's Halo + [2]Phoenix's Feather + [6]Zephyr's Embrace  = Flight Potion
        # [6]Star Sap + [10]Moonlit Root + [12]Dragon's Eye = Night Vision Potion
        # [2]Phoenix Feather + [6]Lotus Core + [13]Leaves of Symphony = Elemental Potion
        # [6]Lotus Core + [10]Moonlit Root + [16]Sage's Sorrow = Sleep Potion


#POTION PRICES
    # Easy: 50
    # Medium: 150
    # Hard: 350

#INGREDIENT PRICES
    # Easy: 120
    # Intermediate: 150
    # Expert: 700
    # EXPERT: 3000

# Player class (ingredients, coins, potion)
# Start off with 4 ingredients
# Simple: 2 ingredients per potion
# Hard: 3 ingredients
# Customers ask for specific potion (class)
# Get coins for selling potions -> buy more ingredients
# Potion Collection + player can create other potions
# Story mode
# free mode
# list of unlockable ingredients + unlockable potions
# 2 classes, while loop, for loop, conditionals, exit option
# OPTIONAL: buy more customers by unlocking new areas/buying new advertisments -> 


#PUT CREDITS AT THE START OF GAME(when all games are put together)
#put ALL games + cutscenes together
#make cutscene/s
#figure out buying from shop
def potion():
    print("\n\nWelcome to my shop, sweetie! What kind of potion are you looking for?")
    print('• RULES •\nThe objective is to mix and match ingredients from your list into a potion and earn coins to buy higher level ingredients from the store. \nThere is a list of all locked potions with hints that reveals what elements are used for it.')
    print('-- Ingredients --\nEach ingredient follows 1 or 2 elements. The elements consists of [fire, water, earth, wind, light, dark]')
    print('There are some ingredients that do not follow these rules, namely the binding ingredients, which can bind two opposing elements')
    print('     - Opposing elements are: [fire and water], [earth and wind], [light and dark]')


    ingredients = []
    # class for the players
    class Player:
        def __init__(self):
            self.coins = 0
            self.starter = ['[1]Flaming Mushroom - fire', '[5]Mermaid Tear - water', '[11]Qilin Scale - earth', '[13]Leaves of Symphony - binding']
            self.easy = ['[4]Windbloom - wind', '[7]Star Sap - light']
            self.intermediate = ['[6]Lotus Core - water/earth', '[8]Angel\'s halo - light', '[9]Handful of Shadow - dark', '[10]Moonlit Root - earth/dark', '[12]Starlit Crystal - earth/light', '[15]Pearl Essence - binding']
            self.expert = ['[2]Phoenix Feather - fire/wind', '[3]Zephyr\'s Embrace - wind', '[14]Dragon\'s Eye - binding', '[16]Sage\'s Sorrow - binding', '[17]Lucid Fantasy - binding']
            self.potions = []
            self.locked_potions = "\nEasy: \nFire Resistence Potion: Fire, Earth \nHealing Elixir: Water, Earth \nBeauty Potion: Fire, Water, Binding \nHair Growth Potion: Wind, Water \nSpeed Potion: Wind, Light" \
                                "\nStamina Potion: Fire, Wind \nVoice Amplification Potion: Water, Binding; Water/Fire" \
                                "\n\nIntermediate: \nStrength Potion: Fire, Dark/Earth \nFire Magic Potion: Fire, Earth/Light \nWater Magic Potion: Water/Earth, Light, Binding \nMP UP Potion: Dark, Binding; Water/Light \nWater Breathing Potion: Water/Earth, Dark\
                                \n\nHard: \nSleeping Potion: Water/Earth, Dark/Earth, Binding; Water/Dark \nLove Potion: Wind, Light, Binding; Light/Dark \nElemental Potion: Fire/Wind, Water/Earth, Binding; Water/Fire, Binding; Light/Dark \nTime Travel Potion: Fire/Wind, Wind, Light" \
                                "\nFlight Potion: Fire/Wind, Wind, Light \nInvisibility Potion: Light, Dark/Earth, Binding; Light/Dark \nYouth Elixir: Light, Dark, Binding; Dark/Light \nThe End: Every Expert binding agent"
            
        def potions_list(self):
            print('\n• Your Potions •')
            self.potions = list(dict.fromkeys(self.potions))
            print(self.potions)
            print('_______________________________________________________')

        def ingredients_list(self):
            print('_______________________________________________________')
            print('\n• Your Ingredients •')
            print(self.starter)
        
        def locked_potions_list(self):
            print('_______________________________________________________')
            print('\n• Locked Potions List •')
            print(self.locked_potions)
            print('_______________________________________________________')

        def store(self):
            print('_______________________________________________________')
            print(f'\nWelcome to my store~ What are you here to buy today? \nType number to buy!\nCoins: {self.coins}\n')
            print('If ingredient is already bought, there is no need to buy it again.')
            print(f'\nEasy Ingredients ~ 120 coins')
            for i in range(2):
                print(f' • {self.easy[i]}')
            print(f'Intermediate Ingredients ~ 150 coins')
            for i in range(6):
                print(f' • {self.intermediate[i]}')
            print(f'\nExpert Ingredients ~ 700 coins')
            for i in range(4):
                print(f' • {self.expert[i]}')
            print(f'\nEXPERT Ingredients ~ 3000 coins')
            print(f' • {self.expert[4]}')

        def buy_ingredient(self):
            easy_price = 120
            intermediate_price = 150
            expert_price = 700
            EXPERT_price  = 3000

            while True:
                try:
                    bought_ingredient = int(input('\nBuy(Enter a number) or To Not Buy(type 0): '))
                    if bought_ingredient == 0:
                        break
                    else:
                        if self.coins < easy_price:
                            print('You don\'t have enough coins.')
                        elif self.coins < intermediate_price:
                            print('You don\'t have enough coins.')
                        elif self.coins < expert_price:
                            print('You don\'t have enough coins.')
                        elif self.coins < EXPERT_price:
                            print('You don\'t have enough coins.')
                        else:
                            print('What?')
                        # Easy
                        if self.coins >= 120:
                            if bought_ingredient == 4:
                                self.coins -= 120
                                bought_ingredient = self.easy[0]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 7:
                                self.coins -= 120
                                bought_ingredient = self.easy[1]
                                self.starter.append(bought_ingredient)
                            else:
                                return
                            
                        # Intermediate
                        if self.coins >= 150:
                            if bought_ingredient == 6:
                                self.coins -= 150
                                bought_ingredient = self.intermediate[0]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 8:
                                self.coins -= 150
                                bought_ingredient = self.intermediate[1]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 9:
                                self.coins -= 150
                                bought_ingredient = self.intermediate[2]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 10:
                                self.coins -= 150
                                bought_ingredient = self.intermediate[3]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 12:
                                self.coins -= 150
                                bought_ingredient = self.intermediate[4]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 15:
                                self.coins -= 150
                                bought_ingredient = self.intermediate[5]
                                self.starter.append(bought_ingredient)
                            else:
                                return
                            
                        # Expert               
                        if self.coins >= 700:
                            if bought_ingredient == 2:
                                self.coins -= 700
                                bought_ingredient = self.expert[0]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 3:
                                self.coins -= 700
                                bought_ingredient = self.expert[1]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 14:
                                self.coins -= 700
                                bought_ingredient = self.expert[2]
                                self.starter.append(bought_ingredient)
                            elif bought_ingredient == 16:
                                self.coins -= 700
                                bought_ingredient = self.expert[3]
                                self.starter.append(bought_ingredient)
                            else:
                                return
                        
                        if self.coins >= 3000:
                            if bought_ingredient == 17:
                                self.coins -= 150
                                bought_ingredient = self.expert[4]
                                self.starter.append(bought_ingredient)
                            else:
                                return
                            
                except ValueError:
                    # Code to handle the ValueError
                    print(f"Error: Could not convert to an integer. Please enter a valid number.")

    player = Player()
    #POTION PRICES
        # Easy: 30
        # Medium: 150
        # Hard: 350

    while True:
        player_action = input('\nWhat would you like to do: ingredients/potions list(i), locked potions (l), shop(s), potion-making(p), leave ').lower()

        while player_action == 'i':
            player.ingredients_list()
            player.potions_list()
            break

        while player_action == 'l':
            player.locked_potions_list()
            break
            

        while player_action == 's':
            player.store()
            player.buy_ingredient()
            break
            

        while player_action == 'p':
            player_choice = str(input('\nActions: ingredients/potions list(i), locked potions (l), shop(s), potion-making(p), leave\nWhat would you like to mix?(EX. 1/2, 1/5/10): ')).lower()
            print()

            # Starter Potions
            if '[1]Flaming Mushroom - fire' and '[5]Mermaid Tear - water' and '[11]Qilin Scale - earth' and '[13]Leaves of Symphony - binding' in player.starter:
                if player_choice == '1/11':
                    print('You have mixed Flaming Mushroom and Qilin Scale. \nYou got a Fire Immunity Potion! \nFire Resistance Potion: Great for when you need to save a princess against a fire breathing dragon!')
                    player.potions.append("Fire Immunity Potion [Flaming Mushroom + Qilin Scale]")
                    player.coins += 30
                elif player_choice == '5/11':
                    print('You have mixed Mermaid Tears and Qilin Scales. \nYou got a Healer\'s Kiss! \nHealing Elixir: An essential for any adventure you may embark on! Heals for 100 HP and heals overtime!')
                    player.potions.append("Healer's Kiss [Mermaid Tear + Quilin Scale]")
                    player.coins += 30
                elif player_choice == '1/5/13':
                    print('You have mixed Flaming Mushroom, Mermaid Tears, and Leaves of Symphony. \nYou got Femme Fatale! \nBeauty Potion: Plastic surgery in a bottle! Just picture the look you want and bam! Does not change species. NOT PERMANENT; Lasts for 1 hour.')
                    player.potions.append('Femme Fatale [Flaming Mushroom + Mermaid Tear + Leaves of Symphony]')
                    player.coins += 30
                elif player_choice == '4/5':
                    print('You have mixed Windbloom and Mermaid Tear. \nYou got Anti-Bald Potion! \nHair Growth Potion: Permanent fix for your hair-do! Does not change hairstyle. May cause side effects: Growth of hair on any and all body parts,  non-stop growth of hair.')
                    player.potions.append('Anti-Bald [Windbloom + Mermaid Tear]')
                    player.coins += 30
                elif player_choice == 'i':
                    player.ingredients_list()
                    player.potions_list()
                elif player_choice == 'l':
                    player.locked_potions_list()
                elif player_choice == 's':
                    player.store()
                    player.buy_ingredient()
                elif player_choice == 'leave':
                    break
                else:
                    print('Pumpkin, what are you doing?')
            
            # Easy Potions 
            elif '[1]Flaming Mushroom - fire' and '[5]Mermaid Tear - water' and '[11]Qilin Scale - earth' and '[13]Leaves of Symphony - binding' and '[4]Windbloom - wind' and '[7]Star Sap - light' in player.starter:   
                    if player_choice == '4/7':
                        print('You have mixed Windbloom and Star Sap. \nYou got Shooting Star! \nSpeed Potion: Zip Zap! Effects last for 30 secs. DO NOT drink entire bottle in one go, WILL lead to increased fatigue, memory loss, and minor time travel.')
                        player.potions.append('Shooting Star [Windbloom + Star Sap]')
                        player.coins += 30
                    elif player_choice == '1/4':
                        print('You have mixed Flaming Mushroom and Windbloom. \nYou got A Rush of Adrenaline! \nStamina Potion: Increases endurance against extensive physical exercise. Suited for longer battles or expeditions. \nMay lead to increased adrenaline or lung collapse. Lasts 10 minutes!')
                        player.potions.append('A Rush of Adrenaline [Flaming Mushroom + Windbloom]')
                        player.coins += 30
                    elif player_choice == '5/13':
                        print('You have mixed Mermaid Tear and Leaves of Symphony. \nYou got Mermaid\'s Song! \nVoice Amplification Potion: ONLY USE IN EMERGENCY. DOES NOT work well with microphones; will cause rupture of ears. \nAmplifies soundwaves of voice, should only be used if needed. May rupture ears of user and any in it\'s radius or cause permanent damage to lungs. Lasts 2 minutes.')
                        player.potions.append('Mermaid\'s Song [Mermaid Tear + Leaves of Symphony]')
                        player.coins += 30
                    elif player_choice == 'i':
                        player.ingredients_list()
                        player.potions_list()
                    elif player_choice == 'l':
                        player.locked_potions_list()
                    elif player_choice == 's':
                        player.store()
                        player.buy_ingredient()
                    elif player_choice == 'leave':
                        break
                    else:
                        print('Pumpkin, what are you doing?')
                    
            # Medium
            elif '[1]Flaming Mushroom - fire' and '[5]Mermaid Tear - water' and '[11]Qilin Scale - earth' and '[13]Leaves of Symphony - binding' and '[4]Windbloom - wind' and '[7]Star Sap - light' and '[6]Lotus Core - water/earth' and '[8]Angel\'s halo - light' and '[9]Handful of Shadow - dark' and '[10]Moonlit Root - earth/dark' and '[12]Starlit Crystal - earth/light' and '[15]Pearl Essence - binding' in player.starter:
                if player_choice == '1/10':
                    print('You have mixed Flaming Mushroom and Moonlit Crystal. \nYou got Herculean Power! \nStrength Potion: Hercules-like strength in a bottle! Causes increased adrenaline, may temporarily alter muscle size. Lasts for 1 minute. \nDO NOT drink multiple servings at once. Will lead to dumbification of the user\'s brain, inablity to talk, loss of self, constant fatigue that never goes away, etc.')
                    player.potions.append('Herculean Power [Flaming Mushroom + Moonlit Root]')
                    player.coins += 150
                elif player_choice == '1/12':
                    print('You have mixed Flaming Mushroom and Starlit Crystal. \nYou got Breath of A Fire Spirit! \nFire Magic Potion: Allows user to manipulate fire! If poured on a flammable material, WILL start a fire. Not recommended to pour more than a drop on any flammable material. Can be mixed with Water Magic Potion. Lasts for 1 hour when consumed.')
                    player.potions.append('Breath of A Fire Spirit [Flaming Mushroom + Starlit Crystal]')
                    player.coins += 150
                elif player_choice == '6/7/15':
                    print('You have mixed Lotus Core, Star Sap, and Pearl Essence. \nYou got Water Spirit\'s Gift! \nWater Magic Potion: Allows user to manipulate water! Recommended to use underwater for best effects! Does not have nutritional benefits of actual water. If poured on surface, will spawn water on surface. Can put out any flame caused by Fire Magic Potion. Lasts for 1 hour when consumed. ')
                    player.potions.append('Water Spirit\'s Gift [Lotus Core + Star Sap + Pearl Essence]')
                    player.coins += 150
                elif player_choice == '12/15':
                    print('You have mixed Pearl Essence and Starlit Crystal. \nYou got Mana Restorer! \nMP Up Potion: Permanently increases user\'s max mana! Temporarily refills mana as well. ')
                    player.potions.append('Mana Restorer [Pearl Essence +R Starlit Crystal]')
                    player.coins += 150
                elif player_choice == '6/9':
                    print('You have mixed Lotus Core and Handful of Shadow. \nYou got Mana Restorer! \nMP Up Potion: Permanently increases user\'s max mana! Temporarily refills mana as well. ')
                    player.potions.append('Ocean\'s Breath [Lotus Core + Handful of Shadow]')
                    player.coins += 150
                elif player_choice == 'i':
                    player.ingredients_list()
                    player.potions_list()
                elif player_choice == 'l':
                    player.locked_potions_list()
                elif player_choice == 's':
                    player.store()
                    player.buy_ingredient()
                elif player_choice == 'leave':
                    break
                else:
                    print('Pumpkin, what are you doing?')

            # Hard
            elif '[1]Flaming Mushroom - fire' and '[5]Mermaid Tear - water' and '[11]Qilin Scale - earth' and '[13]Leaves of Symphony - binding' and '[4]Windbloom - wind' and '[7]Star Sap - light' and '[6]Lotus Core - water/earth' and '[8]Angel\'s halo - light' and '[9]Handful of Shadow - dark' and '[10]Moonlit Root - earth/dark' and '[12]Starlit Crystal - earth/light' and '[15]Pearl Essence - binding' and '[2]Phoenix Feather - fire/wind' and '[3]Zephyr\'s Embrace - wind' and '[14]Dragon\'s Eye - binding' and '[16]Sage\'s Sorrow - binding' and '[17]Lucid Fantasy - binding' in player.starter:
                if player_choice == '6/10/16':
                    print('You have mixed Lotus Core, Moonlit Root, Sage\'s Sorrow. \nYou got Sorrowful Slumber! \nSleeping Potion: WILL alter sleeping schedule, extreme increase in melatonin levels in less than 10 minutes. May alter dreams.')
                    player.potions.append('Sorrowful Slumber [Lotus Core + Moonlit Root + Sage\'s Sorrow]')
                    player.coins += 350
                elif player_choice == '3/8/14':
                    print('You have mixed Zephyr\'s Embrace, Angel\'s Halo, and Dragon\'s Eye. \nYou got Dragon\'s Heart! \nLove Potion: "I only have eyes for you" Made with dragon\'s eyes; Dragons are known for only having one mate, so use it carefully!! May cause side effects, such as, happiness, extreme increase in dopamine levels. ')
                    player.potions.append('Dragon\'s Heart [Zephyr\'s Embrace + Angel\'s Halo + and Dragon\'s Eye]')
                    player.coins += 350
                elif player_choice == '7/13/16':
                    print('You have mixed Phoenix Feather, Lotus Core, Leaves of Symphony, and Dragon\'s Eye. \nYou got Elemental Controller! \nElemental Potion: The ultimate potion for elemental magic. Allows user to manipulate all elements. ')
                    player.potions.append('Elemental Controller [Phoenix Feather + Lotus Core + Leaves of Symphony + and Dragon\'s Eye]')
                    player.coins += 350
                elif player_choice == '2/3/8':
                    print('You have mixed Phoenix Feather, Zephyr\'s Embrace, Angel\'s Halo. \nYou got Wings of A Phoenix! \nFlight Potion: Allows user to alter their own gravity, when they choose. Duration depends on user\'s max mana. Potion absorbs user\'s mana through every use. ')
                    player.potions.append('Wings of A Phoenix [Phoenix Feather + Zephyr\'s Embrace + Angel\'s Halo.]')
                    player.coins += 350
                elif player_choice == '8/10/14':
                    print('You have mixed Angel\'s Halo, Moonlit Root, and Dragon\'s Eye. \nYou got Where the Eyes Cannot See! \nInvisibility Potion: Allows user to control when they become invisible. Hides user as potion is consumed. If potion is not consumed fully; invisibility will only affect part of the user. Lasts indefinitely depending on user. ')
                    player.potions.append('Where the Eyes Cannot See [Angel\'s Halo + Moonlit Root + and Dragon\'s Eye]')
                    player.coins += 350
                elif player_choice == '8/9/14':
                    print('You have mixed Angel\'s Halo, Handful of Shadow, and Dragon\'s Eye. \nYou got Everlasting Youth! \nYouth Elixir: Rewinds the wrinkles of time. Use wisely! May rewind user\'s appearance too far back if focus is diverted. Can be reversed: ask Esmerelda for further questions. ')
                    player.potions.append('Everlasting Youth [Angel\'s Halo + Handful of Shadow + and Dragon\'s Eye]')
                    player.coins += 350
                elif player_choice == '2/3/14/16/17':
                    ending_cutscene = input("Do you want to continue?\nIf you continue, the game will end and you will lose your progress.\n")
                    if ending_cutscene == 'yes':
                        print("\n• Esmerelda Secret Ending •: \n'Why hello there, darling.'" \
                        "\n'Did you enjoy living my life? How did you like potionmaking?'\
                        \n'Oh, don't try to talk, you're teeth will fall out orrr you'll drown in your consiousness.'" \
                        "\n'If you took a liking to the brewing of magic. You can become my darling apprentice. Once you've woken, of course. Come and visit me at my shop.'" \
                        "\n\n'Ah, one more thing, be careful of that snake. Believe me when I say that they are not to be trusted, okay?'")
                    else:
                        break
                    print('You have mixed Phoenix Feather, Zephyr\'s Embrace, Dragon\'s Eye, Sage\'s, and Lucid Fantasy. You\'ve achieved the Veil of The Dreamcatcher! \nInvisibility Potion: Known to restore dreams long lost, this potion, entwines the drinker in a tapestry of vivid, restorative visions. This is a dream. Isn\'t it? ')
                    player.potions.append('Veil of The Dreamcatcher')
                elif player_choice == 'i':
                    player.ingredients_list()
                    player.potions_list()
                elif player_action == 'l':
                    player.locked_potions_list()
                elif player_choice == 's':
                    player.store()
                    player.buy_ingredient()
                elif player_choice == 'leave':
                    break
                else:
                    print('Pumpkin, what are you doing?')
            else:
                print('What')
                    

        if player_action == 'leave':
            break
        
    #cutscene
    print("\n\n • Esmerelda Normal Ending • \nYou awaken from your everlasting dream, that felt so scarily real." \
    "\nYou never knew the life your mysterious neighbor led. This experience has given you a new appreciation for Esmerelda and all her wisdom." \
    "\nFeeling empowered by your vivid dream, you step outside and head straight for the elf's humble potion shop." \
    "\n'Oh! What an unexpected face! Darling, what brings you here?'" \
    "\n'Hm..You just wanted to talk? Interesting, well, what did you want to talk about sweetie?'" \
    "\nAfter talking with your dear friend, you two have never been closer." \
    "\nYou've always wanted to become closer with her, but could never find the right words." \
    "\nAfter your dream, there are too many words to say.")
