import random as r

comp_choice = r.randint(1,3)
print(comp_choice)

user_choice = int(input("choose : 1-rock, 2-paper, 3-scicor"))

if comp_choice == user_choice:
    print("draw")
elif comp_choice == 1 and user_choice == 2:
    print("you win")
elif comp_choice == 1 and user_choice==3:
    print("you lose")
elif comp_choice==2 and user_choice==1:
    print("you lose")
elif comp_choice==2 and user_choice==3:
    print("you win")
elif comp_choice==3 and user_choice==1:
    print("you win")
elif comp_choice==3 and user_choice==2:
    print("you lose")

else:
    print("invalid")