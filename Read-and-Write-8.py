
#  -*-  coding: utf-8  -*-

def data_input(file_name):
    full_dishes = {}
    with open(file_name, 'r', encoding='utf8') as in_file:
        for word_line in in_file:
            dish = word_line.strip()
            word_line = in_file.readline().strip()
            quantity = int(word_line)
            composition = []
            for i in range(quantity):
                ingredients = {}
                word_line = in_file.readline().strip().rsplit('|', 2)
                ingredients['raw'] = word_line[0]
                ingredients['weight'] = int(word_line[1])
                ingredients['unit'] = word_line[2]
                composition.append(ingredients)
            full_dishes[dish] = composition
            word_line = in_file.readline()
    return full_dishes

def data_print(full_dishes):
    print('\n         Исходные данные:\n cook_book = {', end='')
    id_key = 1
    for key, value in full_dishes.items():
        if id_key == 1:
            print(f'\n     {key}:[', end='')
        else:
            print(f',\n     {key}:[', end='')
        id_val = 1
        for entry in value:
            if id_val == 1:
                print(f'\n         {entry}', end='')
            else:
                print(f',\n         {entry}', end='')
            id_val += 1
        print('\n     ]', end='')
        id_key += 1
    print('\n }')
    return

def get_shop_list_by_dishes(full_dishes, dishes_list, persons=1):
    get_list = {}
    for entry in dishes_list:
        for key, value in full_dishes.items():
            if entry == key:
                for ingredient in value:
                    weight = ingredient['weight']
                    if ingredient['raw'] not in get_list.keys():
                        quantity = {}
                        quantity['unit'] = ingredient['unit']
                        quantity['weight'] = weight
                        get_list[ingredient['raw']] = quantity
                    else:
                        get_list[ingredient['raw']]['weight'] += weight
    if persons > 1:
        for value in get_list.values():
            value['weight'] *= persons
    return get_list

def print_shop_list(shop_list_by_dishes):
    print('\n         Список необходимых товаров:\n shop_list_by_dishes = {', end='')
    idx = 1
    for key, value in shop_list_by_dishes.items():
        if idx == 1:
            print(f'\n     {key}: {value}', end='')
        else:
            print(f',\n     {key}: {value}', end='')
        idx += 1
    print('\n }')
    return


#                                         Головной блок
#                  1. Считать список рецептов из внешнего файла.
cook_book = data_input('input_8.txt')

data_print(cook_book)

#                  2. Вычислить количество ингредиентов для приготовления заданных блюда.
shop_list = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
print_shop_list(shop_list)

shop_list = get_shop_list_by_dishes(cook_book, ['Омлет', 'Омлет'], 1)
print_shop_list(shop_list)


# print('\n  -- Конец --  ')  #                 - Для блокнота
input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
