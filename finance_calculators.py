import math

print("Choose either 'investment' or 'bond' from the menu below to proceed:\n\n")
user_put = input('''
investment \t- to calculate the amount of interest you'll earn on interest
bond \t\t- to calculate the amount you'll have to pay on a home loan
''')

if user_put.lower() == "investment":
    amount = input("The amount of money that they are depositing: ")
    interest = float(input("Please enter the interest rate: ")) / 100
    years = input("Please enter the number of years that you would like to invest: ")
    interest_type = input("Please enter the investment type (compound or simple): ")
    if interest_type == "simple":
        a = float(amount) * (1 + float(interest) * float(years))
        earn_interest = float(a) - float(amount)
        print("Original value: R{0:.2f} Future vaule: R{1:.2f} after {2:.0f} year(s) at {3:.2f} % interest \nYou Earned: R{4:.2f} from your investment".format(float(amount),float(a),float(years),float(interest * 100),float(earn_interest)))
    elif interest_type == "compound":
        a = float(amount) * math.pow((1 + float(interest)),float(years))
        earn_interest = float(a) - float(amount)
        print("Original value: R{0:.2f} Future vaule: R{1:.2f} after {2:.0f} year(s) at {3:.2f} % interest \nYou Earned: R{4:.2f} from your investment".format(float(amount),float(a),float(years),float(interest * 100),float(earn_interest)))
elif user_put.lower() == "bond":
    present_value = input("Please enter present value of the house: ")
    interest = float(input("The interset rate: ")) / 100
    interest = interest / 12
    years = float(input("The Length of the loan in years: ")) * 12
    x = (float(interest) * (float(present_value)))/(1 - pow((1 + float(interest)),(-1 * float(years))))
    print("Your bond repayment: R{0:.2f}".format(x))

