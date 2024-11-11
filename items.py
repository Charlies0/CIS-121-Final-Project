class Weapon:
	def __init__(self, name, attackMultiplier):
		self.name = name                          # Name of the weapon (ex. Beat Sword)
		self.attackMultiplier = attackMultiplier  # Multiplier applied to base attack

	def calculateAttackBonus(self, baseAttack):
		# Calculate and return final attack power
		return baseAttack * self.attackMultiplier


class Armor:
	def __init__(self, name, defenseMultiplier):
		self.name = name
		self.defenseMultiplier = defenseMultiplier

	def calculateDefenseBonus(self, baseDefense):
		return baseDefense * self.defenseMultiplier  # Multiplier applied to base defense


class Items:
	def __init__(self):
		self.weapons = {
			"beat_sword": Weapon("Beat Sword", 1.5)      # Creates beat sword with 1.5 attk pwr
			# Add more weapons here "": Weapon("", )
		}
		self.armors = {
			"leather_armor": Armor("Leather Armor", 1.1) # Creates leather armour with 1.1 boosted def
			# Add more armour here  "": Armor("", )
		}
		self.equippedWeapon = None # Tracks currently equipped Weapon
		self.equippedArmor = None

	def equipWeapon(self, weaponName):
		# Eqips a weapon by name if it exists in the weapon dictionary
		if weaponName in self.weapons:
			self.equippedWeapon = self.weapons[weaponName] # Set chosen weapon as equipped
			print(f"Equipped {weaponName} with {self.equippedWeapon.attackMultiplier}x attack multiplier.")
		else:
			print(f"{weaponName} not found in weapons.")

	def equipArmor(self, armorName):
		# Equip armor if available in armors dictionary
		if armorName in self.armors:
			self.equippedArmor = self.armors[armorName]
			print(f"Equipped {armorName} with {self.equippedArmor.defenseMultiplier}x defense multiplier.")
		else:
			print(f"{armorName} not found in armors.")

	def unequipWeapon(self):
		# Unequip the current weapon
		if self.equippedWeapon:
			print(f"Unequipped {self.equippedWeapon.name}")
			self.equippedWeapon = None
		else:
			print(f"No weapon to unequip.")

	def unequipArmor(self):
		# Unequip the current armor
		if self.equippedArmor:
			print(f"Unequipped {self.equippedArmor.name}")
			self.equippedArmor = None
		else:
			print(f"No armor to unequip.")


	def getAttackBonus(self, baseAttack):
		if self.equippedWeapon:
			return self.equippedWeapon.calculateAttackBonus(baseAttack)
		return baseAttack

	def getDefenseBonus(self, baseDefense):
		if self.equippedArmor:
			return self.equippedArmor.calculateDefenseBonus(baseDefense)
		return baseDefense
