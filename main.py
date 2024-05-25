#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $")) #make this a float since some bill totals will have decimals.

tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) #make this an int since it will be a whole number

tip_percent_shortcut = tip / 100 + 1 #shortcut to convert tip to a percentage

bill_with_tip = bill * tip_percent_shortcut #multiply the bill by the tip percentage

people = int(input("How many people to split the bill? ")) #make this an int since we need to divide the bill by the number of people

bill_per_person = bill_with_tip / people #divide the bill by the number of people

final_amount = "{:.2f}".format(bill_per_person) #round the bill per person to 2 decimal places
print(f"Each person should pay: ${final_amount}")