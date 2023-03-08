# Get user input
while True:
    try:
        hourly_rate = float(input("Enter hourly rate: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for hourly rate.")

while True:
    try:
        non_overtime_hours = float(input("Enter number of non-overtime hours worked: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for non-overtime hours worked.")

while True:
    try:
        overtime_hours = float(input("Enter number of overtime hours worked: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for overtime hours worked.")

while True:
    try:
        incentive_percentage = float(input("Enter percentage of eligible hours for incentive pay: "))
        if incentive_percentage < 0 or incentive_percentage > 100:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100 for the incentive percentage.")

while True:
    try:
        incentive_pay = float(input("Enter incentive pay value: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for incentive pay value.")

# Calculate regular pay, overtime pay, and incentive pay
regular_pay = hourly_rate * non_overtime_hours
overtime_pay = hourly_rate * 1.5 * overtime_hours
eligible_hours = (non_overtime_hours + overtime_hours) * (incentive_percentage / 100)
incentive_pay = eligible_hours * incentive_pay

# Calculate gross pay
gross_pay = regular_pay + overtime_pay + incentive_pay

# Calculate the deductions
federal_tax_rate = 0.18
state_tax_rate = 0.05
social_security_tax_rate = 0.10
medicare_tax_rate = 0.03

federal_tax = gross_pay * federal_tax_rate
state_tax = gross_pay * state_tax_rate
social_security_tax = gross_pay * social_security_tax_rate
medicare_tax = gross_pay * medicare_tax_rate

total_deductions = federal_tax + state_tax + social_security_tax + medicare_tax

# Calculate the net pay
net_pay = gross_pay - total_deductions

# Display the results
print(f"Regular pay: ${regular_pay:.2f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Incentive pay: ${incentive_pay:.2f}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Federal tax: ${federal_tax:.2f}")
print(f"State tax: ${state_tax:.2f}")
print(f"Social Security tax: ${social_security_tax:.2f}")
print(f"Medicare tax: ${medicare_tax:.2f}")
print(f"Total deductions: ${total_deductions:.2f}")
print(f"Net pay: ${net_pay:.2f}")
