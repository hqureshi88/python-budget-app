import math

class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description = ""):
    self.ledger.append({
      "amount": amount,
      "description": description
    })
  
  def withdraw(self, amount, description = ""):
    accept_withdraw = self.check_funds(amount)
    if not accept_withdraw:
      pass
      return False
    else:
      self.ledger.append({
        "amount": -amount,
        "description": description
      })
      return True
  
  def get_balance(self):
    total_budget = 0
    for item in self.ledger:
      total_budget += item["amount"]
    return total_budget

  def transfer(self, amount, budget_category):
    accept_withdraw = self.check_funds(amount)
    if not accept_withdraw:
      pass
      return False
    else:
      self.ledger.append({
        "amount": -amount,
        "description": "Transfer to " + budget_category.category
      })
      budget_category.deposit(amount, "Transfer from " + self.category) 
      return True 
  
  def check_funds(self, amount):
    total_check = 0
    for item in self.ledger:
      total_check += item["amount"]
    if amount > total_check:
      return False
    else:
      return True

  def __str__(self):
    output = ""
    chars = "*"*30
    category = self.category
    length = int((len(chars) - len(category))/2)
    char_star = "*"*length
    title = char_star + category + char_star + '\n'
    output += title
    for item in self.ledger:
      desc = item["description"][:23]
      desc = desc.ljust(23, ' ')
      amount = "{:.2f}".format(item["amount"])
      amount = amount.rjust(7,' ')
      line = desc + amount + '\n'
      output += line
    total = "{:.2f}".format(self.get_balance())
    output += "Total: " + total 
    return output

def create_spend_chart(categories):

  total_spend = 0
  category_totals = [] 
  for category in categories:
    category_total_withdrawn = 0
    for num in category.ledger:
      if num['amount'] < 0:
        total_spend += num['amount']
        category_total_withdrawn += num['amount']
    category_totals.append(category_total_withdrawn)

  for i in range(len(category_totals)):
    category_totals[i] = math.floor(((category_totals[i]/total_spend)*100)/10)*10

  graph = "Percentage spent by catergory\n"
  graph += "100|"
  for i in range(90, -1, -10):
    if len(str(i)) == 1:
      temp = "          \n  " + str(i) + "| "
      for j in range(len(category_totals)):
        if category_totals[j] >= i:
          temp += "o  "
      graph += temp
    else:
      temp = "         \n " + str(i) + "| "
      for j in range(len(category_totals)):
        if category_totals[j] >= i:
          temp += "o  "
      graph += temp
  graph += "\n    _"
  
  for i in range(len(categories)):
    graph += "___"
    if i == len(categories)-1:
      graph += "\n    "
  
  max_val = 0
  for word in categories:
    temp_val = len(word.category)
    if max_val < temp_val:
      max_val = temp_val
   
  for num in range(max_val):
    temp = " "
    x = 0  
    for category in categories:
      if x < len(categories)-1:
        if num <= len(category.category)-1:
          temp += category.category[num] + "  "
        else:
          temp += "   "
      elif x >= len(categories)-1:
        if num <= len(category.category)-1:
          temp += category.category[num] + "\n    "
        else:
          temp += "\n    "
      x += 1
    graph += temp
  return graph
  
  total_spend = "{:.2f}".format(total_spend)
  return total_spend
