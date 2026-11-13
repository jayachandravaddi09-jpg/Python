import time
pin=1234
Balance=100000
print("Welcome Pentagon ATM")
print("Insert card")
print("Press for Continue 1.yes 2.NO")
c=int(input("Enter your choice:"))
if c==1:
    print("Select Language:")
    print("1.English")
    print("2.Telugu")
    print("3.Kannada")
    lang=int(input("Enter your choice:"))
    if lang==1:
        password=int(input("Enter your ATM pin:"))
        if pin==password:
            print("Select options")
            print("1.Check Balance")
            print("2.Withdral money")
            a=int(input("Enter your choice:"))
            if a==1:
                print("Avalable balance:",Balance)
            elif a==2:
                Amt=int(input("Enter Amount(1000 or 100 only):"))
                if Amt%100==0:
                    time.sleep(3)
                    print("Transaction being processed")
                    time.sleep(2)
                    print("please wait")
                    time.sleep(4)
                    print("Collect cash")
                    bal=input("You want check balance(yes/no):")
                    if bal=="yes":
                        print("Your balance is: ",Balance-Amt)
                        print("Thank you for Transaction,visit again")
                    else:
                        print("Thank you for using Pentagon ATM! visit again")
                elif Balance<Amt:
                    print("Insufficient balance")
                else:
                    print("invalid amount")
            else:
                print("Invalid option")
        else:
            print("Invalid Pin")
    else:
        print("select only English")
elif c==2:
    print("Thank you for using Pentagon ATM")
else:
    print("Card insert properly")

