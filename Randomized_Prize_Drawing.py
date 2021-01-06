# Import random below:
import random

# Create random_list below:
employees = ['Barb','John','David','Jeremy','Nhavid','Taylor','Lay','Sokhom','Sopheak','Jeanne']
random_list = [random.randint(1,len(employees)) for employee in employees]
print(random_list)
# Create randomer_number below:
randomer_number = random.choice(random_list)
winner = employees[randomer_number - 1]

# Print randomer_number below:
print(randomer_number)
print(winner)
