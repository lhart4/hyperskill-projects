import sys
import argparse
import math


def calculate_nominal_interest(interest):
    nominal_interest = interest / (12 * 100)
    return nominal_interest


def calculate_months(principal, monthly_payment, interest):
    nominal_interest = calculate_nominal_interest(interest)
    num_months = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_interest * principal), 1 + nominal_interest))
    return num_months


def calculate_annuity_payment(principal, interest, num_months):
    nominal_interest = calculate_nominal_interest(interest)
    payment = math.ceil(principal * (nominal_interest * (1 + nominal_interest) ** num_months) / ((1 + nominal_interest) ** num_months - 1))
    return payment


def calculate_differentiated_payment(principal, interest, num_months, current_period):
    nominal_interest = calculate_nominal_interest(interest)
    payment = math.ceil((principal/num_months) + nominal_interest * (principal - ((principal * (current_period - 1))/ num_months)))
    return payment


def calculate_principal(interest, num_months, monthly_payment):
    nominal_interest = calculate_nominal_interest(interest)
    principal = math.floor(monthly_payment / ((nominal_interest * (1 + nominal_interest) ** num_months) / ((1 + nominal_interest) ** num_months - 1)))
    return principal


def calculate_total_payment(payment_type, principal, interest, periods):
    if payment_type == 'diff':
        total_payment = differentiated_payment(principal, interest, periods, verbose=False)
    elif payment_type == 'annuity':
        total_payment = payment * periods
    return total_payment


def print_months(num_months):
    years = math.floor(num_months / 12)
    months = num_months % (years * 12)
    if years == 1:
        yrs = 'year'
    else:
        yrs = 'years'
    if months == 1:
        mon = 'month'
    else:
        mon = 'months'
    if years >= 1 and months == 0:
        print(f'You need {years} {yrs} to repay this credit!')
    elif years == 0 and months >= 1:
        print(f'You need {months} {mon} to repay this credit!')
    else:
        print(f'You need {years} {yrs} and {months} {mon} to repay this credit!')


def differentiated_payment(principal, interest, periods, verbose=True):
    current_period = 0
    total_payment = 0
    while current_period < periods:
        current_period += 1
        payment = calculate_differentiated_payment(principal, interest, periods, current_period)
        total_payment += payment
        if verbose:
            print(f'Month {current_period}: payment is {payment}')
    return total_payment


def error(value_1, value_2, value_3, value_4, value_5):
    if value_1 or value_2 or value_3 or value_4 or value_5:
        print('Incorrect parameters')
        sys.exit()

# returns True to trigger error if --interest is None
def check_interest(interest):
    if interest == None:
        return True


# returns True to trigger error if --type is not 'annuity' or 'diff'
def check_type(payment_type):
    if payment_type == 'annuity' or payment_type == 'diff':
        return False
    else:
        return True


# returns True to trigger error if # parameters with a value is == 4
def check_parameters(params):
    counter = 0
    for param in params:
        if param is None:
            pass
        else:
            counter += 1
    if counter == 4:
        return False
    else:
        return True


# returns True if param is less than 0
def check_for_neg(param):
    if param is None:
        return False
    elif int(param) < 0:
        return True
    else:
        return False


# returns True to trigger error if param in params list returns a result in check_for_neg
def check_negs(params):
    for param in params[1:]:
        result = check_for_neg(param)
        if result:
            return True
    return False


# returns True to trigger error if payment_type is 'diff' and payment is not None
def check_diff_payment(payment_type, payment):
    if payment_type == 'diff' and payment != None:
        return True
    else:
        return False


parser = argparse.ArgumentParser()

# required argument
parser.add_argument('--type', type=str, required=True)

#optional arguments
parser.add_argument('--principal', type=float, default=None, help='the value of the credit principal')
parser.add_argument('--payment', type=float, default=None, help='the value of the monthly payment')
parser.add_argument('--periods', type=float, default=None, help='the number of periods to repay the credit')
parser.add_argument('--interest', type=float, default=None, help='the percentage interest on the credit')

args = parser.parse_args()

payment_type = args.type
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest

params = [payment_type, principal, payment, periods, interest]

# check for errors
error(check_interest(interest),
      check_type(payment_type),
      check_parameters(params),
      check_negs(params),
      check_diff_payment(payment_type, payment))

# do the math
if payment_type == 'annuity':
    if principal is None:
        principal = calculate_principal(interest, periods, payment)
        print(f'Your credit principal = {principal}!')
    elif periods is None:
        periods = calculate_months(principal, payment, interest)
        print_months(periods)
    else:
        payment = calculate_annuity_payment(principal, interest, periods)
        print(f'Your annuity payment = {payment}!')
elif payment_type == 'diff':
    if principal is None:
        principal = calculate_principal(interest, periods, payment)
        print(f'Your credit principal = {principal}!')
    elif periods is None:
        periods = calculate_months(principal, payment, interest)
        print_months(periods)
    else:
        differentiated_payment(principal, interest, periods)
total = calculate_total_payment(payment_type, principal, interest, periods)
print(f'Overpayment = {int(total - principal)}')
