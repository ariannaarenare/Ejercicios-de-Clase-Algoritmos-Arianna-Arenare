deposit = float(input("how much money do you will to deposit?: "))
profit = deposit * 0.04
year1 = deposit + profit
profit = year1 * 0.04
year2 = year1 + profit
profit = year2 * 0.04
year3 = year2 + profit
print(f"In first year you will earn{round{year1}}")
