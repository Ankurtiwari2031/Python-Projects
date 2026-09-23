print("Hi Master ! enter your Data below to open ur Master room")
print("•" * 77)


main_user = "Arcanum"
main_pass = "Arcanum20311"
user2 = "Amit"
pass2 = "Amit2031"
user3 = "Sumit"
pass3 = "Sumit2031"


trial = 1
while trial <= 3:
    local_user = input("Enter username : ")
    local_pass = input("Enter password : ")
    print("•" * 77)

    if local_user == main_user and local_pass == main_pass:
        # =============================================
        print("Welcome my lord ! ur secret vault opened  ")
        balance = 10000000000000
        respond = 0

        while respond != 4:
            # Menu======================================
            print("=" * 20)
            print(
                "[1] check_balance \n[2] withdraw_money \n[3] deposit_money \n[4] exit"
            )
            print("=" * 20)
            respond = int(input("Enter no. : "))
            # ======================≠===================
            if respond == 1:
                print(f"you have  ${balance} money")
            # ----------------------------------------

            elif respond == 2:
                withdraw = int(input("Enter amount : "))

                if withdraw > balance:
                    print("Insufficient Balance")
                    print("°" * 25)
                else:
                    balance -= withdraw
                    print(f"you have${balance} left. ")
            # ----------------------------------------

            elif respond == 3:
                deposit = int(input("Enter amount : "))
                balance += deposit
                print(f"current amount = ${balance} ")
            # ----------------------------------------
            elif respond > 4 or respond < 0:
                print(" plz enter valid number ! ")
                print("~" * 16)
                print(" Thank you ! have a nice day .")
                print("---" * 15)
            elif respond == 4:
                break

        break
    # ================================≠=============
    elif (local_user == user2 and local_pass == pass2) or (
        local_user == user3 and local_pass == pass3
    ):
        print(f"welcome {local_user} ! have a great day ")
        print("---" * 30)
        # =============================================
        # game
        Choosen_no = 0
        trial2 = 0
        while Choosen_no != 6:
            print(
                "[ Choose Number to continue ]\n1-Game\n2-vote\n3-calculator\n4-climate\n5-Table printing\n6-Exit"
            )
            print("-----" * 30)
            Choosen_no = int(input("Enter ur No.  here  : "))
            print("----" * 30)
            if Choosen_no == 1:
                print("Ur Game started ! Have fun ")
                secret_num = 67
                chances = 1
                while chances <= 5:
                    num = int(input("enter ur no : "))

                    if num < secret_num:
                        print("greater")

                    elif num > secret_num:
                        print("smaller")
                    elif num == secret_num:
                        print("congrats you find the no ! ")
                        break
                    chances += 1
                else:
                    print(" you lose game over !! ")
                    print("---" * 15)

                # ===========================================
                # vote
            elif Choosen_no == 2:
                print("Ur vote checking machine started")
                name = input("enter name: ")
                age = int(input("enter ur age: "))
                has_lisence = True

                print(f"Hi there {name}  , Have a great  day !!")

                if age >= 18 and has_lisence:
                    print("you r eligible for voting !")

                elif age >= 18 or not has_lisence:
                    print("sorry! make ur lisence first ")

                else:
                    print("sorry u r not eligible ! ")
            # =============================================
            # calculator
            elif Choosen_no == 3:
                print("calculator started")
                print("operator--> [*]\n[-]\n[+]\n[/]\n[**] for sqre. ")

                first_no = int(input("enter 1st no : "))
                second_no = int(input("enter 2nd no : "))
                opert = input("enter operator : ")
                if opert == "+":
                    print(first_no + second_no)
                elif opert == "-":
                    print(" Ans : ", first_no - second_no)
                elif opert == "*":
                    print(" Ans : ", first_no * second_no)
                elif opert == "/":
                    print(" Ans : ", first_no / second_no)
                else:
                    opert == "**"
                    print(first_no**second_no)
            # ============================================
            # climate
            elif Choosen_no == 4:
                temp = int(input("enter temp :  "))
                if temp >= 45:
                    print("its  too hot ! ")
                elif temp >= 30:
                    print("its not good wether ! ")
                else:
                    print("its good wether!")
            # ============================================
            # Table
            elif Choosen_no == 5:
                print("Table machine started")
                user = input("enter username : ")
                pass1 = input("enter password : ")
                # user data
                password = "Dark2031"
                username = "Ankur"
                # data checking
                if user == username and pass1 == password:
                    print(
                        f"Hi there {user} , your private safe was sucessfully opened !"
                    )
                    # table making
                    num = int(input("enter no. : "))
                    for i in range(1, 11):
                        print(num * i)
                        # greeting
                    print("thank you for giving your precious time. !")
            elif Choosen_no == 6:
                print("Thankyou for using me sir !")

                break

    else:
        print(" Sorry ur username or password  is incorrect try again ! ")

    trial += 1
