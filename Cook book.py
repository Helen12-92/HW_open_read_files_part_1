cook_book = {}

with open('recipes (1).txt', encoding="utf-8") as f:
    for i in f:
        dish = i.strip()
        count = int(f.readline())
        ingredients = []
        for l in range(count):
            ingredient_line = f.readline().strip()
            ingredient_name, quantity, measure = ingredient_line.split(' | ')
            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients.append(ingredient)
        cook_book[dish] = ingredients
        f.readline()

def get_shop_list_by_dishes(dishes, person_count):
    get_shop_list = {}
    for d in dishes:
        if d in cook_book:
            for ingredients in cook_book[d]:
                if ingredients['ingredient_name'] in get_shop_list:
                    get_shop_list[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
                else:
                    get_shop_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'], 'quantity': int(ingredients['quantity']) * person_count}
        else:
            print('Not found dishes')
    print(get_shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


            













    

