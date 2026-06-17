print("welcome to tip calculator") 

bill = float(input("what was your total bill: "))

total_person = float(input("how many total person: "))

tip = int(input("how much tip type one: 12% , 15% , 20% "))

total =round(bill * tip/100 + bill,2) 
per_person = round(total / total_person,2)

print(f"your total bill is ${total}\nper head : ${per_person}")