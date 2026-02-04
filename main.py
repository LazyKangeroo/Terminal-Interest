#* Welcome message
print('---Welcome to the Investment Calculator---\n')

start_amnt = float(input("Enter starting amount: \n > R"))

print("\nWhich Intrest Rate: \n (1) Annoally [yearly]\n (2) Monthly")
rate_type = int(input(">> "))

rate = float(input("\nEnter rate in %:\n >"))

print("\n//NOTE// Period of time is monthly.\n")
timeperiod = int(input("Enter period of time:\n >> "))

#? Deposits
if input('Do you deposit any additional amounts into this account?\n (y/n) >> ')[0].upper() == 'Y':
    deposits = float(input("\nDeposits into Account:\n > R"))

    deposit_options = int(input("When do you make deposits?\n (1) Montly\n (2) Every second month\n (3) Quarterly \n (4) Semi-Annually\n >"))
    match deposit_options:
        case 1:
            frequency = 1
        case 2:
            frequency = 2
        case 3:
            frequency = 3
        case 4:
            frequency = 6
        case _:
            print("\n[!] Error: Deposit Options incorrect input")
            exit()
else:
    deposits = 0
    frequency = 0

#! cal interest
def ann(amnt,rate):
    return amnt * rate / 100 / 12

def monthly(amnt,rate):
    return amnt * rate / 100

new_amnt = start_amnt
count_month = 1

while timeperiod > 0:
    if count_month == frequency:
        new_amnt += deposits
        count_month = 0

    match rate_type:
        case 1:
            new_amnt += ann(new_amnt,rate)
        case 2:
            new_amnt += monthly(new_amnt,rate)
        case _:
            print("\n[!] Error: Rate Type incorrect input")
            exit()

    timeperiod -= 1
    count_month += 1

print(f"\n= R{round(new_amnt,2)}")