# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:42:53 2020

@author: Micky
"""
from random import choice, randint

import Performancemeasure, board, action, agent, NaiveAgent
points = Performancemeasure.s_points

def main():

    wumpus_location = choice(board.board_numbers)
    agent_location = (1,1) #start at location 1
    gold = choice(board.board_numbers) # choice random spot for gold
    pit1 = choice(board.board_numbers) # choice random spot for pit
    pit2 = choice(board.board_numbers) # choice random spot for pit
    pit3 = choice(board.board_numbers) # choice random spot for pit
    while agent_location == wumpus_location:
        agent_location = choice(board.board_numbers)
        if NaiveAgent.r == 0:
            print(action.straight)
        elif NaiveAgent.r ==1:
            print(action.left)
        elif NaiveAgent.r == 2:
            print(action.right)
        elif NaiveAgent.r == 3:
            print(action.shoot)
        elif NaiveAgent.r == 4:
            print(action.grab)  
        elif NaiveAgent.r ==5:
            print(action.climb)
    print("welcome to  wumpas world ")
    print("Created by Micky Kumar")
    print("You can see", len(board.board), "board" )
    print("To Play, just type the number")
    print("of the cave you wish to enter next")
    status_points = (points -- 1)
    while True:
        print(" you are in board", agent_location)

        print("you have:", status_points)
        #if wumpus_location in caves[agent_location]:
        if (agent_location == wumpus_location -1 or
            agent_location == wumpus_location +1 ):
            print("I received a Stench. A wumpus is close by")
        if (agent_location == pit1 -1 or
            agent_location == pit1 +1 ):
            print("I  felt a breeze pit close by")
        if (agent_location == pit2 -1 or
            agent_location == pit2 +1 ):
            print("I  felt a breeze pit close by")    
        if (agent_location == pit3 -1 or
            agent_location == pit3 +1 ):
            print("I  felt a breeze pit close by")                
        if (agent_location == gold -1 or
            agent_location == gold +1 ):
            print("gold close by") 

        print("which cave next")
        al = input(">")#randint(0,6)
        if (not al.isdigit() or int(al) not in board.board_numbers) :
            print("AL")
        else:
            agent_location = int(al)
            if agent_location == wumpus_location:
                wa = randint(1,2)
                if wa == 1:
                        print(Performancemeasure.s_points-Performancemeasure.arrow)
                        print ("you killed the wumpus")
                elif wa == 2:
                    print(Performancemeasure.s_points-Performancemeasure.loss)
                    print("You got eaten by a wumpus")
                    break
            elif agent_location == pit1:
                print(Performancemeasure.s_points - Performancemeasure.loss)
                print("you fell in a pit")
                break
            elif agent_location == pit2:
                print(Performancemeasure.s_points - Performancemeasure.loss)
                print("you fell in a pit")
                break
            elif agent_location == pit3:
                print(Performancemeasure.s_points - Performancemeasure.loss)
                print("you fell in a pit")
                break            
            elif agent_location == gold:
                print(Performancemeasure.s_points+Performancemeasure.win)
                print("Agent received the gold. You win!!!")
                print("you can climb up")
                break
                
       
if __name__ == '__main__':
    main()
