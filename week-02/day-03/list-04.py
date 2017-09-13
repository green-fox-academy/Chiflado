shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)

wrong_item_01 = shop_items.index(2) 
wrong_item_02 = shop_items.index(False)

shop_items[wrong_item_01] = "Croissant"
shop_items[wrong_item_02] = "Ice Cream"

print(shop_items)