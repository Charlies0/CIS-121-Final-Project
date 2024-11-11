class Monster:  
   def __init__(self, name, health, baseAttack, baseDefense):  
      self.name = name  
      self.health = health  
      self.baseAttack = baseAttack  
      self.baseDefense = baseDefense  
  
   def applyIncomingDamage(self, incomingDamage):  
      totalDefense = self.baseDefense  
      damageTaken = max(0, incomingDamage - totalDefense)  
      self.health -= damageTaken  
      return self.health  
  
   def isAlive(self):  
      if self.health > 0:  
        return True  
      else:  
        print(f"The {self.name} died.")  
        return False  
  
   def __str__(self):  
      return (f"Monster Stats:\n"  
           f"Health: {self.health}\n"  
           f"Attack: {self.baseAttack}\n"  
           f"Defense: {self.baseDefense}")
