from datetime import datetime, timedelta

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time) 
  
  def calculate_bill(self, purchased_items):
    total_cost = 0

    for item in purchased_items:
      if item in self.items:
        total_cost += self.items[str(item)]
      else:
        continue
    return total_cost
  pass

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    out_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        out_menus.append(menu.name)
      else:
        continue
    return out_menus
  pass

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises =  franchises
    return
  pass

brunch = Menu("brunch",{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16 )

early_bird = Menu("early bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 15, 18)

dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)

kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

arepas_menu = Menu("Take a Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)

#print(brunch)
#print(early_bird)
#print(dinner)
#print(kids)

brunch_bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print("Brunch: $"+ str(format(brunch_bill, '.2f')))

early_birds_bill = early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])
print("Early Bird: $"+ str(format(early_birds_bill, '.2f')))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

print("Franchise Locations:")
print(" - " + str(flagship_store))
print(" - " + str(new_installment))
print(" - " + str(arepas_place))

basta_fazoolin_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
take_a_arepa_business = Business("Take a Arepa", [arepas_place])

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))
#print(arepas_place.available_menus(17))
print(take_a_arepa_business.franchises)

