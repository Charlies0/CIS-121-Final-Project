from items import Items

class Player():
	def __init__(self):
		# self.name = name # Add name argument when ready
		self.health = 100
		self.baseAttack = 10
		self.baseDefense = 5
		self.items = Items()


# Equips weapons through item class
	def equipWeapon(self, weaponName):
		self.items.equipWeapon(weaponName)

# Equips armor
	def equipArmor(self, armorName):
		self.items.equipArmor(armorName)

	def unequipWeapon(self):
		self.items.unequipWeapon()
		
	def unequipArmor(self):
		self.items.unequipArmor()


	def getAttack(self):
		# Calculate total attack, factoring in any equipped weapon
		return self.items.getAttackBonus(self.baseAttack)
	
	def applyIncomingDamage(self, incomingDamage):
		# Calculate effective defense with equipped armor, then apply damage
		totalDefense  = self.items.getDefenseBonus(self.baseDefense)
		damageTaken = max(0, incomingDamage - totalDefense)			#Returns damage taken ensuring health does not pass zero
		self.health -= damageTaken
		return self.health


	def isAlive(self):
		# Check if the player is still alive
		if self.health > 0:
			return True
		else:
			print (f'You died, better luck next time....')
			return False
			
# Overload Player function
	def __str__(self):
		return (f"Player Stats:\n"
				f"Health: {self.health}\n"
				f"Attack: {self.getAttack()}\n"
				f"Defense: {self.items.getDefenseBonus(self.baseDefense)}")
