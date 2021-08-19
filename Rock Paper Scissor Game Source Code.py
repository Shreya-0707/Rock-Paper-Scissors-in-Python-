import random

comp_wins=0
player_wins=0

def choose_opt():                                  #player choice
    user_choice=input('choose rock..paper..or..scissor : ')
    if user_choice in ['rock','Rock','R','r']:
        user_choice='r'
    elif user_choice in ['paper','Paper','P','p']:
        user_choice='p'
    elif user_choice in ['scissor','Scissor','S','s']:
        user_choice='s'
    else:
        print('invalid choice!!')
        choose_opt()
    return user_choice

def comp_opt():                                  #computer choice
    comp_choice=int(random.randint(1,3))
    if comp_choice==1:
        comp_choice='r'                         #1 : rock
    elif comp_choice==2:
        comp_choice='p'                         #2: paper
    else:
         comp_choice='s'                         #3 : scissor
    #print(comp_choice)
    return comp_choice


while True:
    
    user_choice=choose_opt()
    comp_choice=comp_opt()
    
    if user_choice=='r':
        if comp_choice=='r':
            print('you chose rock..computer choose rock.. its a tie!! ')
        elif comp_choice=='p':
            print('you chose rock..computer choose paper.. you lose!!')
            comp_wins+=1
        elif comp_choice=='s':
            print('you chose rock..computer choose scissor.. you win!!')
            player_wins+=1
            
    elif  user_choice=='p':
        if comp_choice=='r':
            print('you chose paper..computer choose rock.. you win!! ')
            player_wins+=1
        elif comp_choice=='p':
            print('you chose paper..computer chose paper..its a tie!!')
        elif comp_choice =='s':
            print('you chose paper..computer chose scissor..you lose!!')
            comp_wins+=1
        
    elif user_choice=='s':
        if comp_choice=='r':
            print('you chose scissor..computer choose rock.. you lose!! ')

            comp_wins+=1
        elif comp_choice=='p':
            print('you chose scissor...computer choose paper.. you win!!')
            player_wins+=1
        elif comp_choice=='s':
            print('you chose scissor..computer choose scissor.. its a tie!!')


    print(" ")
    print("player wins: "+str(player_wins))
    print("computer wins :"+str(comp_wins))
    print(" ")

    user=input('do you want to play again?(y/n) : ')
    if user=='y':
        pass
    elif user=='n':
        
        break
    else:
        break   
   
