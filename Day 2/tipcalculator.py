#bill of £150 with 12% tip split between 5 people

bill = float(input("Waht was the bill? "))
tip_percent = int(input("What percentage tip do you want to give? "))
people = int(input("How many people are splitting the bill? "))

tip_as_percent = tip_percent/100
total_tip_amount = bill*tip_as_percent
total_bill = bill + total_tip_amount
billperperson = total_bill/people
final_amount = round(billperperson, 2)

print(final_amount)