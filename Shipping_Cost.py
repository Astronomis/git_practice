#Flat charge
ground_flat_charge = 20.00
drone_flat_charge = 0.00
premium_shipping_charge = 125.00

#Calculate cost of ground shipping
def ground_shipping_cost(weight):
  if weight < 2:
    price_per_pound = 1.50
  elif (weight > 2) and (weight <= 6):
    price_per_pound =  3.00
  elif (weight > 6) and (weight <= 10):
    price_per_pound =  4.00
  elif weight > 10:
    price_per_pound =  4.75
  cost = weight * price_per_pound + ground_flat_charge
  return cost

def drone_shipping_cost(weight):
  if weight < 2:
    price_per_pound = 4.50
  elif (weight > 2) and (weight <= 6):
    price_per_pound =  9.00
  elif (weight > 6) and (weight <= 10):
    price_per_pound = 12.00
  elif weight > 10:
    price_per_pound =  14.25
  cost = weight * price_per_pound + drone_flat_charge
  return cost

def best_shipping_method(weight):
  ground_shipping = ground_shipping_cost(weight)
  drone_shipping = drone_shipping_cost(weight)
  
  if (ground_shipping < drone_shipping) and (ground_shipping < premium_shipping_charge):
    return "Ground is the cheapest shipping method. It will cost $"+str(ground_shipping)+" to ship."
  elif (drone_shipping < ground_shipping) and (drone_shipping < premium_shipping_charge):
    return "Drone is the cheapest shipping method. It will cost $"+str(drone_shipping)+" to ship."
  elif (premium_shipping_charge < ground_shipping) and (premium_shipping_charge < drone_shipping):
    return "Premium will be your cheapest shipping method. It will cost $125.00 to ship"

print(ground_shipping_cost(8.4))
print(drone_shipping_cost(1.5))
print(best_shipping_method(4.8))
print(best_shipping_method(41.5))
