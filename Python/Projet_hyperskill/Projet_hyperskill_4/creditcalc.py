import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--interest', type=float, required=True)
parser.add_argument('--periods', type=int)
parser.add_argument('--type', required=True, choices=['diff', 'annuity'])

args = parser.parse_args()

def annuity_calc_nb_months(monthly_payments, interet, loan_principal):  #non utilisable en diff
    interet = (interet / 100) / 12
    dict_mois = {'1' : 0.0833,
             '2' : 0.1667,
             '3' : 0.25,
             '4' : 0.3333,
             '5' : 0.4167,
             '6' : 0.5,
             '7' : 0.5833,
             '8' : 0.6667,
             '9' : 0.75,
             '10' : 0.8333,
             '11' : 0.9166}
    mois = ''
    nb_months = math.log(monthly_payments / (monthly_payments - interet * loan_principal), (1 + interet))
    n = math.ceil(nb_months)
    n_prime1 = n / 12
    n_prime2 = n // 12
    n_prime3 = round(n_prime1 - n_prime2, 4)
    for key, val in dict_mois.items():
        if val == n_prime3:
            mois = key
    if mois != '':
        print(f'It will take {n_prime2} years and {mois} months to repay this loan!')
        result = monthly_payments * n - loan_principal
        print('Overpayment = ', result)
    else:
        print(f'It will take {n_prime2} years to repay this loan!')
        result = round(monthly_payments * n - loan_principal)
        print('Overpayment = ', result)
def annuity_calc_monthly_payments(nb_months, interet, loan_principal):
    interet = (interet / 100) / 12
    monthly_payments = math.ceil(loan_principal * ((interet * (1 + interet) ** nb_months) / ((1 + interet) ** nb_months - 1))) 
    print(f'Your monthly payment = {str(monthly_payments)}.')
    print('Overpayment = ', monthly_payments * nb_months - loan_principal)
def annuity_calc_loan_principal(monthly_payments, interet, nb_months):
    interet = (interet / 100) / 12
    loan_seek = round((monthly_payments / ((interet * (1 + interet) ** nb_months) / ((1 + interet) ** nb_months - 1))))
    print(f'Your loan principal = {loan_seek}!')
    print('Overpayment = ', monthly_payments * nb_months - loan_seek)
def diff_calc_monthly_payments(nb_months, interet, loan_principal):
    interet = (interet / 100) / 12
    Overpayment = 0
    for i in range(1, (nb_months + 1)):
        monthly_payments = math.ceil(loan_principal / nb_months + interet * (loan_principal - ((loan_principal * (i - 1)) / nb_months)))
        print(f'Month {i}: payment is {monthly_payments}')
        Overpayment = Overpayment + monthly_payments
    print('Overpayment = ', Overpayment - loan_principal)

if args.type == 'annuity':
    if args.payment != None and args.principal != None and args.interest != None:
        if args.payment < 0 or args.principal < 0 or args.interest < 0:
            print('Incorrect parameters.')
            exit()
        annuity_calc_nb_months(args.payment, args.interest, args.principal)
    elif args.periods != None and args.principal != None and args.interest != None:
        if args.periods < 0 or args.principal < 0 or args.interest < 0:
            print('Incorrect parameters.')
            exit()
        annuity_calc_monthly_payments(args.periods, args.interest, args.principal)
    elif args.payment != None and args.periods != None and args.interest != None:
        if args.payment < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters.')
            exit()
        annuity_calc_loan_principal(args.payment, args.interest, args.periods)
    else:
        print('Incorrect parameters.')
elif args.type == 'diff':
    if args.periods != None and args.principal != None and args.interest != None:
        if args.periods < 0 or args.principal < 0 or args.interest < 0:
            print('Incorrect parameters.')
            exit()
        diff_calc_monthly_payments(args.periods, args.interest, args.principal)
    else:
        print('Incorrect parameters.')
else:
    print('Incorrect parameters.')