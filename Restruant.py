import time
Veg_biriyani=150
panner_biriyani=120
chicken_biriyan=250
Mutton_Biriyani=300
vennala_cream=40
Straberry=100
Mango=100
Spirit=100
print("==========Online Food booking=============")
print("WELCOME TO FOOD COURT")
print("1.English")
print("2.Hindi")
print("3.Telugu")
print("4.kannada")
lan=input("Select the Language choice(1/2/3/4):")
if lan=="1":
    print("You choose English thank you!")
    time.sleep(3)
    print("=MENU Card=")
    print("1.Vegtarian food items")
    print("2.Nonvegtarian food items")
    print("3.Ice-crems")
    print("4.Juices")
    food=input("which item do you want:")
    if food=="1":
        print("Veg-Items")
        time.sleep(3)
        print("Veg-Biryani:",Veg_biriyani)
        print("Panner_biriyani:",panner_biriyani)
        person=input("if want both(y/n):")
        if person=="y":
            print("ALL-Veg Items",Veg_biriyani+panner_biriyani)
        else:
            print("Thank you for visiting! have a nice day!")
    elif food=="2":
        print("Non-Veg-Items")
        time.sleep(2)
        print("Chicken-biriyani:",chicken_biriyan)
        print("Mutton_Biriyani:",Mutton_Biriyani)
        person=input("if want both(y/n):")
        if person=="y":
            print("All_Nonveg items",chicken_biriyan+Mutton_Biriyani)
        else:
            print("Thank you for visiting! have a nice day!")
    elif food=="3":
        print("Ice-crems")
        print("Vennala_cream:",vennala_cream)
        print("Straberry:",Straberry)
    elif food=="4":
        print("Juices")
        time.sleep(3)
        print("Mango:",Mango)
        print("Spirit:",Spirit)
    else:
        print("Wrong Choice")

else:
    print("Choose only English! please")