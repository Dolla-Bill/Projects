import math

print("\n\ninvestment - to calculate the amount of interest you'll earn on interest \nbond - to calculate the amount you'll have to pay on a home loan")

calculation_choose = input("\n\nChoose either 'investment' or 'bond' from the below menu to proceed: ").lower()
if calculation_choose=='investment':
    p = float(input("Please input the amount of money you are depositing: "))
    r = float(input("Please input the interest rate your investment will be invested at E.g. 8(NB - No need to add the % sign): "))
    t = int(input("Please input the number of years you plan on investing for: "))

    interest = input("Please confirm if your interest rate will be realized on simple or compound interest: ").lower()

    r_rate = r/100

    if interest == 'simple':
        A = p*(1+r_rate*t)
        print(A)
    if interest == 'compound':
        A = p* math.pow((1+r_rate),t)
        print(A)
        
    

elif calculation_choose=='bond':
    p_1 = float(input("Please input the present value of the house: "))
    i_a = float(input("Please input the annual interest rate on the bond agreement E.g. 7: "))
    n = int(input("Please input the loan duration of the bond in months: "))

    i = (i_a/100)

    x = (p_1*i*((1+i)**n))/((1+i)**(-n))

    print(x)
    
else:
    print("Error: Please note you have not selected an appropriate option!")
    

