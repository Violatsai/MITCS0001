'''
Function that returns the total saving amount over
36 months given the input params
  @param portionSaved: number between 0 and 10000, will
                       be mapped linearly between 0 and 1
  @param annualSalary: integer value of annual salary
  @param annualReturn: annual return rate of investment,
                       float number
  @param semiAnnualRaise: annual raise rate of salary, f-
                          loat number
'''
def getTotalSaving(portionSaved, annualSalary, annualReturn, semiAnnualRaise):
	totalSaving = 0
	for month in range(1,37):
		if month % 6 == 1 and month != 1:
			annualSalary = annualSalary * (1 + semiAnnualRaise)
		else:
			pass
		monthly_savings = (annualSalary / 12) \
		                  * (portionSaved / 10000)
		monthly_investment_return = totalSaving * annualReturn/12
		totalSaving += monthly_savings + monthly_investment_return
	return totalSaving

'''
This progrom calculates the saving portion required
to pay the down payment of a 1M$ house within 36 m-
onths, given the starting annual salary.
The program is divided into three steps:
  (1) Initialization of values
  (2) Iteratively solving for best saving rate
  (3) Output results
'''
# Step 1: Initialization of values
annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
portion_downpayment = 0.25
down_payment = total_cost * portion_downpayment
semi_annual_raise = 0.07
annual_return = 0.04

current_savings = 0
month = 0
num_guesses = 0
possible = True
epsilon = 100
low = 0
high = 10000
portion_saved = (high + low) / 2.0

# Step 2: Iteratively solving for the best saving rate
current_savings = getTotalSaving( \
	                portionSaved = portion_saved,\
	                annualSalary = annual_salary, \
	                annualReturn = annual_return, \
	                semiAnnualRaise = semi_annual_raise )

while abs(current_savings - down_payment) >= epsilon:
	num_guesses += 1
	if current_savings - down_payment > epsilon:
		high = portion_saved
	else:
		low = portion_saved
	portion_saved = (high + low) / 2.0
	current_savings = getTotalSaving( \
  	                    portionSaved = portion_saved,\
	                    annualSalary = annual_salary, \
	                    annualReturn = annual_return, \
	                    semiAnnualRaise = semi_annual_raise )
	# If a valid number cannot be derived after 20 iterations,
	# it is very likely that the down payment is infeasible 
	# given the current salary
	if num_guesses >= 20:
		possible = False
		print ("It is impossible to save for your downpayment within 36 months.")
		break

# Step 3: Output the results
if possible:
	print ("Best savings rate: ", '%.4f' % (portion_saved / 10000))
	print ("Steps in bisection search: ", num_guesses)

