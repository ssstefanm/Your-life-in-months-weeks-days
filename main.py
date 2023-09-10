# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# 1 year= 356 days , 52 weeks, 12 months

int_age= int(age)
years_left= 90 - int_age
months_left= 90*12 - int_age*12
weeks_left=90*52 - int_age*52
days_left=90*365 - int_age*365
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")




