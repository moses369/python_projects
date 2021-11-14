import time

def start_game():
  play = input('Do you want to play "To The Mountain"? \n(1) Yes \n(2) No \n ')
  
  if play.strip() == '2':
    print('Thank you for considering!')
    exit()
  elif play.strip() == '1':
    print('Welcome to "To The Mountain", You make decisions by typing the corresponding key. Each decision will have a different outcome. ')
  else:
    print('Please enter 1, or 2')
    exit()

def delay(num):
  time.sleep(num)

def death(num):
  delay(num)
  exit()

def cave():
  print('''\
  You climb the steep cliff-side, grabbing onto black jagged stones. 50ft off the ground and you climb up onto a ledge. Finally able to catch a rest, you notice a giant cave in front of you. Looking above the walls of the mountain are to sleek to climb, you enter the cave with no ther option. You smell rotting flesh and notice bones on the floor. You eventually see a light up ahead with three dancing shadows. Sneakily you see the short green goblins, dressed in ragged hides, each holding a weapon. One has a short sword, the second a spear, the third a club.Stories are told of goblins raiding villages at night kidnapping children and women, you feel your heart thumping through your chest, sweat pouring down your face. You know the only way is forward, you notice a deep shadow along the edges of the wall you can sneak across with. \nDo sneak across in the shadows, or face the goblins with your sword?
  ''')
  delay(2)
  cave1 = input('(1) to sneak \n(2) to face them with your sword   \n')
  
  if cave1.strip() == '1':
    print('''\
      \nYou make your way across the shadows, feeling your heart race through your chest, the goblins to entertained within themselves to notice. You make it across you breathe a sense of relief, but know its not over yet. As you make your way deeper into the cave you notice a giant cavern up ahaed. Inside you hear two thunderous voices speaking a language you don't understand. Gazing into the darkness you see two giant ogres, each 15ft tall, grey and muscular, torches in hand, flesh hanging from their teeth, bones litter the ground. What that flesh belongs to you wish to never know, you sweat profusely, fearful for your life. Your chest sinking into the gorund, yet their is only one way to go now. They stand near the only way across, you think you might be able to sneak around the edge, or face them head on. 
      ''')
    delay(2)
    cave1_sneak = input('(1) to sneak \n(2) to face your foe \n')
    
    if cave1_sneak.strip() == '1': #Player Dies
      print('\nAs you make your way across, hugging the walls of the dark cave. Guided by the light of these monsters before you. The closer you get to them, the faster your heart races. Almost there you tell your self, but then *CRACK*. You freeze, your skin turns pale, your heart feels as if it exploded in your chest, your body shaking uncontrollably. The crack of rib, rings loud in the cavern, breaking the silence in the cave. The ogres turn their head towards you, eyes adjusted to the darkness, they match your gaze. The closest one reaches for you faster then you can blink. You pull out your sword holding it as hard as ever, but unable to stop shaking, it slides across it\'s mighty hand. Darkness ensues and you are no longer shaking..... ')
      death(3)
      
    elif cave1_sneak.strip() == '2':#Player Dies
      print('\nYou steady your nerves for battle, gaining control of your breath, calming your anxiety. You walk slowly towards your enemy. The ogres stop talking, looking into the path your trying to get to. You take this oppurtunity and with all your might slice into it\'s achilles. He screeches in pain, the cut was too shallow and he does not fall. Both turn towards you, the one you sliced moves faster than you thought. You feel as though you\'ve been run over by a bull, and fly across the cavern. Your back slams against the cold rough wall and your head whiplashes against the rock. You fall slumpt, dizzy and barely concious you hear their steps walking towards you and then silence......')
      death(3)
      
  elif cave1.strip() == '2':#Player Dies
      print('\nYou steady your nerves and grip your sword tight. Running as fast as you can, you impale the goblin with the spear. The other two goblins, taken by suprise hesitate to strike back. Attempting to take advantage you pull on your sword, yet it does not budge on the first go, you take your foot and kick the goblin off of your sword. Losing  your oppurtunity you turn and face the goblins, to only find the one with club before you. He swings his club, eyes wide with hunger, snarling like an animal. You move out of the way, and as you swing your about to swing your sword down onto his head, you feel a sharp pain through your stomach. Blood fills your mouth, looking down you see a sword portruding out of your stomach. The club goblin, regains his footing and swings again aiming for your head. Everything goes dark.....')
      death(3)

  else:
    print('Please enter 1, or 2')
    delay(2)
    cave()

def harpy_encounter():
  print('''\
    \nYou make your way towards the melody becoming ever so entranced by it's beauty. You find yourself staring at a harpy singing into the wind. It's giant snake like eyes stare into your soul, and it stands up, standing 4ft tall. It's wings span 10ft across, the body of a human with grey skin,feet of an eagle claw,a face with no nose,a mouth filled with razor shapr teeth, fingers replaced with long razor sharped claws. It flies into the air and glides towards you with its legs ready to pick you up in the air. You draw your sword, sweating, anxious and scared, you swing your sword as the harpy flies into your reacha and you cut into one of its legs.However, the other leg is able to slice your arm, leaving three deep claw marks. The harpy, unable to use it's cut leg, decides to fly away avoiding any more injuries. You stand their blood flowing down your, arm. You feel some sense of pride in survivingthe encounter, however unable to use your injured arm, you wrap it in bandages and continue your journey.
    ''')

def goblin_path_encounter(message):
  
  print('''\
  \nMaking your way up the mountain,the path becomes more narrow. with rocks on one side and a long fall on the other, you near the top of the mountain. You hear goblins making their way down,with an injured arm you prepare yourself for battle.Stories are told of goblins raiding villages at night kidnapping children and women, you feel your heart thumping through your chest, sweat pouring down your face. There is no where to run.Two goblins turn the corner, one with a sword and shield, the other a spear. ''' + message)

def starting_up_the_mountain(num):
  print('''\
    \nFinally you come across a path leading to the top of the mountain. You make your way up the mountain, as you ascend the air becomes thinner. You look back and the view is astonishing, seeing into the vast world for miles, you never knew it could look so beautiful. You continue up the mountain and begin to hear a melody, you spot a backpack sitting on the ground. It must be another traveler, they sing beautifully, you've never heard such a beautiful song before.
    ''') 
  delay(2)
  investigate_or_keep_walking = input('(1) You investigate the melody. \n(2) You ignore it and keep going \n')
  
  if investigate_or_keep_walking.strip() == '1': #Investigates the Melody
    harpy_encounter()
    
    # Ate Berries Path
    
    if num == 1: #Player dies
      goblin_path_encounter('The smell of your blood drives them mad and they charge you. The sword/shield goblin lunges towards you swinging his sword down to your head, you deflect the blow and kick his raised shield sending him falling down the cliff. Causing your stomach to cramp harder than ever forcing your body to instictvely bend over you prop yourself up from falling with your sword.When you look up towards the second goblin his spear already inches from your eyes, everything goes black....')
      death(3)

    # Did Not Eat The Berries
    elif num == 2:#Player Dies
      goblin_path_encounter('''The smell of your blood drives them mad and they charge you. The sword/shield goblin lunges towards you swinging his sword down to your head, you deflect the blow and kick his raised shield sending him falling down the cliff.The other goblin's spear already inches to your belly, unable to deflect it with your other arm, you swing down striking him in his shoulder, feeling his spear enter your belly.Both you and the goblin stumble from the pain. The goblin still alive,, the cut was too shallow, gets up and jumps towards you. You lay flat on your back pointing your sword towards him.The goblin impales himself on your sword, his teeth just inches from your face,he spits blood onto your face. Unable to throw him off of you, his limp body pins you to the ground. With massive amounts of blood pooling below your body, your eyes grow heavy, slowly you fall asleep....''')
    death(3)
  # Did Not investigate
  elif investigate_or_keep_walking.strip() == '2':
    #Ate Berries
    if num == 1:
      goblin_path_encounter('''Spotting you the sword/shield goblin lunges towards you swinging his sword down towards your head, you deflect the blow and kick his raised shield sending him falling down the cliff. Causing your stomach to cramp harder than ever forcing your body to instictvely bend over you prop yourself up from falling with your sword. When you look up towards the second goblin his spear already inches from your eyes, you quickly grab the spear with your other arm and barely pulling it away from your eyes, it slides across the side of your head, cutting the top half of your ear off. The goblin pulled along with the spear lets go, and with it's razor sharp teeth lunges to bite your neck. Letting go of the sword you quickly get your arm between you and the goblin. Latching on to your arm, you wince in pain, you turn over and push your arm into it's mouth pinning him down. You quickly grab the sword with your other arm, as the goblin bites down harder unable to move under your weight. You impale the goblins heart, and it lets go of your arm.Your arm bleeding, half of yout ear gone, and blood running down the back of your head. You bandage what you can. ''')
    
    #Did not eat berries
    elif num == 2:
      goblin_path_encounter('''The sword/shield goblin lunges towards you swinging his sword down to your head, you deflect the blow and kick his raised shield sending him falling down the cliff.The other goblin's spear already inches to your belly, you use your free hand and push it away from your center. It glances only cutting the side of your ribs, you swing your sword hand down and slice into the goblins shoulder. It falls in pain, still alive from the shallow cut. The goblin snarls at you, you drive your sword into it's neck ending it for good.''')
  else:
    print('Please enter 1, or 2')
    delay(2)
    starting_up_the_mountain()

def walk_around_the_mountain():
  print('''\nYou walk across the base of the mountain through the forest. An hour passes by and you become hungry, you notice some blue berries growing on a bush, and think they look like the berries mother would gather for jam. The thought of your mother's bread and berry jam makes you mouth water. \nDo you eat the berries,or keep going and only have bread?   
  ''')
  delay(2)
  berries_or_walk = input('(1) eat berries \n(2)keep going  \n')

  if berries_or_walk.strip() == '1':
    print('\nYou eat some bread and berries, the flavor is delicous. You continue down the side of the mountain, but your stomach starts to cramp, as though youve been stabbed witha knife. You vomit, yet the pain still lingers...')
    delay(2)
    starting_up_the_mountain(1)
  
  elif berries_or_walk.strip() =='2':
    delay(1)
    starting_up_the_mountain(2)
  
  else:
    print('Please enter 1, or 2')
    delay(1)
    walk_around_the_mountain()

def intro():
  print('''\
  \nYour family is gravely ill. The oldest child of 4, it is up to you to save them. The only way you can save them is by climbing to the top of the mountain. Few have ever come back down, and those who do know not what lies at the top. The path is filled with inhuman dangers, yet you must make it to the top. You begin your travels bringing a sword,and some bread for the journey. As you reach the base of the mountain closest to the village, you examine the steep wallsy jagged with rocks sharp as knives, you think to yourself,"I may be able to climb this". \n Do you climb the walls, hoping to shorten your journey, or do you travel along the base in hopes of finding an easier path?     
  ''')
  delay(2)
  climb_or_walk = input('(1) Climb the mountain \n(2) Walk around the mountain \n')

  if climb_or_walk.strip() == '1':
    cave()

  elif climb_or_walk.strip() == '2':
    walk_around_the_mountain()

  else: 
    print('Please enter 1, or 2')
    delay(2)
    intro()

def end_game():
  delay(7)
  print('''\
    \nSlowly making your way to the top of the mountain.As you see the top in sight the wind is blowing hard, you have to use your sword to help you walk across. You finally make it to the top and the wind stops. You can not believe your eyes. A behemoth of old, that stories say to be the most wise and ancient creatures of all, a dragon. Towering over the largest of trees, wider than the longest of buildings, scales harder iron itself.As you hear your heart thump through your chest,its eyes open.Eyes as deep as the sea itself, stare into your soul, you dare not match it's gaze. The dragon stands up, the wind from it's movements knocking onto the ground. It asks, "Who are you, and why have you come?". You tell the dragon of your family, and how you have come for the dragonflower.The dragon looks into your soul and then asks, "I will let you take this flower, however you may also have this (he grabs a rare diamond, one worth over 500 million coins.),but whichever you choose you may not have the other,this flower is only located with other dragons and so you may never get another chance to find one, if you take the gem. So what will it be {}, take the gem and become the richest human in the lands and desert your family, or save them?"
  '''.format(NAME))
  delay(4)
  save_or_greed = input('(1)take the gem \n(2)save your family \n')
  if save_or_greed.strip() == '1':
    print('''\
      \nThe dragon hands you the gem, "Here you go {}, your greed has led to the death of you family. We will see how happy you live when you're riches mean nothing." Confused by the what the dragon said, you make your way down the moutain, knowing you will now be the richest in the world. However, as you look across the horizon a gust of wind knocks you to the ground, and the dragon flies overhead. Burning your home, and all of the villages, cities in the kingdom to the ground. You now understood what the dragon meant by his words...'''.format(NAME))
  elif save_or_greed.strip() == '2':
    print('''\
    \nThe dragon looks into your eyes, "Come and grab the flower, save your family, I respect your integrity and commitment.However you will not remember this encounter {}." The dragon allows you to pass and grab the flower, he stops any fatal bleeding and heals any internal wounds with his magic, and erases your memory of him. You walk down towards your home with the dragonflower in hand, finally able to save your family...
    '''.format(NAME))
  else:
    print('Please enter 1, or 2')
    delay(2)
    end_game()





start_game()

delay(3)
NAME = input("What is your character's name?   ")
delay(1)
intro()
end_game()
