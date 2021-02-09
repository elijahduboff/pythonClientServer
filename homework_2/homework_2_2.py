import json


def write_order_to_json(item, quntity, price, buyer, date):
    new_order = {
        'item': item,
        'quantity': quntity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json', 'r', encoding='windows-1251') as fn:
        json_data = json.load(fn)
        json_data['orders'].append(new_order)

    with open('orders.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)


write_order_to_json('Игрушка', 1, 1000, 'Иванов', '04-02-2021')
