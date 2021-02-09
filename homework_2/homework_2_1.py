import re
import csv

files = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data(files):
    os_name_list_temp = []
    os_prod_list_temp = []
    os_code_list_temp = []
    os_type_list_temp = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in files:
        with open(file, 'r', encoding='windows-1251') as fn:
            data = fn.read()
            data = re.sub(r'\s{2,30}', ',', data)
            os_name_list_temp.append(re.findall(r'(?<=Название\s\w{2}:,)([a-zA-Zа-яА-Я0-9 ]*)', data))
            os_name_list = list(map(lambda x: x[0], os_name_list_temp))
            os_prod_list_temp.append(re.findall(r'(?<=Изготовитель\sОС:,)([a-zA-Zа-яА-Я0-9 ]*)', data))
            os_prod_list = list(map(lambda x: x[0], os_prod_list_temp))
            os_code_list_temp.append(re.findall(r'(?<=Код\sпродукта:,)([a-zA-Zа-яА-Я0-9- ]*)', data))
            os_code_list = list(map(lambda x: x[0], os_code_list_temp))
            os_type_list_temp.append(re.findall(r'(?<=Тип\sсистемы:,)([a-zA-Zа-яА-Я0-9- ]*)', data))
            os_type_list = list(map(lambda x: x[0], os_type_list_temp))
    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)
    return main_data


def write_in_csv(filename):
    data_for_writing = get_data(files)
    with open(filename, 'w') as fn:
        fn_csv_writer = csv.writer(fn)
        for item in data_for_writing:
            fn_csv_writer.writerow(item)


write_in_csv('result_1.csv')
