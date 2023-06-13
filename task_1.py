from pprint import pprint

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def visit(some_list):
    geo_log = []
    for logs in some_list:
        for k, v in logs.items():
            if 'Россия' in v:
                geo_log.append(logs)

    return geo_log

if __name__ == '__main__':
    pprint(visit(geo_logs))