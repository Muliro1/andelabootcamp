class BankAccount(object):
	def deposit(self):
		pass
	def withdraw(self):
		pass


class SavingsAccount(BankAccount):
	def __init__(self, balance = 500):
		self.balance = balance
	def deposit_cash(self, amount):
		self.balance += amount
		return self.balance
	def withdraw_cash(self, amount):
		if self.balance - amount < 500:
			return 'cannot withdraw beyond the minimum limit'
		else:
			self.balance -= amount
		return self.balance

