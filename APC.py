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

# Calculate total pay
total_pay = regular_pay + overtime_pay + incentive_pay

# Print results
print(f"Regular pay: ${regular_pay:.2f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Incentive pay: ${incentive_pay:.2f}")
print(f"Total pay: ${total_pay:.2f}")

