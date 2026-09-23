name=input("Enter ur name : ")
age=int(input("Enter ur age : "))
phone_no=int(input("Enter ur phone no : "))
address=input("Enter ur address : ")
people=int(input("Enter no of people : "))


#-------------------------------------------

print(f"----------HELLO {name} !--------")




print("[1] Room \n[2] food \n[3] Food and Room \n[4] Exit \n[5] customer data")

print(10*"---")


total= 0


while True:
  reply=int(input("Enter no: "))

  
  
  if reply == 1:
    
    print(" [1] single room - $500 per day \n [2] Double room - $1000 per day \n [3] Ac room - $1500")
    
    reply_room=int(input("Enter  no from above : "))

    if reply_room==1:
      days=int(input("Enter no of days : "))
      total= 500 * days
      print(f"Order placed for single room. Bill : ${total}")
    elif reply_room==2:
      days=int(input("Enter no of days : "))
      total= 1000 * days
      print(f"Order placed for Double room. Bill : ${total} ")
    elif reply_room==3:
      days=int(input("Enter no of days : "))
      total= 1500 * days
      print(f"Order placed for Ac room. Bill : ${total}")
      
  elif reply== 2:
    print("[1] pizza - $50  \n [2] momos - $10 \n [3] burger - $15 \n [4] matar paneer - $20 \n [5] noodles - $15")
    print(10*"---")
    reply_food=int(input("Enter no for food : "))
    
    if reply_food==1:
      
      quantity=int(input("Enter Qty  : "))
      total = total + (50*quantity)
      print(f"Order placed ! Bill : ${total} ")
      
    elif reply_food==2:
      
      quantity=int(input("Enter Qty  : "))
      total= total + (10*quantity)
      print(f"Order placed ! Bill : ${total} ")
      
    elif reply_food==3:
      
      quantity=int(input("Enter Qty  : "))
      total =total + (15*quantity)
      print(f"Order placed ! Bill : ${total} ")
      
    elif reply_food==4:
      quantity=int(input("Enter Qty  : "))
      total= total +(20*quantity)
      print(f"Order placed ! Bill : ${total} ")
      
      
    elif reply_food==5:
      quantity=int(input("Enter Qty  : "))
      total = total + (15*quantity)
      print(f"Order placed ! Bill : ${total} ")
      
  elif reply == 3:
    
    print("[1] single room - $500 per day \n [2] Double room - $1000 per day \n [3] Ac room - $1500")
    print(10*"---")
    print("[a] pizza - $50  \n [b] momos - $10 \n [c] burger - $15 \n [d] matar paneer - $20 \n [e] noodles - $15")
    print(10*"---")
    
    reply_food_and_room = input("Enter no e.g [1+a] : " )
    days=int(input("Enter no of days : "))
    quantity=int(input("Enter Qty  : "))

    if reply_food_and_room == "1+a":
      total = (500*days)+(50*quantity)
      discount= 10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room == "1+b":
      total = (500*days)+(10*quantity)
      discount = 10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room== "1+c":
      total= (500*days)+(15*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="1+d":
      total= (500*days)+(20*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="1+e":
      total= (500*days)+(15*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="2+a":
      total = (1000*days)+(50*quantity)
      discount= 10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="2+b":
      total = (1000*days)+(10*quantity)
      discount = 10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="2+c":
      total= (1000*days)+(15*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="2+d":
      total= (1000*days)+(20*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="2+e":
      total= (1000*days)+(15*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="3+a":
      total = (1500*days)+(50*quantity)
      discount= 10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="3+b":
      total = (1500*days)+(10*quantity)
      discount = 10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="3+c":
      total= (1500*days)+(15*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="3+d":
      total= (1500*days)+(20*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
    elif reply_food_and_room=="3+e":
      total= (1500*days)+(15*quantity)
      discount=10/100*total
      final_price=total-discount
      print(f"Bill : ${final_price}")
  elif reply==4:
    close=input("Type yes for exit : ")
    if close=="yes":
      break
  elif reply==5:
    print(f" name = {name} \n age = {age} \n phone no = {phone_no} \n Address ={address} \n No of people = {people}")


    