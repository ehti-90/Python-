import logo as l
from data import accounts
import random
import os

# function to choose random accounts from data
def choose_data(accounts):
    r = random.randint(0,20)
    account =  accounts[r]
    return account
  
def duplicate(a,b):
    if a == b:
        return True
    return False
   
# formating to improve user experience
def format(account):
    name = account["name"]
    country = account["country"]
    descrip = account["description"]
    
    return f"{name} - { country} - {descrip}"
    

def  check_answer(user, acc_a_f ,acc_b_f):  # check if guess is correct
    if acc_a_f > acc_b_f and user =="A":
        return True
    elif acc_a_f < acc_b_f and user =="B":
        return True
    else:
        return False
    
def game():       
    print(l.name)
    account_a = choose_data(accounts)
    account_b = choose_data(accounts)

    score = 0 

    follower_a = account_a["followers_million"]
    follower_b = account_b["followers_million"]

    if duplicate(account_a,account_b): #   if we get both same then choose another account_b
        account_b = choose_data(accounts)
        
    print(f"Choice A: {format(account_a)}")
    print(l.vs)
    print(f"Choice B: {format(account_b)}")

    user_guess = input("Who has more Followers:Type (A/B) ").upper()

    while user_guess not in ["A", "B"]:
        print("Wrong : Choose (A/B)")
        user_guess = input("Who has more Followers:Type (A/B) ").upper()


    is_correct  = check_answer(user_guess,follower_a ,follower_b)
    os.system("cls")


    if is_correct :
        score += 1
        print(f"You're Correct : current score {score}")
    else:
        print(f"You're Wrong : Final score {score}")

    while is_correct :
        
        account_a = account_b
        account_b = choose_data(accounts)


        follower_a = account_a["followers_million"]
        follower_b = account_b["followers_million"]

        if duplicate(account_a,account_b): #   if we get both same account  then choose another account_b
            account_b = choose_data(accounts)
        
        print(f"Choice A: {format(account_a)}")
        print(l.vs)
        print(f"Choice B: {format(account_b)}")    
        
        user_guess = input("Who has more Followers:Type (A/B) ").upper()
        is_correct  = check_answer(user_guess,follower_a ,follower_b)
        os.system("cls")

        if is_correct :
            score += 1
            print(f"You're Correct : current score {score}")
        else:
            print(f"You're Wrong : Final score {score}")
    
        
game()







