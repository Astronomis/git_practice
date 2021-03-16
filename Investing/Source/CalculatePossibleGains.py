#What Do I want this thing to do?
# 1. Take input of the investing price
# 2. Take input of current stock value
# 3. Take input of goal stock sell value
# 4. Calculate interval sell points and possible gains
# 5. Calculate possible gains for selling at goal price point

###Planned improvements after base development
# 1. Log last run info for reopening session
# 2. Create storage to track investment gains and losses over time
# 3. Monitor progress from all accounts
# 4. Learn to work with APIs and be able to pull data from stock market to automate daily changes.

#Stock node, used to:
#Get information on the investment, current value, goal value, and return the information.
#Calculate what the profit would be if the stock met your goal value.
#Provide amount of shares owned.

class Stock:
    def __init__(self, investment):
        self.investment = investment
        self.stocks = []
        self.zone_count = 1

#    def __repr__(self):
#        return "You are investing $" + str(self.investment) + " at a value of $" + str(self.current_value) + " with a goal of selling at $" + str(self.goal_value) + "."    

##ADD TO CLASS##
    def AddCurrentValue(self, current_value):
        self.current_value = current_value

    def AddGoalValue(self, goal_value):
        self.goal_value = goal_value

#GET FROM CLASS##
    def GetCurrentValue(self):
        return self.current_value

    def GetGoalValue(self):
        return self.goal_value

    def GetInvestment(self):
        return self.investment
##GET NEW INFO 
    def GetStockCount(self, investment, current_value):
        self.stock_count = float(float(investment)/float(current_value))
        return str(self.stock_count)
    
    def GetStockSellPoints(self, current_value, goal_value, sell_point_count):
        diff_value = float(goal_value) - float(current_value)
        quarter_diff_value = float(diff_value) / int(sell_point_count)
        interval = float(current_value)
        print("Stock Selling Points: ")
        zone_count = int(sell_point_count) - 1
        for i in range(zone_count):
            interval += float(quarter_diff_value)
            stock_count = self.GetStockCount(self.investment, self.current_value)
            print( "    $" + str(interval) + " = $" + str(float(interval) * float(stock_count)))
    23123
    def GetStockGoal(self):
        return (float(self.investment)/float(self.current_value))*float(goal_value)


investment_amount = input("Investment: ")
stock = Stock(investment_amount) 
current_value = input("Current Value: ")
stock.AddCurrentValue(current_value) 
goal_value = input("Goal Value: " )
stock.AddGoalValue(goal_value)
stock_count = stock.GetStockCount(investment_amount,current_value)

print("Please input the amount of different possible gains you would like to see.")
sell_point_count = input("Sell Zone Count: ")

print("Inputed Values:")
print("  Investment    : $" + str(investment_amount))
print("  Current Value : $" + str(current_value))
print("  Goal Value    : $" + str(goal_value))
print("")
print("Output Information:")
print("  Shares        :  " + str(stock_count))
print("")
stock.GetStockSellPoints(current_value, goal_value, sell_point_count)
goal_value = stock.GetStockGoal()