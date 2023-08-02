interest_rate = input(
    "Please enter the interest rate.  Note that you must enter the value as a whole number, for example if the interest rate is 8%, enter 8: "
)
interest_rate = int(interest_rate)
print(interest_rate)
interest_percentage = int(interest_rate) * float(.01)
interest_percentage = float(interest_percentage)
print(interest_percentage)
investment_amount = input(
    "Please enter investment amount, note please enter the value as a whole number, for example, if the investment is $10000 enter 10000: "
)
investment_amount = int(investment_amount)
double = int(2)
goal = int(investment_amount) * int(double)
#print(investment_amount)
george = (investment_amount) * (interest_percentage)
peter = (george) + (investment_amount)
george = int(george)
peter = int(peter)
#print(george)
#print(peter)
current_number = 0
goal2 = int(8)

while (investment_amount) < (goal):
  current_number += 1
  investment_amount += (george)
  george = (investment_amount) * (interest_percentage)

  print(f"\nYear {current_number} return: {investment_amount}")
#test2