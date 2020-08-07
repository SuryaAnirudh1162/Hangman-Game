#Hangman_Game




import random
import string




#Name_of_Player
print("Enter Your Name : ")
Name = input()
print(" The Hangman Game Welcomes You "+Name)
print(" Here is your word and try to guess within 7 Chances ")
print(" We wish you to win ")
print()




#Making_A_List_of_Words_&_Letters
List_of_Words = ['BoJack Horseman','Stranger Things','Orange is the New Black','American Vandal',
                            'Mindhunter','Russian Doll','Money Heist']
Chances = 7
Letters = string.ascii_letters
List_of_Letters = list(Letters)




#Selecting_A_Random_Word
Secret_Word = random.choice(List_of_Words)
Length_of_Secret_Word = len(Secret_Word)
List_Secret_Word = list(Secret_Word)




#Printing_Dashes
Players_List = []
Length_To_Check = 0
for i in range(Length_of_Secret_Word):
    if  List_Secret_Word[i] in List_of_Letters :
        print('_ ',end="")
        Length_To_Check+=1
        Players_List.append('_ ')
    else:
        Players_List.append('    ')
        print('    ',end="")
print()




#Players_Starts_His_Game
while(True):

    if Chances>0 and Length_To_Check == 0:
        print("Hurray !! You have Won !!")
        break

    print("Enter your Letter : ")
    Player_input = input()
    if len(Player_input)==0:
        print("Please enter a letter")
        continue
    elif len(Player_input)>=2:
        print("Please enter only one letter")
        continue

    if Player_input in List_Secret_Word:
        for i in range(Length_of_Secret_Word):
            if List_Secret_Word[i] == Player_input :
                Players_List[i]=Player_input
                Length_To_Check-=1
    else:
        Chances-=1
        if Chances<=0:
            print()
            print("Sorry, you have lost the game. TRY AGAIN ")
            print("The Answer is "+Secret_Word)
            break
        print(" Try Again and there are only "+str(Chances)+" chances ")

    s=''
    print(s.join(Players_List))
    
    print()
    
