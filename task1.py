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

        print(cook_book)

