annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

current_savings = 0
month = 0
portion_downpayment = 0.25
annual_return = 0.04

downpayment = total_cost*portion_downpayment
monthly_savings = annual_salary/12*portion_saved

while current_savings <= downpayment:
	monthly_investment_return = current_savings*annual_return/12
	current_savings += monthly_savings + monthly_investment_return
	month += 1
print ("Number of months: " + str(month))