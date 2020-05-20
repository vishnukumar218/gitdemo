class user:
	def __init__ (self, Email):
		self.Email = Email


	def sign_in(self):
		print('logged in')

	def attack(self):
		print('dont do anything')

class Wizard(user):
	def __init__ (self, Name, Power, Email):
		super().__init__(Email)
		self.Name = Name
		self.Power = Power

	def attack(self): 
		user.attack(self)
		print(f'attacking with the power of {self.Power}')


class Archer(user):
	def __init__ (self, Name, Num_Arrows):
		self.Name = Name
		self.Num_Arrows = Num_Arrows

	def attack(self):
		print(f'attacking with the power: arrows-left {self.Num_Arrows}')




Archer1 = Archer('kumar', 100)
Wizard1 = Wizard('vishnu', 50, 'vishnukumar218@gmail.com')

#for char in [Wizard1, Archer1]:
#	char.attack()


