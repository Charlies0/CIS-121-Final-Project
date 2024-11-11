
class Room:  
   def __init__(self, name, description, exits):  
      self.name = name  
      self.description = description  
      self.exits = exits  
  
   def __str__(self):  
      return (f"Room: {self.name}\n"  
           f"Description: {self.description}\n"  
           f"Exits: {self.exits}")
