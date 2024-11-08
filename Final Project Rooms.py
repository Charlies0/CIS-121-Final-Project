# Create parameters with the constructor and set instance attributes
class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

	# Call for an exit and get the direction.
    def get_exit(self, direction):
        return self.exits.get(direction)

# Initialize rooms
rooms = {
    'R1': Room("R1", "You are in Room 1.", {'East': 'R2'}),
    'R2': Room("R2", "You are in Room 2.", {'South': 'R3', 'West': 'R1'}),
    'R3': Room("R3", "You are in Room 3.", {'North': 'R2', 'South': 'R5', 'East': 'R4'}),
    'R4': Room("R4", "You are in Room 4.", {'West': 'R3'}),
    'R5': Room("R5", "You are in Room 5.", {'North': 'R3'}),
}

current_room = rooms['R1']



'''
# Define the rooms as a dictionary
rooms = {
    'R1': {'East': 'R2'},
    'R2': {'South': 'R3', 'West': 'R1'},
    'R3': {'North': 'R2', 'South': 'R5', 'East': 'R4'},
    'R4': {'West': 'R3'},
    'R5': {'North': 'R3'}
}

current_room = 'R1'

# Game loop
while True:
    print(f"You are in room {current_room}")
    print("Available directions:", ', '.join(rooms[current_room].keys()))
    
    # Ask for user input
    direction = input("Enter direction (or 'quit' to exit): ").capitalize()
    
    if direction == 'Quit':
        print("Thanks for playing!")
        break
    elif direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("You can't go that way.")

# Game loop
while True:
    print(f"You are in {current_room.name}. {current_room.description}")
    print("Available directions:", ', '.join(current_room.exits.keys()))
    
    # Ask for user input
    direction = input("Enter direction (or 'quit' to exit): ").capitalize()
    
    if direction == 'Quit':
        print("Thanks for playing!")
        break
    else:
        next_room_name = current_room.get_exit(direction)
        if next_room_name:
            current_room = rooms[next_room_name]
        else:
            print("You can't go that way.")
'''
