import random

class Artifacts:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def display_list(lst):
    print("\nAdventurer's Emporium:")
    total = 0
    if not lst:
        print("Your inventory is empty.")
    else:
        for i, item in enumerate(lst, 1):
            print(f"{i}. {item.name} - {item.price} Gold")
            total += item.price
        print(f"Total: {total} Gold")

def checkout(lst, emporium_items, gold):
    total_cost = len(emporium_items) * 100  
    if gold < total_cost:
        print("\nYou don't have enough gold to buy all these items son.")
        return gold
    print("\nChecking out...")
    for item in emporium_items:
        lst.append(Artifacts(item, 100))  
    print("You have purchased all the items in your List.")
    return gold - total_cost

if __name__ == "__main__":
    shopping = True
    shop_list = []
    gold = random.randint(1000, 1200)

    while shopping:
        print("\n\n\nWelcome to the Guild Market\n\n"
              f"[G] Gold: {gold}\n\n"  
              "[S] Shop\n"
              "[L] List\n"
              "[E] Exit\n")
        option = input("Enter your choice: ").upper()

        if option == 'S':
            while True:
                print("\n\n\nWhat're you here for kid?\n\n"
                      "[W] Blacksmith Weapons\n"
                      "[P] Alchemy Potions\n"
                      "[M] Mystic Armaments\n"
                      "[A] Body Armor\n\n"
                      "[E] Leave Market\n"
                      "[R] Return to Main Menu\n"
                      "[C] Checkout from Adventurer's Emporium\n")
                option2 = input("Enter your choice: ").upper()

                if option2 == 'E':
                    print("\n\n\nSee you next time kid...\n\n")
                    shopping = False
                    break

                elif option2 == 'R':
                        continue

                elif option2 == 'C':
                    emporium_items = ["Spear of the Holy Blood", 
                                      "Dragon Bone Battle Scythe", 
                                      "Orc Battle Axe", 
                                      "Great Bow",
                                      "Elixir of Life", 
                                      "Potion of Strength", 
                                      "Healing Concoction", 
                                      "Bottle o' Enchanting",
                                      "Thistlewind", 
                                      "Magic Robe", 
                                      "Demonic Wings", 
                                      "Ebony Elven Bow",
                                      "Full Mithril Armor", 
                                      "Red Dragon Armor", 
                                      "Dwarven Infused Armor", 
                                      "Adamantine Shield"]
                    print(f"Gold before checkout: {gold}")
                    new_gold = checkout(shop_list, emporium_items, gold)
                    print(f"Gold after checkout: {new_gold}")
                    if new_gold is not None:
                        gold = new_gold
                        print(f"Updated gold: {gold}")
                        continue
                
                elif option2 in ['W', 'P', 'M', 'A']:
                    items = {
                        'W': ["Spear of the Holy Blood", 
                              "Dragon Bone Battle Scythe", 
                              "Orc Battle Axe", 
                              "Great Bow"],
                        'P': ["Elixir of Life", 
                              "Potion of Healing", 
                              "Healing Concoction", 
                              "Bottle o' Enchanting"],
                        'M': ["Thistlewind", 
                              "Magic Robe", 
                              "Demonic Wings", 
                              "Ebony Elven Bow"],
                        'A': ["Full Mithril Armor", 
                              "Red Dragon Armor", 
                              "Dwarven Infused Armor", 
                              "Adamantine Shield"]
                    }
                    
                    print("\n\n\nSee what you need...\n")
                    for i, item in enumerate(items[option2], 1):
                        print(f"[{i}] {item}")
                    
                    option3 = int(input("\n\nEnter your choice : "))
                    if 1 <= option3 <= 4:
                        chosen_item = items[option2][option3 - 1]
                        print(f"\nYou chose: {chosen_item}\n")

                        print("\n[A] Add to list\n"
                              "[C] Cancel\n\n"
                              "Enter an Option: ")
                        option4 = (input())

                        if option4 == 'A' or option4 == 'a':
                            shop_list.append(Artifacts(chosen_item, 100))  
                            print(f"\nYou've added {chosen_item} to your list")
                            break
                            
                        elif option4 == 'C' or option4 == 'c':
                            continue  
                        
                        else:
                            print("\nInvalid option")

                else:
                    print("Invalid option")
        
        elif option == 'L':
            while True:
                display_list(shop_list)
                print("\n[C] Checkout from Adventurer's Emporium\n"
                      "[M] Main Menu\n")
                sub_option = input("Enter your choice: ").upper()

                if sub_option == 'C':
                    emporium_items = ["Spear of the Holy Blood", 
                                      "Dragon Bone Battle Scythe", 
                                      "Orc Battle Axe", 
                                      "Great Bow",
                                      "Elixir of Life", 
                                      "Potion of Haste", 
                                      "Bravesmite Concoction", 
                                      "Bottle o' Enchanting",
                                      "Thistlewind", 
                                      "Magic Robe", 
                                      "Demonic Wings", 
                                      "Ebony Elven Bow",
                                      "Full Mithril Armor", 
                                      "Red Dragon Armor", 
                                      "Dwarven Infused Armor", 
                                      "Adamantine Shield"]
                    gold = checkout(shop_list, emporium_items, gold)
                    break

                elif sub_option == 'M':
                    break

                else:
                    print("Invalid option")

        elif option == 'E':
            print("\n\nSee you next time kid...\n\n")
            shopping = False

        else:
            print("Invalid option")