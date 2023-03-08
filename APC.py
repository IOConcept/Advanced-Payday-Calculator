# Get user input
hourly_rate = float(input("Enter hourly rate: "))
non_overtime_hours = float(input("Enter number of non-overtime hours worked: "))
overtime_hours = float(input("Enter number of overtime hours worked: "))
incentive_percentage = float(input("Enter percentage of eligible hours for incentive pay: "))
incentive_pay_value = float(input("Enter incentive pay value: "))

# Calculate regular pay, overtime pay, and incentive pay
regular_pay = hourly_rate * non_overtime_hours
overtime_pay = hourly_rate * 1.5 * overtime_hours
eligible_hours = (non_overtime_hours + overtime_hours) * (incentive_percentage / 100)
incentive_pay = eligible_hours * incentive_pay_value

# Calculate total pay
total_pay = regular_pay + overtime_pay + incentive_pay

# Print results
print(f"Regular pay: ${regular_pay:.2f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Incentive pay: ${incentive_pay:.2f}")
print(f"Total pay: ${total_pay:.2f}")

