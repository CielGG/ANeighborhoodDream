

def rpg():
    print(f'\nWelcome Traveler!\nI knew we were destined to meet!\nWe\'ve got no time to waste, let\'s make haste!')
    print('I shall bring you to take a peek into the thrilling life of Isla the Adventurer, and your very lovely neighbor.\n')

    # superclass Creatures
    class Creatures:
        def __init__(self):
            self.health = 50
            self.level = 0
            self.attack = 10
            self.exp = 0
            self.skill_attack = 20

    # subclass Goblin
    class Goblin(Creatures):
        def __init__(self):
            super().__init__() # allows access to superclass attributes
            self.goblin_health = 50
            self.goblin_attack = 15

        def goblin_attacks_flame(self, flame):
            print(f'Goblin attacks! Your familiar takes {self.goblin_attack} damage!')
            flame.health -= self.goblin_attack

        def goblin_attacks_onyx(self, onyx):
            print(f'Goblin attacks! Your familiar takes {self.goblin_attack} damage!')
            onyx.health -= self.goblin_attack

        def goblins_health(self):
            print(f'\nGoblin health: {self.goblin_health}')
            if self.goblin_health <= 0:
                print('You have defeated Goblin! +500 exp')

    # subclass Ogre
    class Ogre(Creatures):
        def __init__(self):
            super().__init__()
            self.ogre_health = 100
            self.ogre_attack = 20

        def ogre_attacks_flame(self, flame):
            print(f'Ogre attacks! Your familiar takes {self.ogre_attack} damage!')
            flame.health -= self.ogre_attack

        def ogre_attacks_onyx(self, onyx):
            print(f'Ogre attacks! Your familiar takes {self.ogre_attack} damage!')
            onyx.health -= self.ogre_attack

        def ogres_health(self):
            print(f'\nOgre health: {self.ogre_health}')
            if self.ogre_health <= 0:
                print('You have defeated Ogre! +700 exp')

    # subclass Flame
    class Flame(Creatures):
        def __init__(self):
            super().__init__()
            self.skills = ['Crimson Storm']

        def flame_attack(self, goblin, ogre): # flame attack method
            print(f'Flame attacks!')
            if fight_who == 'ogre':
                ogre.ogre_health -= self.attack
                print(f'Ogre takes {self.attack} damage!')
                if ogre.ogre_health < 0:
                    ogre.ogre_health = 0
                ogre.ogres_health()
            else:
                goblin.goblin_health -= self.attack
                print(f'Goblin takes {self.attack} damage!')
                if goblin.goblin_health < 0:
                    goblin.goblin_health = 0
                goblin.goblins_health()

        def flame_crimson_storm(self, goblin, ogre): # flame skill method
            if fight_who == 'ogre':
                ogre.ogre_health -= self.skill_attack
                print(f'Ogre takes {self.skill_attack} damage!')
                if ogre.ogre_health < 0:
                    ogre.ogre_health = 0
                ogre.ogres_health()
            else:
                goblin.goblin_health -= self.skill_attack
                print(f'Goblin takes {self.skill_attack} damage!')
                if goblin.goblin_health < 0:
                    goblin.goblin_health = 0
                goblin.goblins_health()

        def status(self): # flame status method
            print('\n• Flame • ')
            print(f'--Status--\nLevel: {self.level}\nExp: {self.exp}/1000\n'
                f'Health: {self.health}\nAttack: {self.attack}\nSkills: {self.skills}\n')
            
        def level_up(self): # flame level up method
            if self.exp < 1000:
                print('\nFlame does not have enough experience, fight more monsters to level up.')
            else:
                print(f'\nYour pet has leveled up!')
                self.health += 50
                self.level += 1
                self.attack += 5
                self.skill_attack += 5
                self.exp -= 1000

    # subclass Onyx
    class Onyx(Creatures):
        def __init__(self):
            super().__init__()
            self.onyx_skills = ['Onyx Blast'] # if we have time add Crystalization as ult

        def onyx_attack(self, goblin, ogre): # onyx attack method
            print(f'Onyx attacks!')
            if fight_who == 'ogre':
                ogre.ogre_health -= self.attack
                print(f'Ogre takes {self.attack} damage!')
                if ogre.ogre_health < 0:
                    ogre.ogre_health = 0
                ogre.ogres_health()
            else:
                goblin.goblin_health -= self.attack
                print(f'Goblin takes {self.attack} damage!')
                if goblin.goblin_health < 0:
                    goblin.goblin_health = 0
                goblin.goblins_health()

        def onyx_onyx_blast(self, goblin, ogre): # onyx skill method
            if fight_who == 'ogre':
                ogre.ogre_health -= self.skill_attack
                print(f'Ogre takes {self.skill_attack} damage!')
                if ogre.ogre_health < 0:
                    ogre.ogre_health = 0
                ogre.ogres_health()
            else:
                goblin.goblin_health -= self.skill_attack
                print(f'Goblin takes {self.skill_attack} damage!')
                if goblin.goblin_health < 0:
                    goblin.goblin_health = 0
                goblin.goblins_health()

        def status(self): # onyx status method
            print('\n• Onyx • ')
            print(f'--Status--\nLevel: {self.level}\nExp: {self.exp}/1000\n'
                f'Health: {self.health}\nAttack: {self.attack}\nSkills: {self.onyx_skills}\n')
            
        def level_up(self): # onyx level up method
            if self.exp < 1000:
                print('\nOnyx does not have enough experience, fight more monsters to level up.')
            else:
                print(f'\nYour pet has leveled up!')
                self.health += 50
                self.level += 1
                self.attack += 5
                self.skill_attack += 5
                self.exp -= 1000

    flame = Flame()
    onyx = Onyx()

    # function for fighting Goblin
    def fighting_goblin(flame, onyx):
        goblin = Goblin()
        ogre = Ogre()
        if familiar_choice.capitalize() == 'Flame': # if choice = flame
            health = flame.health
            print('You have encountered Goblin!\nThe battle begins!\n')
            goblin.goblins_health()
            print(f'Flame health: {flame.health}')
            while goblin.goblin_health > 0:
                familiar_action = input('\nAttack: Normal Attack (a) / Skill Attack (s)\n').lower()
                if familiar_action == 'a':
                    flame.flame_attack(goblin, ogre)
                elif familiar_action == 's':
                    flame.flame_crimson_storm(goblin, ogre)
                else:
                    print("Invalid attack choice.")
                    continue
                if goblin.goblin_health <= 0:
                    flame.exp += 500
                    flame.health = health
                    print('Goblin has been defeated!')
                    print('You never realised fighting would be this exciting and so easy!')
                    return
                goblin.goblin_attacks_flame(flame)
                if flame.health <= 0:
                    flame.health = health
                    print('Flame has been defeated!')
                    return
                print(f'Flame health: {flame.health}')

        else: # if choice = onyx
            health = onyx.health
            print('You have encountered Goblin!\nThe battle begins!\n')
            goblin.goblins_health()
            print(f'Onyx health: {onyx.health}')
            while goblin.goblin_health > 0:
                familiar_action = input('\nAttack: Normal Attack (a) / Skill Attack (s) \n').lower()
                if familiar_action == 'a':
                    onyx.onyx_attack(goblin, ogre)
                elif familiar_action == 's':
                    onyx.onyx_onyx_blast(goblin, ogre)
                else:
                    print("Invalid attack choice.")
                    continue
                if goblin.goblin_health <= 0:
                    onyx.exp += 500
                    onyx.health = health
                    print('Goblin has been defeated!')
                    print('You never realised fighting would be this exciting and so easy!')
                    return
                goblin.goblin_attacks_onyx(onyx)
                if onyx.health <= 0:
                    onyx.health = health
                    print('Onyx has been defeated!')
                    return
                print(f'Onyx health: {onyx.health}')

    # function for fighting Ogre
    def fighting_ogre(flame, onyx):
        goblin = Goblin()
        ogre = Ogre()
        if familiar_choice.capitalize() == 'Flame': # if choice = flame
            health = flame.health
            print('You have encountered Ogre!\nThe battle begins!\n')
            ogre.ogres_health()
            print(f'Flame health: {flame.health}')
            while ogre.ogre_health > 0:
                familiar_action = input('\nAttack: Normal Attack (a) / Skill Attack (s) \n').lower()
                if familiar_action == 'a':
                    flame.flame_attack(goblin, ogre)
                elif familiar_action == 's':
                    flame.flame_crimson_storm(goblin, ogre)
                else:
                    print("Invalid attack choice.")
                    continue
                if ogre.ogre_health <= 0:
                    flame.exp += 700
                    flame.health = health
                    print('Ogre has been defeated!')
                    print('You have never seen nor fought this monster before.\nWhat an amazing sight it is to see one dead before your very eyes!')
                    return
                ogre.ogre_attacks_flame(flame)
                if flame.health <= 0:
                    flame.health = health
                    print('Flame has been defeated!')
                    print('You are determined to treat Flame better after this dream ends.')
                    return
                print(f'Flame health: {flame.health}')

        else: # if choice = onyx
            health = onyx.health
            print('You have encountered Ogre!\nThe battle begins!\n')
            ogre.ogres_health()
            while ogre.ogre_health > 0:
                familiar_action = input('\nAttack: Normal Attack (a) / Skill Attack (s) \n').lower()
                if familiar_action == 'a':
                    onyx.onyx_attack(goblin, ogre)
                elif familiar_action == 's':
                    onyx.onyx_onyx_blast(goblin, ogre)
                else:
                    print("Invalid attack choice.")
                    continue
                if ogre.ogre_health <= 0:
                    onyx.exp += 700
                    onyx.health = health
                    print('Ogre has been defeated!')
                    print('You have never seen nor fought this monster before.\nWhat an amazing sight it is to see one dead before your very eyes!')
                    return
                ogre.ogre_attacks_onyx(onyx)
                if onyx.health <= 0:
                    onyx.health = health
                    print('Onyx has been defeated!')
                    print('Onyx had always seemed so strong in your eyes.\nYou decide to give it a treat after the dream ends.')
                    return
                print(f'Onyx health: {onyx.health}')

    # What actually puts everything together
    print('• RULES •\nYou may choose a familiar and switch them throughout this adventure.\nType your action in the terminal to manuever through fighting and leveling up.\nOnce you get to level 1, you have the option to fight a higher level monster.')
    while True:
        flame.status()
        onyx.status()
        familiar_choice = input(f'Choose your familiar:\nFlame - fire type wolf\nOnyx - rock type dragon\n??? - ????? ???? ?????\n').capitalize()

        # Flame
        while familiar_choice == 'Flame': 
            your_action = input('\n--Action--\n(status, fight, level up, leave)\n').lower()
            if your_action == 'status':
                flame.status()
            elif your_action == 'fight':
                fight_who = input('Do you want to fight Goblin or Ogre? ').lower()
                if fight_who == 'ogre':
                    if flame.level < 1:
                        print('Flame\'s level is not high enough.')
                    else:
                        fighting_ogre(flame, onyx)
                elif fight_who == 'goblin':
                    fighting_goblin(flame, onyx)
                else:
                    print('Invalid input.')
            elif your_action == 'level up':
                flame.level_up()
                flame.status()
            elif your_action == 'leave':
                break
            else:
                print('Invalid input, try again.')

        # Onyx
        while familiar_choice == 'Onyx':
            your_action = input('\n--Action--\n(status, fight, level up, leave)\n').lower()
            if your_action == 'status':
                onyx.status()
            elif your_action == 'fight':
                fight_who = input('Do you want to fight Goblin or Ogre? ').lower()
                if fight_who == 'ogre':
                    if onyx.level < 1:
                        print('Onyx\'s level is not high enough.')
                    else:
                        fighting_ogre(flame, onyx)
                elif fight_who == 'goblin':
                    fighting_goblin(flame, onyx)
                else:
                    print('Invalid input.')
            elif your_action == 'level up':
                onyx.level_up()
                onyx.status()
            elif your_action == 'leave':
                break
            else:
                print('Invalid input, try again.')
        
        # ???
        while familiar_choice == '???':
            print('\n??? used to be one of Isla\'s familiars. Isla has been looking for ??? ever since its sudden disappearance 2 years ago.\nIsla seemed to have mentioned to you once before that it was a fairy.')
            your_action = input('\n--Action--\n(status, leave)\n').lower()
            if your_action == 'status':
                print('\n• ??? • ')
                print('--Status--\nLevel: ???\nExp: ???\n'
                    f'Health: ???\nAttack: ???\nSkills: ???\n')
                print('Everything about this familiar is mysterious. You have no information about this familiar.')
                break
            elif your_action == 'leave':
                break
            else:
                print('Invalid input, try again.')

        # Asks player if they want to continue or leave
        action = input('Do you wish to continue this dream(y/n)? ').lower()
        if action == 'y':
            continue
        elif action == 'n':
            print('You have left the dream world.')
            break
        else:
            print('I\'m sorry, what did you say?')
            action = input('Do you wish to continue this dream(y/n)? ').lower()
            if action == 'n':
                break

    print('\n\n • Isla\'s Ending • \nYou awaken from your everlasting dream and hurry towards the mirror.'\
          "\nYou look at yourself through the mirror and find a gleam in your eyes. You find Isla's adventures stirring your soul, exhilarating."\
          "\nYou walk out of your house and greet Isla at the Adventurer's Guild Hall."\
          "\n'Wow! Fancy meeting you here! What adventure do you wish to embark on today?'" \
          "\n'Oh, not going on one I see.'"\
          "\n'You're here to find me and my familiars?'"\
          "\n'My goodness, what exquisite treats you have for them!'"\
          "\n'Your gifts are much appreciated! When I come back from my adventure, I shall bring you something interesting.'"\
          "\n'You wish to know? Mmm...well that's a secret!")