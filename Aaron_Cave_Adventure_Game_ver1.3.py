
import random  
  
class Character:  
   def __init__(self, name, health, attack, defense, has_weapon, has_armor):  
      self.name = name  
      self.health = health  
      self.attack = attack  
      self.defense = defense  
      self.has_weapon = has_weapon  
      self.has_armor = has_armor  
  
class Room:  
   def __init__(self, description, monster=None):  
      self.description = description  
      self.monster = monster  
  
class Game:  
   def __init__(self):  
      self.player = None  
      self.rooms = [  
        Room("You are at the entrance of the cave."),  
        Room("You are in a dark room."),  
        Room("You are in a room with a Kobold.", monster="Kobold"),  
        Room("You are in a room with a chest."),  
        Room("You are in a room with an Orc.", monster="Orc"),  
        Room("You are in a room with a Skeleton.", monster="Skeleton"),  
        Room("You are in a room with a door."),  
        Room("You are in a room with the captive.", monster="Captive")  
      ]  
      self.current_room = 0  
      self.health_potions = 0  
  
   def start_game(self):  
      player_name = input("What is your character's name? ")  
      self.player = Character(player_name, 10, 2, 1, True, False)  
      print(f"Welcome, {player_name}! You are at the entrance of the cave. Your goal is to rescue the captive being held in the cave.")  
      self.play_game()  
  
   def play_game(self):  
      while True:  
        print(self.rooms[self.current_room].description)  
        if self.rooms[self.current_room].monster:  
           monster = self.rooms[self.current_room].monster  
           if monster == "Kobold":  
              monster_health = 5  
              monster_attack = 1  
              monster_defense = 1  
           elif monster == "Orc":  
              monster_health = 10  
              monster_attack = 2  
              monster_defense = 2  
           elif monster == "Skeleton":  
              monster_health = 15  
              monster_attack = 3  
              monster_defense = 3  
           elif monster == "Captive":  
              print("You rescued the captive! Congratulations, you won!")  
              break  
           while monster_health > 0:  
              print(f"{monster} health: {monster_health}")  
              action = input("What do you do? (attack/run) ")  
              if action == "attack":  
                attack_roll = random.randint(1, 6)  
                if attack_roll >= 3 - monster_defense:  
                   damage = 1  
                   monster_health -= damage  
                   print(f"You hit the {monster} for {damage} damage!")  
                else:  
                   print("Your attack was blocked!")  
                if monster_health > 0:  
                   monster_attack_roll = random.randint(1, 6)  
                   if monster_attack_roll >= 3 - self.player.defense:  
                      damage = 1  
                      self.player.health -= damage  
                      print(f"The {monster} hit you for {damage} damage!")  
                      print(f"Your health is now {self.player.health}.")  
                   else:  
                      print("The monster's attack was blocked!")  
              elif action == "run":  
                print("You ran away!")  
                break  
           if monster_health <= 0:  
              print(f"You defeated the {monster}!")    
              if self.player.health < 10:  
                self.player.health = 10  
                print(f"You found a health potion and used it, your health is now {self.player.health}.")  
        if self.player.health <= 0:  
           print("You died! Game over.")  
           break  
        direction = input("Which direction do you want to go? (north/south/east/west) ")  
        if direction == "north" and self.current_room > 0:  
           self.current_room -= 1  
        elif direction == "south" and self.current_room < len(self.rooms) - 1:  
           self.current_room += 1  
        elif direction == "east" and self.current_room % 2 == 0:  
           self.current_room += 1  
        elif direction == "west" and self.current_room % 2 == 1:  
           self.current_room -= 1  
        else:  
           print("You can't go that way!")  
  
game = Game()  
game.start_game()
