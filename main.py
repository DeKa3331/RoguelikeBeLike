import random

class Monster:
    Type = ["boss", "weakMonster", "strongMonster"]

    def __init__(self, power, type, dmgdealt, goldDrop):
        self.power = power
        self.type = type
        self.dmgdealt = dmgdealt
        self.goldDrop = goldDrop


Goblin = Monster(2, "weakMonster", 1, 3)
Hydra = Monster(20, "strongMonster", 8, 15)
Dragon = Monster(100, "boss", 15, 0)



class Field:
    def __init__(self, name, field_type, monster, adjacent_fields,is_fountain_used=False):
        self.name = name
        self.type = field_type
        self.monster = monster
        self.adjacent_fields = adjacent_fields
        self.is_fountain_used = is_fountain_used

    def __str__(self):
        return f"Pole: {self.name}"




    def respawn_monster(self):
        if random.uniform(0, 100) <= 85:
            if self.type == "Goblin Hatchery":
                self.monster = Goblin
                print(f"A Goblin respawned on field {self.name}")
            elif self.type == "Hydra Hatchery":
                self.monster = Hydra
                print(f"A Hydra respawned on field {self.name}")

A1 = Field("A1", "Start", None, {})
B1 = Field("B1", "Goblin Hatchery", Goblin, {})
B2 = Field("B2", "Goblin", Goblin, {})
B3 = Field("B3", "Empty", None, {})
B4 = Field("B4", "Shop", None, {})
C1 = Field("C1", "Empty", None, {})
D1 = Field("D1", "Hydra", Hydra, {})
D2 = Field("D2", "Hydra Hatchery", Hydra, {})
D3 = Field("D3", "Fountain",None , {})
D4 = Field("D4", "Boss", Dragon, {})

A1.adjacent_fields = {"up": B4}
B4.adjacent_fields = {"left": B3, "down": A1}
B3.adjacent_fields = {"left": B2, "right": B4}
B2.adjacent_fields = {"left": B1, "right": B3}
B1.adjacent_fields = {"up": C1, "right": B2}
C1.adjacent_fields = {"up": D1, "down": B1}
D1.adjacent_fields = {"right": D2, "down": C1}
D2.adjacent_fields = {"left": D1, "right": D3}
D3.adjacent_fields = {"left": D2, "right": D4}
D4.adjacent_fields = {"left": D3}




class Shop:
    def __init__(self):
        self.items = {
            "Dagger": {"power": 4, "cost": 4, "max_stock": 3, "stock": 3},
            "Sword": {"power": 7, "cost": 6, "max_stock": 5, "stock": 5},
            "Throwing Knife": {"power": 20, "cost": 16, "max_stock": 6, "stock": 6},
        }

    def buy_item(self, player, item_name):
        if item_name in self.items:
            item = self.items[item_name]
            if item["stock"] > 0:
                if player.gold >= item["cost"]:
                    player.power += item["power"]
                    player.gold -= item["cost"]
                    item["stock"] -= 1
                    print(f"You bought {item_name}! Now your power increased to {player.power}.")
                    print(f"Remaining gold: {player.gold}. Remaining stock {item_name}: {item['stock']}.")
                else:
                    print("You don't have enough gold!")
            else:
                print(f"{item_name} is no longer avaible.")
        else:
            print("That item is not available in the shop.")

class Items:
    def __init__(self, items, cost):
        self.type = type
        self.cost = cost


class Player:
    def __init__(self, health, max_health, power, gold, position,turnnumber,shop):
        self.health = health
        self.max_health = max_health
        self.power = power
        self.gold = gold
        self.position = position
        self.turnnumber=turnnumber
        self.shop = shop


    def move(self, direction):
        player.turnnumber+=1
        current_field = self.position
        if direction in current_field.adjacent_fields:
            new_position = current_field.adjacent_fields[direction]
            self.position = new_position
            print(f"Player moved to tile {self.position.name} \n\n")
            print("--------------------------------------------\n\n")

            self.check_field_type()

            self.show_possible_moves()
        else:
            print("You can't move there!")

    def check_field_type(self):
        field_type = self.position.type

        if field_type == "Fountain":
            if not self.position.is_fountain_used:
                self.health = self.max_health
                print(f"Player found secret Fountain! he have been healed. Your current health is: {player.health}")
                self.position.is_fountain_used = True
            else:
                print("the player has reached the Fountain! However, it has already been used.")
        elif field_type == "Shop":
            print("The player has stopped in tavern.")
            self.enter_shop()
        elif field_type == "Goblin Hatchery":
            if self.position.monster is not None:
                print("The player is on Goblin Hatchery field. Beware of the goblins!")
                self.fight(self.position.monster)
            else:
                print("The player has reached an empty field.He is safe, atleast for now")
            self.position.respawn_monster()
        elif field_type == "Goblin":
            if self.position.monster is not None:
                print("The player has encountered a Goblin! Prepare for battle!")
                self.fight(self.position.monster)
            else:
                print("The player has reached an empty field.He is safe, atleast for now")
        elif field_type == "Hydra":
            if self.position.monster is not None:
                print("The player has encountered a Hydra! Prepare for battle!")
                self.fight(self.position.monster)
            else:
                print("The player has reached an empty field.He is safe, atleast for now")
        elif field_type == "Hydra Hatchery":
            if self.position.monster is not None:
                print("The player went straight into Hydra's Hatchery! Beware of incoming Hydras!")
                self.fight(self.position.monster)
            else:
                print("The player has reached an empty field.He is safe, atleast for now")
            self.position.respawn_monster()
        elif field_type == "Boss":
            print("The player is on the final boss field.")
            self.fight(self.position.monster)
        elif field_type == "Empty":
            print("The player has reached an empty field.He is safe, atleast for now")
        elif field_type == "Start":
            print("The player has returned to the start. What are you doing here? Go back to the fight!")


    def enter_shop(self):
        while True:
            self.show_shop()
            choice = input("Do you want to return to the shop? (yes/no): ").lower()
            if choice == "no":
                print("Player left the shop.")
                break


    def show_shop(self):
        print("Avaible items:")
        print(f"Your gold: {self.gold}")
        for item_name, item_info in self.shop.items.items():
            print(f"{item_name}: Power +{item_info['power']}, Cost: {item_info['cost']}, Remaining stock: {item_info['stock']}")

        item_choice = input("Choose an item to buy (or 'exit' to leave): ")
        if item_choice in self.shop.items:
            self.shop.buy_item(self, item_choice)
        elif item_choice.lower() == 'exit':
            print("Player left the shop.")
        else:
            print("That item doesn't exist?.")



    def show_possible_moves(self):
        current_field = self.position
        print(f"Avaible directions: ")
        for direction, field in current_field.adjacent_fields.items():
            print(f"- {direction}: {field.name}")

    def fight(self, Monster):
        winning_chance = (self.power/ (self.power + Monster.power)) * 100

        roll = random.uniform(0, 100)
        print(f"Chance of winning: {winning_chance:.2f}%.")

        if roll <= winning_chance:
            if Monster == Dragon:
                print("You defeated the mighty Dragon! Congratulations, you won the game!")
                print(f"Your final hp was: {player.health}" )
                print(f"It took you: {player.turnnumber} turns")
                exit()


            print(f"WIN!,monster dropped {Monster.goldDrop} gold!")
            self.gold += Monster.goldDrop
            self.position.monster= None


        else:
            print("Sadly, player lost the fight.")
            self.health -= Monster.dmgdealt

            if player.health <= 0:
                print("Well, you lost all of you health, try your luck next time")
                exit()
            else:
                print(f"Your hp dropped to  {self.health}.")

Player1_shop = Shop()
player= Player(50,50,10,2,A1,0,Player1_shop)

def draw_map(player):
    map_layout = [
        [D1, D2, D3, D4],
        [C1, None, None, None],
        [B1, B2, B3, B4],
        [None, None, None, A1]
    ]

    print("MAP:")
    for row in map_layout:
        row_display = ""
        for field in row:
            if field is None:
                row_display += "   |"
            elif field == player.position:
                row_display += " P |"
            else:
                row_display += f" {field.name} |"
        print(row_display)
        print("-" * len(row_display))




draw_map(player)
print(f"Start location: {player.position}")
player.show_possible_moves()



while True:
    move_direction = input("Choose direction (right - R, left - L, up - U, down - D): ").upper()

    if move_direction == "R":
        player.move("right")
    elif move_direction == "L":
        player.move("left")
    elif move_direction == "U":
        player.move("up")
    elif move_direction == "D":
        player.move("down")
    else:
        print("Wrong direction, you can't move into the wall.")

    draw_map(player)



'''
Base idea of map only one way, with back tracking. Hatchery has 80% to respawn monster, to farm gold/stats

Hydra   hydraHatchery  Fountain  Boss(Dragon)
emptyField
goblinHatchery Goblin  Emptyfield   Shop
                                    Start

D1 D2 D3 D4       
C1                              
B1 B2 B3 B4
         A1

10/50/2/none


Dagger+4 cost4 3
Sword +7 cost6 5
throwingKnife +20 cost 16 6
'''
