import random
import os 
import black_jack_logo as l


def deal_card():    # function to choose random card 
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]    # for simplicity we do not remove that card we can use it again
    card = random.choice(cards)
    return card

def black_jack(cards): # we check if theres a black jack If yes that user will win
    if sum(cards) == 21:
       return 0
    return 1

def calculate_score(cards):
    if black_jack(cards) == 0:
        return 0

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
        
    
print(l.logo)
user_cards = []
computer_card = []

for _ in range(2): # Two cards for user and computer
    user_cards.append(deal_card())
    computer_card.append(deal_card())
    

win = False
user_name = input("Enter Your name To play : ")

while win == False:
        
        print(f"{user_name} Cards Are:{user_cards} ")
        print(f"Computer Cards Are:[ {computer_card[0]}, _ ]")
        
        if black_jack(user_cards) == 0:
            print("----You Winx-----")
            exit()
            clear_cards(user_cards,computer_card)
        elif black_jack(computer_card)== 0:
            print("----Computer Winx-----")
            exit()
    
        finish = False    
        while finish == False:
            choice = input("Do You Want To Stay or Draw another (s/d) : ").lower()
            if choice == "d":
                user_cards.append(deal_card())
                print(f"Your Cards Are:{user_cards} ")
                
                if calculate_score(user_cards) > 21:
                    print(f"----{user_name} BUSTED : Computer Win-----")
                    finish = True
                    exit()
                    
            elif choice == "s":
                finish = True
                
        while calculate_score(computer_card)  < 17:
            computer_card.append(deal_card())
            if calculate_score(computer_card) > 21:
                print(f"----Computer BUSTED : {user_name} Win-----")
                exit()
        
        
        if calculate_score(user_cards) > calculate_score(computer_card):
            print("-----You Winw----")
            print(f"Your Cards Are:{user_cards} ")
            print(f"Computer Cards Are: {computer_card} ")
            exit()
        elif calculate_score(user_cards) < calculate_score(computer_card):
            print("-----Computer Winw----")
            print(f"Your Cards Are:{user_cards} ")
            print(f"Computer Cards Are: {computer_card} ")
            exit()
        else:
            print("-----Draw----")
            exit()

            
            

   


            

        

            

        
                
        
                
                
                
                
                
            
        
    
        
        


        
            