import os


def clear():
    os.system('cls')


clear()

print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   |
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\@@@/.-'    __/ \__ |
              |==== .'.'^'.'.====|
     TREASURE |  _\o/   __  {.' __  '.} _   _\o/  _|
     LOCKED   `""""-""""""""""""""""""""""""""-""""`

''')

print('''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___       __ _  __ _ _ __ ___   ___
| __| '__/ _ \/ _` / __| | | | '__/ _ \_   / _` |/ _` | '_ ` _ \ / _ \-
| |_| | |  __/ (_| \__ \ |_| | | |  __/   | (_| | (_| | | | | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|    \__, | \__,_|_| |_| |_|\___|
                                            __/ | 
                                           |___/ 
 ''')

print(' "WELCOME TO TREASURE ISLAND" ')
print(' "YOUR MISSION IS TO FIND THE TREASURE" \n')
print('"YOU NEED TO ANSWER 12 RIDDLES TO GET THE TREASURE BOX "\n\n')

choice1 = input(" Soft and plump, I’ll be right here. Throughout your dreams, you’ll keep me near. "
                "I’ll keep you comfy all through the night, and you’ll leave me here in the morning light. \n").lower()

if choice1 == "pillow":
    print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
    choice2 = input("People climb me, cut me and burn me, they show me no respect! My rings are not of gold, "
                    "but they do tell my age? \n").lower()

    if choice2 == "tree":
        print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
        choice3 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait '
                        'for a boat. Type "swim" to swim across. \n').lower()

        if choice3 == "wait":
            choice4 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                            "One red, one blue and one white. Which colour do you choose? \n").lower()

            if choice4 == "red":
                print("It's a room full of fire. Game Over.")
            elif choice4 == "blue":
                print("You are very near to find the treasure. Give answers of few more riddles. ")
                choice5 = input(" I’m never wicked, but I do have a wick. I come in all sizes, "
                                "from skinny to thick. \n").lower()

                if choice5 == "candle":
                    print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
                    choice6 = input(" I’m a bird but I can’t fly? \n").lower()

                    if choice6 == "penguin":
                        print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
                        choice7 = input("Look at me and you’ll see a familiar sight,you can’t beat my movements, "
                                        "try as you might. \n").lower()

                        if choice7 == "mirror":
                            print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
                            choice8 = input(" Now you’re getting close to land You need your pirate ship to stop "
                                            "So you’ll take down all your sails And this object in the water "
                                            "you’ll drop \n").lower()

                            if choice8 == "anchor":
                                print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
                                choice9 = input(" Most every day, you step on me. All I require is a bend of "
                                                "your knee. \n").lower()

                                if choice9 == "stairs":
                                    print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
                                    choice10 = input(" When looking for buried gold. This item helps a lot. "
                                                     "As on this piece of paperIs where X marks the spot \n").lower()

                                    if choice10 == "treasure map" or choice10 == "treasuremap":
                                        print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
                                        choice11 = input(" I’m so simple that I only point; "
                                                         "yet I guide people all over the world? \n").lower()
                                        if choice11 == "compass":
                                            print(" CORRECT ANSWER !! HERE IS YOUR NEXT RIDDLE... \n")
                                            choice12 = input(" Fluttering, flying and flitting so free, "
                                                             "from flower to flower is where you’ll find me? \n").lower()
                                            if choice12 == "butterfly":
                                                print(" CORRECT ANSWER !! \n")
                                                print("YOU FOUND THE TREASURE. YOU WIN !! ")

                                                print(''' 
                                                88                                                88              
                                                88                                                ""      
                                                88                                                       
                                                88,dPPYba,   ,adPPYba, 8b,dPPYba,  ,adPPYba,      88 ,adPPYba       8b       d8  ,adPPYba,  88       88 8b,dPPYba
                                                88P'    "8a a8P_____88 88P'   "Y8 a8P_____88      88 I8[    ""      `8b     d8' a8"     "8a 88       88 88P'   "Y8 
                                                88       88 8PP""""""" 88         8PP"""""""      88  `"Y8ba,        `8b   d8'  8b       d8 88       88 88
                                                88       88 "8b,   ,aa 88         "8b,   ,aa      88 aa    ]8I        `8b,d8'   "8a,   ,a8" "8a,   ,a88 88
                                                88       88  `"Ybbd8"' 88          `"Ybbd8"'      88 `"YbbdP"'          Y88'     `"YbbdP"'   `"YbbdP'Y8 88 
                                                                                                                       d8'
                                                                                                                      d8' 

                                                 ''')
                                                print('''

                                                                                                                                          88
                                                  ,d                                                                                      88 
                                                  88                                                                                      88
                                                MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba       88,dPPYba,   ,adPPYba, 8b,     ,d8
                                                  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8 a8P_____88      88P'    "8a a8"     "8a `Y8, ,8P'
                                                  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88         8PP"""""""      88       d8 8b       d8   )888(
                                                  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa      88b,   ,a8" "8a,   ,a8" ,d8" "8b, 
                                                  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          `"Ybbd8"'      8Y"Ybbd8"'   `"YbbdP"' 8P'     `Y8 


                                                ''')
                                                print(''''*******************************************************************************
                                                          |                   |                  |                     |
                                                 _________|________________.=""_;=.______________|_____________________|_______   
                                                |                   |  ,-"_,=""     `"=.|                  |                      
                                                |___________________|__"=._o`"-._        `"=.______________|___________________   
                                                          |                `"=._o`"=._      _`"=._                     |          T
                                                 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______   R
                                                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |                      E     U
                                                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________   A     N
                                                          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |          S     L
                                                 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______   U     O
                                                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |                      R     C
                                                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________   E     K
                                                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____         E
                                                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_         D
                                                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____   
                                                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_   
                                                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____   
                                                /______/______/______/______/______/______/______/______/______/______/______/_   
                                                *******************************************************************************''')

                                            else:
                                                print("WRONG ANSWER !! YOU WAS BEHIND THE TREASURE DOOR. "
                                                      "GAME OVER.... \n")
                                                print('''


                                                                          /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                                                         ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                                                          \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                                                           \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                                                            \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                                                           \/|(O)(O)|                    aa,    ,88
                                                                          \/ |      |                    "Y8bbdP" 
                                                      ___________________\/  \      /
                                                     //                //     |____|
                                                    //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                                                   //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                                                  // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                                                 //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                                                ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                                                       /  /\   /     |  ||
                                                      /  / /  /      \  ||
                                                      | |  | |        | ||                               88
                                                      | |  | |        | ||                               88   
                                                      |_|  |_|        |_||                               88  
                                                       \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                                                         88P'    "8a `8b     d8' a8P_____88  
                                                                                                         88       d8  `8b   d8'  8PP"""""""
                                                                                                         88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                                                         8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                                                         d8'     
                                                                                                                        d8'  

                                                ''')

                                        else:
                                            print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
                                            print('''


                                                                      /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                                                     ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                                                      \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                                                       \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                                                        \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                                                       \/|(O)(O)|                    aa,    ,88
                                                                      \/ |      |                    "Y8bbdP" 
                                                  ___________________\/  \      /
                                                 //                //     |____|
                                                //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                                               //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                                              // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                                             //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                                            ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                                                   /  /\   /     |  ||
                                                  /  / /  /      \  ||
                                                  | |  | |        | ||                               88
                                                  | |  | |        | ||                               88   
                                                  |_|  |_|        |_||                               88  
                                                   \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                                                     88P'    "8a `8b     d8' a8P_____88  
                                                                                                     88       d8  `8b   d8'  8PP"""""""
                                                                                                     88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                                                     8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                                                     d8'     
                                                                                                                    d8'  

                                            ''')

                                    else:
                                        print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
                                        print('''


                                                                  /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                                                 ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                                                  \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                                                   \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                                                    \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                                                   \/|(O)(O)|                    aa,    ,88
                                                                  \/ |      |                    "Y8bbdP" 
                                              ___________________\/  \      /
                                             //                //     |____|
                                            //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                                           //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                                          // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                                         //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                                        ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                                               /  /\   /     |  ||
                                              /  / /  /      \  ||
                                              | |  | |        | ||                               88
                                              | |  | |        | ||                               88   
                                              |_|  |_|        |_||                               88  
                                               \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                                                 88P'    "8a `8b     d8' a8P_____88  
                                                                                                 88       d8  `8b   d8'  8PP"""""""
                                                                                                 88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                                                 8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                                                 d8'     
                                                                                                                d8'  

                                        ''')

                                else:
                                    print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
                                    print('''


                                                              /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                                             ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                                              \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                                               \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                                                \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                                               \/|(O)(O)|                    aa,    ,88
                                                              \/ |      |                    "Y8bbdP" 
                                          ___________________\/  \      /
                                         //                //     |____|
                                        //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                                       //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                                      // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                                     //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                                    ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                                           /  /\   /     |  ||
                                          /  / /  /      \  ||
                                          | |  | |        | ||                               88
                                          | |  | |        | ||                               88   
                                          |_|  |_|        |_||                               88  
                                           \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                                             88P'    "8a `8b     d8' a8P_____88  
                                                                                             88       d8  `8b   d8'  8PP"""""""
                                                                                             88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                                             8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                                             d8'     
                                                                                                            d8'  

                                    ''')

                            else:
                                print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
                                print('''


                                                          /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                                         ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                                          \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                                           \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                                            \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                                           \/|(O)(O)|                    aa,    ,88
                                                          \/ |      |                    "Y8bbdP" 
                                      ___________________\/  \      /
                                     //                //     |____|
                                    //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                                   //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                                  // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                                 //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                                ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                                       /  /\   /     |  ||
                                      /  / /  /      \  ||
                                      | |  | |        | ||                               88
                                      | |  | |        | ||                               88   
                                      |_|  |_|        |_||                               88  
                                       \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                                         88P'    "8a `8b     d8' a8P_____88  
                                                                                         88       d8  `8b   d8'  8PP"""""""
                                                                                         88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                                         8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                                         d8'     
                                                                                                        d8'  

                                ''')

                        else:
                            print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
                            print('''


                                                      /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                                     ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                                      \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                                       \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                                        \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                                       \/|(O)(O)|                    aa,    ,88
                                                      \/ |      |                    "Y8bbdP" 
                                  ___________________\/  \      /
                                 //                //     |____|
                                //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                               //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                              // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                             //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                            ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                                   /  /\   /     |  ||
                                  /  / /  /      \  ||
                                  | |  | |        | ||                               88
                                  | |  | |        | ||                               88   
                                  |_|  |_|        |_||                               88  
                                   \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                                     88P'    "8a `8b     d8' a8P_____88  
                                                                                     88       d8  `8b   d8'  8PP"""""""
                                                                                     88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                                     8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                                     d8'     
                                                                                                    d8'  

                            ''')

                    else:
                        print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
                        print('''


                                                  /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                                 ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                                  \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                                   \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                                    \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                                   \/|(O)(O)|                    aa,    ,88
                                                  \/ |      |                    "Y8bbdP" 
                              ___________________\/  \      /
                             //                //     |____|
                            //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                           //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                          // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                         //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                        ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                               /  /\   /     |  ||
                              /  / /  /      \  ||
                              | |  | |        | ||                               88
                              | |  | |        | ||                               88   
                              |_|  |_|        |_||                               88  
                               \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                                 88P'    "8a `8b     d8' a8P_____88  
                                                                                 88       d8  `8b   d8'  8PP"""""""
                                                                                 88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                                 8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                                 d8'     
                                                                                                d8'  

                        ''')

                else:
                    print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
                    print('''


                                              /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                             ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                              \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                               \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                                \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                               \/|(O)(O)|                    aa,    ,88
                                              \/ |      |                    "Y8bbdP" 
                          ___________________\/  \      /
                         //                //     |____|
                        //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                       //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                      // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                     //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                    ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                           /  /\   /     |  ||
                          /  / /  /      \  ||
                          | |  | |        | ||                               88
                          | |  | |        | ||                               88   
                          |_|  |_|        |_||                               88  
                           \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                             88P'    "8a `8b     d8' a8P_____88  
                                                                             88       d8  `8b   d8'  8PP"""""""
                                                                             88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                             8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                             d8'     
                                                                                            d8'  

                    ''')

            elif choice4 == "white":
                print("You enter a room of beasts. Game Over. ")
                print('''


                                          /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                         ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                          \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                           \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                            \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                           \/|(O)(O)|                    aa,    ,88
                                          \/ |      |                    "Y8bbdP" 
                      ___________________\/  \      /
                     //                //     |____|
                    //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                   //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                  // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                 //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                       /  /\   /     |  ||
                      /  / /  /      \  ||
                      | |  | |        | ||                               88
                      | |  | |        | ||                               88   
                      |_|  |_|        |_||                               88  
                       \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                         88P'    "8a `8b     d8' a8P_____88  
                                                                         88       d8  `8b   d8'  8PP"""""""
                                                                         88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                         8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                         d8'     
                                                                                        d8'  

                ''')
            else:
                print("You chose a door that doesn't exist. Game Over. ")
                print('''


                                          /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                         ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                          \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                           \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                            \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                           \/|(O)(O)|                    aa,    ,88
                                          \/ |      |                    "Y8bbdP" 
                      ___________________\/  \      /
                     //                //     |____|
                    //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
                   //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
                  // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
                 //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
                ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                       /  /\   /     |  ||
                      /  / /  /      \  ||
                      | |  | |        | ||                               88
                      | |  | |        | ||                               88   
                      |_|  |_|        |_||                               88  
                       \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                         88P'    "8a `8b     d8' a8P_____88  
                                                                         88       d8  `8b   d8'  8PP"""""""
                                                                         88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                         8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                         d8'     
                                                                                        d8'  

                ''')

        else:
            print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
            print('''


                                      /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                     ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                      \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                       \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                        \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                       \/|(O)(O)|                    aa,    ,88
                                      \/ |      |                    "Y8bbdP" 
                  ___________________\/  \      /
                 //                //     |____|
                //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
               //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
              // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
             //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
            ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
                   /  /\   /     |  ||
                  /  / /  /      \  ||
                  | |  | |        | ||                               88
                  | |  | |        | ||                               88   
                  |_|  |_|        |_||                               88  
                   \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                     88P'    "8a `8b     d8' a8P_____88  
                                                                     88       d8  `8b   d8'  8PP"""""""
                                                                     88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                     8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                     d8'     
                                                                                    d8'  

            ''')

    else:
        print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")
        print('''


                                  /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                                 ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                                  \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                                   \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                                    \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                                   \/|(O)(O)|                    aa,    ,88
                                  \/ |      |                    "Y8bbdP" 
              ___________________\/  \      /
             //                //     |____|
            //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
           //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
          // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
         //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
        ""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
               /  /\   /     |  ||
              /  / /  /      \  ||
              | |  | |        | ||                               88
              | |  | |        | ||                               88   
              |_|  |_|        |_||                               88  
               \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                                 88P'    "8a `8b     d8' a8P_____88  
                                                                 88       d8  `8b   d8'  8PP"""""""
                                                                 88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                                 8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                                 d8'     
                                                                                d8'  

        ''')

else:
    print("WRONG ANSWER !! YOU CAN'T GO TO THE NEXT RIDDLE. GAME OVER.... \n")

    print('''


                          /_\          /_\_              ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 
                         ( \_\        // )              a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88
                          \ \_\      // /               8b       88 ,adPPPPP88 88      88      88 8PP"""""""
                           \_\_\||||//_/                "8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 
                            \/ _  _ \_                   `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 
                           \/|(O)(O)|                    aa,    ,88
                          \/ |      |                    "Y8bbdP" 
      ___________________\/  \      /
     //                //     |____|
    //                ||     /      \_                    ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
   //|                \|     \ 0  0 /                    a8"     "8a `8b     d8' a8P_____88 88P'   "Y8 
  // \       )         V    / \____/                     8b       d8  `8b   d8'  8PP""""""" 88          
 //   \     /        (     /                             "8a,   ,a8"   `8b,d8'   "8b,   ,aa 88          
""     \   /_________|  |_/                               `"YbbdP"'      "8"      `"Ybbd8"' 88          
       /  /\   /     |  ||
      /  / /  /      \  ||
      | |  | |        | ||                               88
      | |  | |        | ||                               88   
      |_|  |_|        |_||                               88  
       \_\  \_\        \_\_\                             88,dPPYba,  8b       d8 ,adPPYba,
                                                         88P'    "8a `8b     d8' a8P_____88  
                                                         88       d8  `8b   d8'  8PP"""""""
                                                         88b,   ,a8"   `8b,d8'   "8b,   ,aa  
                                                         8Y"Ybbd8"'      Y88'    `"Ybbd8"'
                                                                         d8'     
                                                                        d8'  

''')
