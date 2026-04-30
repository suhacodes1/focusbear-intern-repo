import pytest
from utils import calculate_task_completion_rate


def test_completion_rate_normal_case():
    assert calculate_task_completion_rate(8, 10) == 80.0


def test_completion_rate_zero_total_tasks():
    assert calculate_task_completion_rate(5, 0) == 0


def test_completion_rate_with_decimal_result():
    assert calculate_task_completion_rate(1, 3) == 33.33


def test_completion_rate_negative_values():
    with pytest.raises(ValueError):
        calculate_task_completion_rate(-1, 10)