import pytest
from task_2 import unique_id   # Импорт функции
from task_2 import ids   # Импорт словаря

@pytest.mark.parametrize('input_data, expected_result', [
    (ids, [98, 35, 15, 213, 54, 119]),
])

def test_unique_id(input_data, expected_result):
    assert unique_id(input_data) == expected_result
