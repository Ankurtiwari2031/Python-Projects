
#user input
user = input("enter username : ")
pass1 = input("enter password : ")


#user data
password = "Dark2031"
username = "Ankur"

# data checking
if user == username and pass1 == password:
  print(f"Hi there {user} , your private safe was sucessfully opened !")
  
  #table making 
  num = int(input("enter no. : "))
  for i in range(1,11):
    print(num*i)
    #greeting
  print("thank you for giving your precious time. !")

else:
  print("username or password is incorrect ! try again !!")

