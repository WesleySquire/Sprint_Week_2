#Sprit Week 2 - Project 1 - Python + Github
#Create a file for default values and call it TCDef.dat.  The file will contain the Claim Number(143), the HST Rate(.15), the low per diem rate (85.00), 
#the high per diem rate (100), the mileage rate (.10), the rental car rate (56.00)
#Start by presenting the following menu to the user.  Validate the input to allow only 1 –5.  Set up functions for each of the choices–add a comment to describe the function only.
#Include  at  least 2  other  functionsin  the  program  that  accept  values  as  parameters  and return a value(s) to the program.  
#Add comment to these functions including a description, list of parameters, and a list of return values.

######################################
#
#MENU
#INPUT
#1-5 for what to do in menu -
#
#PROCESSING
#Do function that user inputed - Travel Claim - Edit Def Values - Print Travel Claim Report - Graph Monthly Claim Totales - Quit
#
######################################
#
#Employee Travel Claim
#Will process travel claims returned to office - read def values from file for system to use
#INPUT
#Emp Num, Name, Local of trip, start date, end date, value for rented or owned, total km traveled (Only if used own car)
#Processing
#Calc per diem by multiplying total days by daily rate of 85 for claims of 3 days or less or a dailt rate of 100 for 4 or more days
#.10 per KM traveled if owned car or 56 per day if owner rented car
#Claim amount calculated by Per Diem + Mileage amount, HST on only per diem, Claim Total = Claim Amount + HST
#Write all input values and calc values to a file called Claims.dat - use comma seperated format w/ all claims on same line
#Invoice num += 1
#Repeat program until user enters termination value at end of claim processing
#Once program ends write current values back to default table so its up to date once you start the program next time
#OUTPUT
#All inputs and calc values - basic printout w/ headings + values
#Display that claim has been processed and info saved, update invoice num by 1
#
#######################################
#
#Edit System Values
#Write this function to read the values from the defaults table, display a couple of headings at the beginning with, company name and subtitle (Edit System Default Values) 
#Followed with a series of inputs to allow  the  user to enter new values,  if required, for each of thedefault values. 
#Once completewrite the new updated values to the defaults file and display a message telling the user that the default values have been successfully updated
#Display a message to “Press any key to continue ...” before returning to the menu.
#INPUT
#Inputs to allow user to enter new values, and press any key to continue at end
#PROCESSING
#Read values in TCDef.dat table, write new defaulted values to file
#OUTPUT
#Couple headings at beggining w/ company name and subtitle (Edit System Default Values)
#Message saying default values have been successfully updtated


"""Wesley Squire + Bradon Walsh
    Sprint Week 2, Python + Github
     March 12, 2021 - MMMM DD, YYYY"""

#Importing backpack and datetime
import Backpack as BP
from datetime import date
from datetime import datetime

#Travel Claim Function - Wesley Squire, March 13, 2021
def EmpTravClaim(): 
    f = open('/home/ec2-user/environment/Sprint_Week_2/TCDef.dat', 'r')
    ClaimNum = int(f.readline())
    HSTRate = float(f.readline())
    LowPerDiemRate = float(f.readline())
    HighPerDiemRate = float(f.readline())
    MileageRate = float(f.readline())
    RentalRate = float(f.readline())
    f.close()

    while True:
        
        #Inputs for emp info and claims
        EmpNum = str(input(" Enter Employee Number : "))
        EmpName = input(" Enter Employee Name: ")
        Location = input(" Enter The Location Of The Trip: ")
        
        staryear = int(input(" Enter Start Year Of Trip: "))
        starmonth = int(input(" Enter Start Month Of Trip: "))
        starday = int(input(" Enter Start Day Of Trip: "))
    
        endyear = int(input(" Enter End Year Of Trip: "))
        endmonth = int(input(" Enter Ending Month Of Trip: "))
        endday = int(input(" Enter End Day Of Trip: "))
    
        Date1 = date(staryear, starmonth, starday)
        Date2 = date(endyear, endmonth, endday)
        DaysGone = Date2 - Date1
        NumDays = DaysGone.days
        
        Car = input(" Was The Car Used Rented Or Owned (Enter 'O' For Owned or 'R' for Rented): ")
      
        ################################################
        
        #Calcs for if Car was Rented or Owned
        if (Car == "O") or (Car == "o"):
            KmTrav = float(input(" Enter Kilometers Travelled: "))
            PaymentKm = KmTrav * MileageRate
            RentedOwned = "Owned"
        elif (Car == "R") or (Car == "r"):
            PaymentKm = NumDays * RentalRate
            RentedOwned = "Rented"
            KmTrav = "N/A"
        if (NumDays <= 3):
            DailyRate = NumDays * LowPerDiemRate
        elif (NumDays >= 4):
            DailyRate = NumDays * HighPerDiemRate
        print("-="*27 + "-")
        
        ###############################################
        
        #Calcs for SubClaim, Tax, and ClaimTotal
        SubClaim = DailyRate + PaymentKm
        HST = SubClaim * HSTRate
        ClaimTotal = SubClaim + HST
        print()
        print()
        print()
        
        ###############################################
        
        #This write downs the data claims in the Claims.dat folder
        f = open("/home/ec2-user/environment/Sprint_Week_2/Claims.dat", "a")
        f.write("{}, ".format(str(ClaimNum)))
        f.write("{}, ".format(EmpName))
        f.write("{}, ".format(str(DailyRate)))
        f.write("{}, ".format(str(PaymentKm)))
        f.write("{}, ".format(str(SubClaim)))
        f.write("{}, ".format(str(HST)))
        f.write("{}, ".format(str(ClaimTotal)))
        f.write("{}, ".format(Location))
        f.write("{}, ".format(RentedOwned))
        f.write("{}, ".format(str(KmTrav)))
        f.write("{}, ".format(str(NumDays)))
        f.write("{}, ".format(str(Date2)))
        f.write('\n')
        f.close()
        
        ##############################################
        
        #Print Statements and formatting
        print(" Employee Number: {}".format(EmpNum))
        print(" Name: {}                Location: {}".format(EmpName, Location))
        print(" Claim #: {}".format(ClaimNum))
        print(" Start Date: {}".format(Date1))
        print()
        print(" End Date: {}         Days On Trip: {}".format(Date2, DaysGone))
        print(" Car Was: {}         ".format(RentedOwned))
        print()
        print(" Kilometers Travelled: {}        Per Diem: ${:,.2f}".format(KmTrav,SubClaim))
        print("                                         Hst: ${:,.2f}".format(HST))
        print("                                             ---------")
        print("                                 Claim Total: ${:,.2f}".format(ClaimTotal))
        print("-="*27 + "-")
        print("    Process Data Succefully Saved To File")
        print()
        
        #############################################
        
        #This Increases the claim num by 1 
        ClaimNum += 1
        
        #Asks user if they want to process another claim
        Cont = input("Process another claim (Y/N): ")
        if Cont.upper() != "Y":
            break
    
    #This re-writes and stores the claimnum and hstrate
    f = open('/home/ec2-user/environment/Sprint_Week_2/TCDef.dat', 'w')
    f.write("{}\n".format(str(ClaimNum)))
    f.write("{}\n".format(str(HSTRate)))
    f.write("{}\n".format(str(LowPerDiemRate)))
    f.write("{}\n".format(str(HighPerDiemRate)))
    f.write("{}\n".format(str(MileageRate)))
    f.write("{}\n".format(str(RentalRate)))
    f.close()

#Function to edit system values in TCDef.dat - Wesley Squire, March 14, 2021
def EditSystemValues():
    print("              NL Chocolate Company")
    print("           Edit System Default Values")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    f = open('/home/ec2-user/environment/Sprint_Week_2/TCDef.dat', 'r+')
    ClaimNum = int(f.readline())
    HSTRate = float(f.readline())
    LowPerDiemRate = float(f.readline())
    HighPerDiemRate = float(f.readline())
    MileageRate = float(f.readline())
    RentalRate = float(f.readline())
    print("Claim  HST   LowPer  HighPer  Mileage   Rental")
    print("Number Rate   Rate    Rate     Rate      Rate")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("{:<3}   {:<3}   {:<6}  {:<6}   {:<3}       {:<3}".format(ClaimNum, HSTRate, LowPerDiemRate, HighPerDiemRate, MileageRate, RentalRate))
    f.close
    
    f = open('/home/ec2-user/environment/Sprint_Week_2/TCDef.dat', 'w+')
    ClaimNum = input(" Please enter new claim number: ")
    HSTRate = input(" Please enter new HST rate: ")
    LowPerDiemRate = input(" Please enter new Low Per Diem rate: ")
    HighPerDiemRate = input(" Please enter new High Per Diem rate: ")
    MileageRate = input(" Please enter new Mileage rate: ")
    RentalRate = input(" Please enter new Rental rate: ")
    f.write("{}\n".format(str(ClaimNum)))
    f.write("{}\n".format(str(HSTRate)))
    f.write("{}\n".format(str(LowPerDiemRate)))
    f.write("{}\n".format(str(HighPerDiemRate)))
    f.write("{}\n".format(str(MileageRate)))
    f.write("{}\n".format(str(RentalRate)))
    f.close()
        
    print()
    print("    Default Values Have Been Succefully Updated.")
    AnyKey = input("Press any key to continue... ")

#Function for the travel claim report - Wesley Squire, March 15, 2021


def TravelClaimReport():
    ClaimCtr = 0
    PerDiemTotal = 0
    MileageTotal = 0
    ClaimTotalAcc = 0
    print("         1         2         3         4         5         6         7         8")
    print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
    print()
    print(" " * 32 + "NL CHOCOLATE COMPANY")
    print()
    print(" " * 23 + "TRAVEL CLAIMS LISTING AS OF " + datetime.today().strftime('%m-%d-%Y'))
    print()
    print("CLAIM   CLAIM      SALESPERSON        CLAIM     PER DIEM    MILEAGE      CLAIM")
    print("NUMBER  DATE          NAME           LOCATION    AMOUNT     AMOUNT       AMOUNT")
    print("=" * 80)
    f = open('/home/ec2-user/environment/Sprint_Week_2/Claims.dat', 'r')
    for claims in f:
        Claimlist = claims.split(",")
        ClaimNum = Claimlist[0]
        EmpName = Claimlist[1].strip()
        PerDiem = float(Claimlist[2].strip())
        MileageAmt = float(Claimlist[3].strip())
        SubClaim = float(Claimlist[4].strip())
        HST = float(Claimlist[5].strip())
        ClaimTotal = float(Claimlist[6].strip())
        ClaimLocation = str(Claimlist[7].strip())
        RentedOwned = str(Claimlist[8].strip())
        KMTrav = str(Claimlist[9].strip())
        NumDays = int(Claimlist[10].strip())
        ClaimDate = Claimlist[11]
        
        
        print(" {} {} {:<20} {:<10} ${:,.2f}    ${:<6,.2f}    ${:,.2f}".format(ClaimNum, ClaimDate, EmpName, ClaimLocation, PerDiem, MileageAmt, ClaimTotal  ))
        
        ClaimCtr += 1
        PerDiemTotal += PerDiem
        MileageTotal += MileageAmt
        ClaimTotalAcc += ClaimTotal
    f.close()
    print("=" * 80)
    print("{:<2} claims listed                              ${:<8,.2f} ${:<8,.2f}      ${:<8,.2f}".format(ClaimCtr, PerDiemTotal, MileageTotal, ClaimTotal))
    print()
    print(" " * 32 + "END OF REPORT")
    AnyKey = input("Press any key to continue... ")
    
    
#Main Menu formatting and processing - Wesley Squire, March 13, 2021
def main():
    while True:    
        
        print()
        print("NL Chocolate Company")
        print("Travel Claims Processing System")
        print()
        print("1. Enter an Employee Travel Claim.")
        print("2. Edit System Default Values.")
        print("3. Print Travel Claim Report.")
        print("4. Graph Monthly Claim Totals.")
        print("5. Quit Program.")
        print()
        
        while True:
            Choice = input("   Enter choice (1-7): ")
            IsValid = BP.ValIntNumber(Choice, 1, 7)
            if IsValid:
                Choice = int(Choice)
                break
   
        if Choice == 1:
            print()
            print("Employee Travel Claim...")
            EmpTravClaim()
        
        elif Choice == 2:
            print()
            EditSystemValues()
        
        elif Choice == 3:
            print()
            print("Printing Travel Claim Report...")
            TravelClaimReport()
        
        
        elif Choice == 4:
            print()
            print("Graphing Monthly Claim Report...")
            #GraphMonClaimRep()
            
        
        elif Choice == 5:
            exit(0)
            
        elif Choice == 6:
            print()
            
        elif Choice == 7:
            print()
        
        
        else:
            exit(0)
    
        
if __name__ == "__main__":
    main()
