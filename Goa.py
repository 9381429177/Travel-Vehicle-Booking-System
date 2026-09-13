#Booking Application
import time
print("!---Choose trip planning---!")
print("press 1.Goa 2.Pondicherry")
print("select your visiting place:")
choice=(int(input()))
if choice==1:
    print("went your transport plan:")
    print("press 1.Bus 2.train")
    choice=(int(input()))
    if choice==choice:
        print("Welcome to Goa")
        print("choose your Residential vehicle:")
        print("1.Bike")
        print("2.car")
        vehicle=int(input("Select your vehicle:"))
        if vehicle==1:
            print("Available bikes")
            print("--------------------")
            print("1.KTM")
            print("2.R15")
            print("3.SUZUKI")
            bike=int(input('Select your Bike:'))
            print('Please  enter your details')
            name=input('Enter your name:')
            number=int(input("Enter your number:"))
            days=int(input("Enter your days:"))
            AadharNumber=int(input("Enter your AadharNumber:"))
            DrivingLicense=int(input("Enter your DrivingLicense:"))
            print("Your booking details are as follows:")
            print("---------------------------------------")
            if bike==1:
                price=1000
                amount=price*days
                print("vehicle:KTM")
            elif bike==2:
                price=2000
                amount=price*days
                print("vehicle:R15",)
            elif bike==3:
                price=500
                amount=price*days
                print("vehicle:SUZUKI")
            print('your Name:',name)
            print('your ph number:',number)
            print('Number of days:',days)
            print("you AadharNumber:",AadharNumber)
            print("your DrivingLicense Number:",DrivingLicense)
            print("your total amount:",amount)
            print("-----------------------------------------")
            print("Do you want to proceed?")
            print("press 1.yes 2.no")
            choice=int(input())
            if choice==1:
                print("choose your payment method")
                print("press 1.cash 2.online")
                choice=int(input())
                if choice==1:
                    print("Your booking successfully!!!!!")
                    print("Thank you!!Enjoy your trip")
                else:
                    time.sleep(3)
                    print("your booking successfully!!!!!")
                    print("Thank you!!Enjoy your trip")
            elif choice==2:
                print("Thank you")
        elif vehicle==2:
            print("Available of cars:")
            print("---------------------------")
            print("1.THAR")
            print("2.KIA")
            print("3.FORTUNAR")
            car=int(input('Select your car:'))
            print('Please  enter your details:')
            print('--------------------------')
            name=input("Enter your name:")
            number=int(input("Enter your number:"))
            days=int(input("Enter your days:"))
            AadharNumber=int(input("Enter your AadharNumber:"))
            DrivingLicense=int(input("Enter your DrivingLicense:"))
            print("Your booking details are as follows:")
            print("---------------------------------------------")
            if car==1:
                price=3000
                amount=price*days
                print("vehicle:THAR")
            elif car==2:
                price=4000
                amount=price*days
                print("vehicle:KIA")
            elif car==3:
                price=5000
                amount=price*days
                print("vehicle:FORTUNAR")
            print('your Name:',name)
            print('your ph number:',number)
            print("Number of days:",days)
            print("your AadharNumber:",AadharNumber)
            print("your DrivingLicense number:",DrivingLicense)
            print("your total amount:",amount)
            print("Do you want to proceed?")
            print("press 1.yes 2.no")
            choice=int(input())
            if choice==1:
                print("choose your payment method")
                print("press 1.cash 2.online")
                choice=int(input())
                if choice==1:
                    print("Your booking successfully")
                    print("Thank you!!Enjoy your trip")
                else:
                    time.sleep(3)
                    print("Your booking successfully!!!!!")
            elif choice==2:
                print("Thank You")


elif choice==2:
        print("welcome to Pondicherry")
        print("choose your Residential vehicle:")
        print("1.Bike")
        print("2.car")
        vehicle=int(input("Select your Vehicle:"))
        if vehicle == 1:
            print("Available bikes")
            print("--------------------")
            print("1.ktm")
            print("2.R15")
            print("3.vespa")
            bike = int(input("Select your Bike:"))
            print("Please  enter your details")
            name = input("Enter your name:")
            number = int(input("Enter your number:"))
            days = int(input("Enter your days:"))
            AadharNumber = int(input("Enter your AadharNumber:"))
            DrivingLicense = int(input("Enter your DrivingLicense:"))

            print("Your booking details are as follows:")
            print("---------------------------------------")
            if bike==1:
                price=1200
                amount=price*days
                print("vehicle:ktm")
            elif bike==2:
                price = 1300
                amount = price * days
                print("vehicle:R15",)
            elif bike==3:
                price = 1000
                amount = price * days
                print("vehicle:Vespa")
            print("your Name:", name)
            print("your ph number:", number)
            print("Number of days:", days)
            print("you AadharNumber:", AadharNumber)
            print("your DrivingLicense number:", DrivingLicense)
            print("your total amount:", amount)
            print("-----------------------------------------")
            print("Do you want to proceed?")
            print("press 1.yes 2.no")
            choice=int(input())
            if choice == 1:
                print("choose your payment method")
                print("press 1.cash 2.online")
                choice=int(input())
                if choice==1:
                    print("Your booking successfully")
                    print("Thank you!!Enjoy your trip")
                else:
                    time.sleep(3)
                    print("your booking successfully!!!!!")
                    print("Thank you!!Enjoy your trip")
            elif choice==2:
                print("Thank you")
        elif choice==2:
            print("Available of cars:")
            print("---------------------------")
            print("1.Creta")
            print("2.Kia")
            print("3.Fortunar")
            car = int(input("Select your car:"))
            print("Please  enter your details:")
            print("--------------------------")
            name = input("Enter your name:")
            number = int(input("Enter your number:"))
            days = int(input("Enter your days:"))
            AadharNumber = int(input("Enter your aadhar number:"))
            DrivingLicense = int(input("Enter your DrivingLicense:"))
            print("Your booking details are as follows:")
            print("--------------------------------------------")
            if car == 1:
                price = 3000
                amount = price * days
                print("vehicle:Creta")
            elif car == 2:
                price = 4000
                amount = price * days
                print("vehicle:Kia")
            elif car == 3:
                price = 5000
                amount = price * days
                print("vehicle:Fortunar")
            print("your Name:", name)
            print("your ph number:", number)
            print("Number of days:", days)
            print("you AadharNumber:", AadharNumber)
            print("your DrivingLicense number:", DrivingLicense)
            print("your total amount:",amount)
            print("Do you want to proceed?")
            print("press 1.yes 2.no")
            choice=int(input())
            if choice==1:
                print("chosee your payment method")
                print("press 1.cash 2.online")
                choice=int(input())
                if choice==1:
                    print("Your booking successfully")
                    print("Thank you!!Enjoy your trip")
                else:
                    time.sleep(3)
                    print("Your booking successfully!!!!!")
                    print("Thank you!Enjoy your trip")
            else:
                print("Thank you")
else:
    print("select valid trip")

