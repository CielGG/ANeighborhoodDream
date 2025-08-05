from capstone_math import cap_math
from riddle import riddle
from rpg import rpg
from haggling import haggling
from potion import potion

# intro cutscene
print("\nAfter a long tiring day, you slump onto your bed. Ready to go to sleep.\
\nAs you lay down, tucked into your blanket. \nYou begin to dream..\
\nof your neighbors?" \
"\n\nThere they stand, your neighbors:" \
"\n\n • Esmerelda, an elf Wizard who enjoys talking about her old life as an adventurer with you. She treats you like her own kid and doesn't look a day over 20. Even as the ripe age of 1,253." \
"\n\n • Willow, a snake Merchant, who acts too friendly, almost like they have an alterior motive. You've caught them stashing a glowing creature into a bag one time.." \
"\n\n • Cairo, a fox Mercenary, known for their versatile skill set and frivolous personality. They enjoy asking tricky questions or riddles, acting as if they know more than they lead on." \
"\n\n • Isla, a human Adventurer, a strong women who enjoys exploring new places with her strange, but cute pets. You heard one of her fairies went missing recently. " \
"She's asked you, on occassion, to look after some of them while she's off on an adventure. You don't know what she really does on these trips.." \
"\n\n • Lupin, a dwarf Professor, he's a hot tempered old man that almost never goes out due to constantly being overworked. Is either at home doing work or at work. " \
"Once, he slept for an entire day. You haven't gotten the chance to interact with him due to his busy schedule, but Esmerelda has told you about him.")

def main():
    while True:
        character_choice = input("\nWho's life would you like to take a peek at? ").capitalize()
        if character_choice == "Esmerelda":
            potion()
        elif character_choice == "Willow":
            haggling()
        elif character_choice == "Cairo":
            riddle()
        elif character_choice == "Isla":
            rpg()
        elif character_choice == "Lupin":
            cap_math()

main()



# # Esmerelda
# print("\nCutscene:\
#     \nYou awaken from your everlasting dream, that felt so scarily real." \
#     "\nYou never knew the life your mysterious neighbor led. This experience has given you a new appreciation for Esmerelda and all her wisdom." \
#     "\nFeeling empowered by your vivid dream, you step outside and head straight for the elf's humble potion shop." \
#     "\n'Oh! What an unexpected face! Darling, what brings you here?'" \
#     "\n'Hm..You just wanted to talk? Interesting, well, what did you want to talk about sweetie?'" \
#     "\nAfter talking with your dear friend, you two have never been closer." \
#     "\nYou've always wanted to become closer with her, but could never find the right words." \
#     "\nAfter your dream, there are too many words to say.")

# # Esmerelda Secret Potion
# print("\n'Why hello there, darling.'" \
#       "\n'Did you enjoy living my life? How did you like potionmaking?'"\
#       "\n'Oh, don't try to talk, you're teeth will fall out orrr you'll drown in your consiousness.'" \
#       "\n'If you took a liking to the brewing of magic. You can become my darling apprentice. Once you've woken, of course. Come and visit me at my shop.'" \
#       "\n\n'Ah, one more thing, be careful of that snake. Believe me when I say that they are not to be trusted, okay?'")

# # Lupin
# print("You: Phew, all done grading these tests. That was harder than I expected. I am feeling a little tired. A quick nap wouldn’t hurt...\n"\
#     "\nYou wake up from your everlasting dream to a new morning away from those horrid numbers. You gain a new understandinding of Lupin's hectic worklife." \
#     "\nHaving to grade so many tests would tire anyone out. How has he managed to not go insane yet??" \
#     "\nYou begin brewing a calming chamomile tea, known for its calming and sleep aiding abilities. Nervously, you head over to Lupin's house and begin knocking."\
#     "\n'Who in the name of Odin is 'nocking this early in the morning. I ought to 'ave a word with you bumbling neighbors.'"\
#     "\n'Bloody 'ell, you youngesters these days 'ave way too much tim... Oh is that for me? 'Ow did you know I 'aven't been able to sleep. Was it the eyebags?'"\
#     "\n'For this I give you a B-, a respectable passing grade. Well, thanks for the tea neighbor, I ought to go back to sleep now before my next class starts.'")
    
# # Cairo 
# print("\n...You wake up from your everlasting dream. Feeling like a new person. You never knew your neighbor's life could be so enticing." \
#     "\nYou gain a new appreciation for your neighbor Cairo." \
#     "\nYou walk out of your house, looking for a particular fox. When you find them, you strike a conversation with them. Asking for a riddle." \
#     "\n\n'I always appear with my companion. When you're close, we seem to arrive together. But from far away, I come first, and my companion follows. What am I?'" \
#     "\n'Guess you'll have to think about it more~!'" \
#     "\n'How did you know I loved riddles? Have you been stalking me comrad~?'" \
#     "\n'Haha! Joking! Joking! I am curious though.'" \
#     "\n\nYou: 'I just had a feeling.'")

# #Isla
# print('You awaken from your everlasting dream and hurry towards the mirror.'\
#     "\nYou look at yourself through the mirror and find a gleam in your eyes. You find Isla's adventures stirring your soul, exhilarating."\
#     "\nYou walk out of your house and greet Isla at the Adventurer's Guild Hall."\
#     "\n'Wow! Fancy meeting you here! What adventure do you wish to embark on today?'" \
#     "\n'Oh, not going on one I see.'"\
#     "\n'You're here to find me and my familiars?'"\
#     "\n'My goodness, what exquisite treats you have for them!'"\
#     "\n'Your gifts are much appreciated! When I come back from my adventure, I shall bring you something interesting.'"\
#     "\n'You wish to know? Mmm...well that's a secret!")

# # Azareth
# print("\n\nAfter a long day of haggling and dealing with tiring customers. Willow closes the front door and flips the sign to closed. \nYou weren't able to fully breath in the atmosphere of the store." \
#       "The gloomy weight of the air and random belongings, that don't match at all, \nscattered around the room feel off. You can tell something grim has happened in here. You go behind the cash register, \nyou hadn't noticed the drawers next to it." \
#       "Curiously, you open the drawer, wondering what Willow could possibly be hiding." \
#       "In shock, you see random trinkets, and a plastic piece of what looks like 2 guild IDs." \
#       "On one, it says 'Willow'. On the other it says..." \
#       "\n\nAzareth? Both have the snakey face on it. The one belonging to Azareth seems older and more accurate compared to its cheaply made copy." \
#       "\n\nSo...who is Willow? Or should I say Azareth? Are either even their real name..?")