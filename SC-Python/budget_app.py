class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []


  def __str__(self):
    budget = self.category.center(30, "*") + "\n"

    for item in self.ledger:
      temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      budget += temp + "\n"

    budget += "Total: " + str(self.get_balance())
    return budget

  def deposit(self, amount, description=""):
    temp = {}
    temp['amount'] = amount
    temp['description'] = description
    self.ledger.append(temp)


  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      temp = {}
      temp['amount'] = 0 - amount
      temp['description'] = description
      self.ledger.append(temp)
      return True
    return False


  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance


  def transfer(self, amount, budget_cat):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_cat.category)
      budget_cat.deposit(amount, "Transfer from " + self.category)
      return True
    return False


  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True


def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  percent = "Percentage spent by category"
  for i in range(100, -1, -10):
    percent += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        percent += " o "
      else:
        percent += "   "
    
    percent += " "
  percent += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    percent += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        percent += " " + categories[j].category[i] + " "
      else:
        percent += "   "
    
    percent += " "

  return percent