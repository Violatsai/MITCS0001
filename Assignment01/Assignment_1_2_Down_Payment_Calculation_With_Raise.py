annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))
current_savings = 0
month = 0
portion_downpayment = 0.25
annual_return = 0.04

downpayment = total_cost*portion_downpayment

while current_savings <= downpayment:
	if month%6 == 1 and month != 1:
		annual_salary = annual_salary*(1+semi_annual_raise)
	else:
		pass
	monthly_savings = annual_salary/12*portion_saved
	monthly_investment_return = current_savings*annual_return/12
	current_savings += monthly_savings + monthly_investment_return
	month += 1
print ("Number of months: " + str(month))