def main():
    print('This is a monthly payment loan calculator')
    print("")


    principal = float(input('Enter the loan amount: '))
    apr = float(input('Enter the amount interest rate: '))
    years = int(input('Enter amount of years: '))


    monthly_interet_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interet_rate / (1 - (1 + monthly_interet_rate) ** (-amount_of_months))

    print('The monthly payment for this loan is: %.2f ' % monthly_payment)
main()