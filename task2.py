from pprint import pprint
cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as f:
    dish_name = f.readline().strip()

    while dish_name:
        ingredients_count=int(f.readline().strip())
        ingredients_list = []

        for _ in range(ingredients_count):
            ingredient = f.readline().strip()
            parts = ingredient.split(' | ')
            ingredient_dict = {
                'ingredient_name': parts[0],
                'quantity': int(parts[1]),
                'measure': parts[2]
            }
            ingredients_list.append(ingredient_dict)

        cook_book[dish_name]=ingredients_list

        f.readline()
        dish_name = f.readline().strip()

# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            ingredient_quantity = ingredient['quantity']*person_count
            ingredient_measure = ingredient['measure']

            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += ingredient_quantity
            else:
                shop_list[ingredient_name] = {
                    'measure': ingredient_measure,
                    'quantity': ingredient_quantity
                }

    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



