import logos as logo
import os

#  os.system("cls")  # Windows clear terminal

print(logo.auction_log)
print("*-----------Welcome to the Blind Auction : Highest Bidder Wins-------- *")

data = {}   # dictionary to store bidder and bod data
cont = True
print("\n"*5)

while cont == True:
    
    name = input("Enter Bidder Name : ")
    amount  = int(input("Enter Your Bid:  $"))
    
    choice = input(" Bid to Continue : (yes/no) : ").lower() # if there are other bidders
    
    data[name] = amount

    if choice == "yes":
        os.system("cls")
    
    elif choice == "no": 
        cont = False
        highest = 0
        name = ""
         
        for bid in data:
            if data[bid] > highest:
                highest = data[bid]
                name = bid
        
        os.system("cls")
        print(f"{name} Wins: His Bid was ${highest} the Highest")
    else:
        print("Wrong Choice Try Again")
            
            
        
        
    
    
    
    
    