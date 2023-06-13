import pytest
from task_3 import maximus   # Импорт функции
from task_3 import stats   # Импорт словаря

@pytest.mark.parametrize('input_data, expected_result', [
    (stats, 'yandex'),
])

def test_maximus(input_data, expected_result):
    assert maximus(input_data) == expected_result