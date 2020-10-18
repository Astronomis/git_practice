teams = []
number_of_teams = input("Number of Teams: ")

teams_range = range(int(number_of_teams))
for num in teams_range:
    teams += str(num)

my_number = 27
my_team = int(my_number) % int(number_of_teams)
print(teams[my_team])

neighbor_1_number = my_number - 1
neighbor_1_team = int(neighbor_1_number) % int(number_of_teams)

neighbor_2_number = my_number + 1
neighbor_2_team = int(neighbor_2_number) % int(number_of_teams)

print(teams[neighbor_1_team])
print(teams[neighbor_2_team])
