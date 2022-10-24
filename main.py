name_of_recipient = input(("Who is reciving this paycheck? "))

while True:
    try:
        hourly_rate = int(input("What is your hourly rate? "))
        hours_worked = float(input("How many hours did they work this week? "))

        def regular_pay(hourly_rate, hours_worked):
            pay = hourly_rate * hours_worked
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


        print(f"Employee name: {name_of_recipient}")
        print(f"Hourly rate is: ${hourly_rate}")
        print(f"Hours worked: {hours_worked}")
        print(f"Regular pay: ${regular_pay(hourly_rate, hours_worked)}")
        print(f"Gross pay: ${gross_pay(hourly_rate, hours_worked)}")
        print(f"Federal tax: ${fed_tax(hourly_rate, hours_worked)}")
        print(f"State tax: ${state_tax(hourly_rate, hours_worked)}")
        print(f"FICA tax: ${fica_tax(hourly_rate, hours_worked)}")
        print(f"Total tax: ${total_tax(hourly_rate, hours_worked)}")
        print(f"Net pay: ${net_pay(hourly_rate, hours_worked)}")
    except ValueError:
        print("Invalid input, please enter a number between 1 and 168")
        continue
    else:
        break
