# A script to determine the paycheck information for a given employee:



def regular_pay(hourly_rate, hours_worked):
    pay = hourly_rate * hours_worked
    return pay

def overtime_pay(hourly_rate, hours_worked):
    pay = 1.5 * hourly_rate * (hours_worked - 40)
    return pay

def gross_pay(hourly_rate, hours_worked):
    if hours_worked <= 40:
        pay = hourly_rate * hours_worked
    else:
        pay = (hourly_rate * 40) + (1.5 * hourly_rate * (hours_worked - 40))
    return pay

def fed_tax(hourly_rate, hours_worked):
    return (gross_pay(hourly_rate, hours_worked) * .15)

def state_tax(hourly_rate, hours_worked):
    return (gross_pay(hourly_rate, hours_worked) * .10)

def fica_tax(hourly_rate, hours_worked):
    return (gross_pay(hourly_rate, hours_worked) * .02)

def total_tax(hourly_rate, hours_worked):
    return (fed_tax(hourly_rate, hours_worked)) + (state_tax(hourly_rate, hours_worked)) + (
        fica_tax(hourly_rate, hours_worked))

def net_pay(hourly_rate, hours_worked):
    return (gross_pay(hourly_rate, hours_worked)) - (total_tax(hourly_rate, hours_worked))


name_of_recipient = input(("Who is receiving this paycheck? "))

while True:
    try:
        hourly_rate = float(input("What is their hourly rate? "))
    except ValueError:
        print("Invalid input, please enter a number")
        continue
    else:
        break

while True:
    try:
        hours_worked = float(input("How many hours did they work this week? "))
    except ValueError:
        print("Invalid input, please enter a number between 0 and 168")
        continue
    if hours_worked < 0:
        print("Invalid input, please enter a number between 0 and 168")
    elif hours_worked > 168:
        print("Invalid input, please enter a number between 0 and 168")
    else:
        break



print(f"Employee name: {(name_of_recipient)}")
print(f"Hourly rate is: ${(hourly_rate)}")
print(f"Hours worked: {(hours_worked)}")
print(f"Regular pay: ${round(regular_pay(hourly_rate, hours_worked),2)}")
print(f"Overtime pay: ${round(overtime_pay(hourly_rate, hours_worked),2)}")
print(f"Gross pay: ${round(gross_pay(hourly_rate, hours_worked),2)}")
print(f"Federal tax: ${round(fed_tax(hourly_rate, hours_worked),2)}")
print(f"State tax: ${round(state_tax(hourly_rate, hours_worked),2)}")
print(f"FICA tax: ${round(fica_tax(hourly_rate, hours_worked),2)}")
print(f"Total tax: ${round(total_tax(hourly_rate, hours_worked),2)}")
print(f"Net pay: ${round(net_pay(hourly_rate, hours_worked),2)}")

