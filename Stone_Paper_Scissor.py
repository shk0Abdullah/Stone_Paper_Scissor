# -->  '''stone paper scissor game Two Mode GAME''' <--
import sys
print('Enter 0 to exit')
mode = input('''Chose the Mode to Start the Game \n1.Comp mode \n2.Player Mode\n''').replace(' ','')
if mode == '0':
    sys.exit()
if mode.lower() == 'compmode' or mode == '1':
    #Getting User Name()
    name = input('Enter Your Name\n')
    if name == '0':
        sys.exit()
    import random
    while True:
        comp = ''#--> defining comp
        # who wins
        def game(comp, player):
            if comp == player:
                return print("--Tie-- , Play Again!")
            else:
                if comp == "s":
                    if player == 'p':
                        return print("YOU--Won!--the GAME ")
                    else:
                        return  print('You--Lose!--') 
                if comp == "sc":
                    if player == 's':
                        return print("YOU--Won!--the GAME ")
                    else:
                        return  print('You--Lose!--') 
                if comp == "p":
                    if player == 'sc':
                        return print("YOU--Won!--the GAME ")
                    else:
                        return  print('You--Lose!--')   
        # player input
        player = input(f"---{name}'s Turns---\nstone(s)\npaper(p)\nscissor(sc)\n")
        if player == '0':
            sys.exit()
        # capitalize short form
        def nae1(nam):
            dic = { 'sc' :'Scissor',
            's':'Stone',
            'p':'Paper'
            }
            print(dic.get(nam, 'Invalid choice'))
        '''if nam == 'sc':
                print('Scissor')
            elif nam =='s':
                print('Stone')
            elif nam == 'p' :
                print('Paper')'''
        # use of randint
        randno = random.randint(1,3)
        # conversion of random 1 to 3 numbers to 's','p','sc'

        if randno == 1: 
            comp = 's'
        elif randno == 2:
            comp = 'p'
        else:
            comp = 'sc' 

        # showing Decisions
        print(f'''YOU CHOOSE: ''', end ='')
        end = nae1(player)
        print ('COMP CHOOSE: ', end= '')
        end= nae1(comp)
        # game call function
        game(comp , player) 

    # ---> PLAYER MODE

elif mode == '2' or mode.title() == 'Playermode':
     # stone paper scissor game --> Player Mode
    name1 = input('Enter the name of the First Player\n')
    name2 = input('Enter the name of the Second Player\n')
    # who wins
    def game(player1, player2):
        if player1 == player2:
            return print("--Tie-- , Play Again!")
        else:
            if player1 == "s":
                if player2 == 'p':
                    return print(f"{name2}--Wins!-- ")
                else:
                    return  print(f'{name1}--Lose!--') 
            if player1 == "sc":
                if player2 == 's':
                    return print(f"{name2}--Wins!-- ")
                else:
                    return  print(f'{name1}--Lose!--') 
            if player1 == "p":
                if player2 == 'sc':
                    return print(f"{name2}--Wins!-- ")
                else:
                    return  print(f'{name1}--Lose!--')   
    # player1 input
    while True:
            player1 = input(f"\n---{name1}'s Turns----\nstone(s)\npaper(p)\nscissor(sc)\n")
            if player1 == '0':
                sys.exit()
            # player2 input
            player2 = input(f"\n---{name2}'s Turns---\nstone(s)\npaper(p)\nscissor(sc)\n")
            if player2 == '0':
                sys.exit()
            # capitalize short form
            def name(nam):
                dic = { 'sc' :'Scissor',
                's':'Stone',
                'p':'Paper'
                    }
                print(dic.get(nam, 'Invalid choice'))
            '''if nam == 'sc':
                    print('Scissor')
                elif nam =='s':
                    print('Stone')
                elif nam == 'p' :
                    print('Paper')'''


        

            # showing Decisions
            print(f'{name1} CHOOSE: ', end ='')
            end = name(player1)
            print (f'{name2} CHOOSE: ', end= '')
            end= name(player2)
            # game call function
            game(player1 , player2)