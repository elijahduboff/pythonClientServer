# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
# с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;

import yaml


def write_check_yaml():
    data_for_yaml = {
        'key_1': ['строка', 'string', 1, 1.02],
        'key_2': 124942,
        'key_3': {
            '1': f'{30}U+20AC',
            '2': f'{20}U+20AC',
            '3': f'{10}U+20AC'
        }
    }
    with open('file.yaml', 'w') as file:
        yaml.dump(data_for_yaml, file, default_flow_style=False, allow_unicode=True)

    with open('file.yaml', 'r') as file:
        data_from_yaml = yaml.load(file, Loader=yaml.FullLoader)

    print(data_from_yaml == data_from_yaml)


write_check_yaml()
