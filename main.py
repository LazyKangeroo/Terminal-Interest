def calAnn(timeperiod, amnt, deposits, rate):
    new_amnt = amnt
    while timeperiod > 0:
        new_amnt += deposits
        new_amnt += new_amnt * rate / 100 / 12
        timeperiod -= 1
    print(f"\n= R{round(new_amnt,2)}")


def calMonthly(timeperiod, amnt, deposits, rate):
    new_amnt = amnt
    while timeperiod > 0:
        new_amnt += deposits
        new_amnt += new_amnt * rate / 100
        timeperiod -= 1
    print(f"\n= R{round(new_amnt,2)}")

print('---Welcome to the Investment Calculator---\n')

start_amnt = float(input("Enter starting amount: \n > R"))

print("\nWhich Intrest Rate: \n (1) Annoally [yearly]\n (2) Monthly")
rate_type = int(input(">> "))

rate = float(input("\nEnter rate in %:\n >"))

print("\n//NOTE// Period of time is monthly.\n")
timeperiod = int(input("Enter period of time:\n >> "))

deposits = float(input("\nMontly Deposits into Account:\n > R"))

match rate_type:
    case 1:
        calAnn(timeperiod,start_amnt,deposits,rate)
    case 2:
        calMonthly(timeperiod,start_amnt,deposits,rate)
    case _:
        print("\n[!] Error: Rate Type incorrect input")