#Prices
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

# Descriptions
lovely_loveseat_description = """
Lovely Loveseat: 
Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
""" + str(lovely_loveseat_price)

stylish_settee_description = """
Stylish Settee: 
Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
""" + str(stylish_settee_price)

luxurious_lamp_description = """
Luxurious Lamp: 
Glass and iron. 36 inches tall. Brown with cream shade.
""" + str(luxurious_lamp_price)



#Tax
sales_tax = .088

# Items total cost
customer_one_total = 0

#Items description
customer_one_itemization = []

# Customer One Actions
customer_one_total += lovely_loveseat_price
customer_one_itemization.append(lovely_loveseat_description)
customer_one_total += luxurious_lamp_price
customer_one_itemization.append(luxurious_lamp_description)

# Log pretax total
customer_one_no_tax_total = customer_one_total
# Calculate total with tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Print receipt
print("Customer One Items:")
for item in customer_one_itemization:
  print(item)
print("Customer One Total:")
print("  Item cost: " + "       $" + str(format(customer_one_no_tax_total, '.2f')))
print("  Sales Tax(8.88%): $" + str(format(customer_one_tax, '.2f')))
print("______________________________")
print("      Total:        $" + str(format(customer_one_total, '.2f')))
