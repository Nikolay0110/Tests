import pytest
from task_1 import visit   # Импорт функции
from task_1 import geo_logs   # Импорт спичка



@pytest.mark.parametrize('input_list, expected_result',  [
    (geo_logs, [{'visit1': ['Москва', 'Россия']},
                {'visit3': ['Владимир', 'Россия']},
                {'visit7': ['Тула', 'Россия']},
                {'visit8': ['Тула', 'Россия']},
                {'visit9': ['Курск', 'Россия']},
                {'visit10': ['Архангельск', 'Россия']}]),
    ([], []),
    ([{'visit1': ['Москва', 'Россия']}], [{'visit1': ['Москва', 'Россия']}]),
    ([{'visit1': ['Москва', 'Россия']}, {'visit2': ['Дели', 'Индия']}], [{'visit1': ['Москва', 'Россия']}]),
])


def test_visit(input_list, expected_result):
    assert visit(input_list) == expected_result
