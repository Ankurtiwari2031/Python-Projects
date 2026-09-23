
#user input
user = input("Enter Username : ")
pass1 = input("Enter Password : ")


#user data
password = "Dark2031"
username = "Ankur"

# data checking
if user == username and pass1 == password:
  print(f"Hi there {user} , your private safe was sucessfully opened !")

  
  #Default value
  balance = 10000
  respond=0

  while respond !=4:
  
  #Menu======================================
    print("="*20)
    print("[1] check_balance \n[2] withdraw_money \n[3] deposit_money \n[4] exit")
    print("="*20)
    respond = int(input("Enter no. : "))
  #==========================================
    if respond ==1:
      print(f"you have  ${balance} money")
    #----------------------------------------
    elif respond ==2:
      withdraw=int(input("Enter amount : "))
      
      if withdraw > balance:
        print("Insufficient Balance")
        print("°"*25)
      else:
        balance-=withdraw
        print(f"you have${balance} left. ")
    #----------------------------------------
      
    elif respond==3:
      deposit = int(input("Enter amount : "))
      balance += deposit
      print(f"current amount = ${balance} ")
    #----------------------------------------
    elif respond>4 or respond<0:
      print(" plz enter valid number ! ")
      print("~"*16)
      print(" Thank you ! have a nice day .")  
      print("---"*15)  
else:
  print("username or password is Incorrect ! try again !!  ")
  print("-----"*15)  
    
    
    
    
    
    
    