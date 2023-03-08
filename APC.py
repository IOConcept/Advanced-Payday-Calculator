hourly_rate = float(input("Enter your hourly rate: "))
overtime_rate = 1.5 * hourly_rate
incentive_rate = 4.0

non_overtime_hours = float(input("Enter the number of non-overtime hours worked: "))
overtime_hours = float(input("Enter the number of overtime hours worked: "))
incentive_percent = float(input("Enter the percentage of hours eligible for incentive pay (e.g. 10 for 10%): "))

total_hours = non_overtime_hours + overtime_hours
incentive_hours = total_hours * (incentive_percent / 100)
regular_pay = non_overtime_hours * hourly_rate
overtime_pay = overtime_hours * overtime_rate
incentive_pay = incentive_hours * incentive_rate
total_pay = regular_pay + overtime_pay + incentive_pay

print("Regular pay for non-overtime hours: ${:.2f}".format(regular_pay))
print("Overtime pay for overtime hours: ${:.2f}".format(overtime_pay))
print("Incentive pay for eligible hours: ${:.2f}".format(incentive_pay))
print("Total pay: ${:.2f}".format(total_pay))
