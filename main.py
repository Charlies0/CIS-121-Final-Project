from player import Player  
from monsters import Monster  
from rooms import Room  
  
def main():  
   player = Player()  
   player.name = input("What is your name? ")  
  
   print(f"Hello, {player.name}! Your goal is to rescue the captive trapped in the cave system.")  
   print("You are standing at the entrance of the cave. You see a dark tunnel ahead of you.")  
  
   current_room = Room("Entrance", "You are at the entrance of the cave.", ["North"])  
   rooms = {  
      "Entrance": current_room,  
      "Room1": Room("Room1", "You are in a small room with a chest.", ["South", "East"]),  
      "Room2": Room("Room2", "You are in a room with a kobold.", ["West", "North"]),  
      "Room3": Room("Room3", "You are in a room with an orc.", ["South", "East"]),  
      "Room4": Room("Room4", "You are in a room with a skeleton.", ["West", "North"]),  
      "Room5": Room("Room5", "You are in a room with a chest.", ["South", "East"]),  
      "Room6": Room("Room6", "You are in a room with a kobold.", ["West", "North"]),  
      "Room7": Room("Room7", "You are in a room with an orc.", ["South", "East"]),  
      "Room8": Room("Room8", "You are in a room with a skeleton.", ["West", "North"]),  
      "Room9": Room("Room9", "You are in a room with a chest.", ["South", "East"]),  
      "Room10": Room("Room10", "You are in a room with the captive.", ["West"])  
   }  

   defeated_monsters = []  # Track defeated monsters
   previous_room = None  # Track the previous room

   while True:  
      print(current_room.description)  
      print("Exits: ", current_room.exits)  
  
      action = "fight" if any(monster in current_room.description for monster in ["kobold", "orc", "skeleton"]) else input("What do you want to do? (go, fight, equip, unequip, stats, health) ")  
  
      if action == "go":  
        direction = input("Which direction do you want to go? (North, South, East, West) ")  
        if direction in current_room.exits:  
           previous_room = current_room  # Save the current room before moving
           if direction == "North":
               current_room = rooms["Room2"]
           elif direction == "South":
               current_room = rooms["Room1"]
           elif direction == "East":
               current_room = rooms["Room3"]
           elif direction == "West":
               current_room = rooms["Room4"]
        else:  
           print("You can't go that way.")  
      elif action == "fight":  
        if "kobold" in current_room.description and "kobold" not in defeated_monsters:
            monster = Monster("kobold", 20, 5, 2)  
            print(f"You are fighting a {monster.name}!")  
            while monster.isAlive():  
               print(f"Monster's health: {monster.health}")  
               action = input("What do you want to do? (attack, run) ")  
               if action == "attack":  
                  damage = player.getAttack()  
                  monster.applyIncomingDamage(damage)  
                  if not monster.isAlive():  
                    defeated_monsters.append("kobold")
                    print(f"You killed the {monster.name}!")  
                    player.health = 100  
                    print(f"Your health is restored to {player.health}.")  
                    break  # Exit the fight loop
               elif action == "run":  
                  print("test")
                  break  
        elif "orc" in current_room.description and "orc" not in defeated_monsters:
            monster = Monster("orc", 25, 7, 3)  
            print(f"You are fighting a {monster.name}!")  
            while monster.isAlive():  
               print(f"Monster's health: {monster.health}")  
               action = input("What do you want to do? (attack, run) ")  
               if action == "attack":  
                  damage = player.getAttack()  
                  monster.applyIncomingDamage(damage)  
                  if not monster.isAlive():  
                    defeated_monsters.append("orc")
                    print(f"You killed the {monster.name}!")  
                    player.health = 100  
                    print(f"Your health is restored to {player.health}.")  
                    break  # Exit the fight loop
               elif action == "run":  
                  print("You cannot run away from the fight!")  
        elif "skeleton" in current_room.description and "skeleton" not in defeated_monsters:
            monster = Monster("skeleton", 15, 4, 1)  
            print(f"You are fighting a {monster.name}!")  
            while monster.isAlive():  
               print(f"Monster's health: {monster.health}")  
               action = input("What do you want to do? (attack, run) ")  
               if action == "attack":  
                  damage = player.getAttack()  
                  monster.applyIncomingDamage(damage)  
                  if not monster.isAlive():  
                    defeated_monsters.append("skeleton")
                    print(f"You killed the {monster.name}!")  
                    player.health = 100  
                    print(f"Your health is restored to {player.health}.")  
                    break  # Exit the fight loop
               elif action == "run":  
                  print("test")
                  current_room = previous_room 
        else:
            print("The room is empty.")
            
      elif action == "equip":  
        item = input("What do you want to equip? (weapon, armor) ")  
        if item == "weapon":  
           weapon_name = input("What is the name of the weapon? ")  
           player.equipWeapon(weapon_name)  
        elif item == "armor":  
           armor_name = input("What is the name of the armor? ")  
           player.equipArmor(armor_name)  
      elif action == "unequip":  
        item = input("What do you want to unequip? (weapon, armor) ")  
        if item == "weapon":  
           player.unequipWeapon()  
        elif item == "armor":  
           player.unequipArmor()  
      elif action == "stats":  
        print(player)  
      elif action == "health":  
        print(f"Your health is {player.health}.")  
      else:  
        print("Invalid action.")  
  
if __name__ == "__main__":  
   main()
